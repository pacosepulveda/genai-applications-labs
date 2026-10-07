
import json
import re
from collections import Counter
from pathlib import Path
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_ID = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_ID)
model.eval()

def locate_cases():
    candidates = [
        Path("../assets/nlp_eval_cases.jsonl"),
        Path("assets/nlp_eval_cases.jsonl"),
        Path("M05/assets/nlp_eval_cases.jsonl"),
    ]
    for p in candidates:
        if p.exists():
            return p
    raise FileNotFoundError(candidates)

cases = [
    json.loads(line)
    for line in locate_cases().read_text(encoding="utf-8").splitlines()
    if line.strip()
]

def generate(instruction, max_new_tokens=120, num_beams=1, do_sample=False):
    encoded = tokenizer(
        instruction,
        return_tensors="pt",
        truncation=True,
    )
    kwargs = {
        "max_new_tokens": max_new_tokens,
        "num_beams": num_beams,
        "do_sample": do_sample,
    }
    if do_sample:
        kwargs.update({"temperature": 0.8, "top_p": 0.9})
    with torch.no_grad():
        out = model.generate(**encoded, **kwargs)
    return tokenizer.decode(out[0], skip_special_tokens=True)

def words(text):
    return re.findall(r"\w+", text.lower(), flags=re.UNICODE)

def rouge1_recall(candidate, reference):
    cand = Counter(words(candidate))
    ref = Counter(words(reference))
    if not ref:
        return 0.0
    overlap = sum((cand & ref).values())
    return overlap / sum(ref.values())

def contains_all(text, required):
    lower = text.lower()
    return all(item.lower() in lower for item in required)

results = []

for case in cases:
    task = case["task"]

    if task == "summarize":
        instruction = "Summarize faithfully in Spanish, preserving concrete facts: " + case["input"]
        output = generate(instruction, max_new_tokens=100, num_beams=2)
        metric = rouge1_recall(output, case["reference"])
        constraints_ok = contains_all(output, case.get("must_include", []))
        unsupported = []

    elif task == "translate_en":
        instruction = (
            "Translate to English. Preserve identifiers, codes, paths and placeholders exactly: "
            + case["input"]
        )
        output = generate(instruction, max_new_tokens=120, num_beams=2)
        protected = case.get("protected", [])
        constraints_ok = all(item in output for item in protected)
        metric = rouge1_recall(output, case["reference"])
        unsupported = []

    elif task == "generate":
        instruction = case["input"] + " Do not invent dates, times or facts not supplied."
        output = generate(instruction, max_new_tokens=90, num_beams=1)
        unsupported = []
        for pattern in [r"\b\d{1,2}:\d{2}\b", r"\b\d{1,2}/\d{1,2}(?:/\d{2,4})?\b"]:
            for match in re.findall(pattern, output):
                if match not in case["input"]:
                    unsupported.append(match)
        constraints_ok = len(unsupported) == 0
        metric = None

    else:
        continue

    results.append({
        "case_id": case["id"],
        "task": task,
        "output": output,
        "metric_rouge1_recall": metric,
        "constraints_ok": constraints_ok,
        "unsupported_claims": unsupported,
        "notes": "Revisión humana recomendada",
    })

results_df = pd.DataFrame(results)
print(results_df.to_string(index=False))
results_df.to_csv("m05_eval_results.csv", index=False)

case = next(c for c in cases if c["id"] == "SUM-01")
instruction = "Summarize faithfully in Spanish: " + case["input"]

comparisons = {
    "greedy": generate(instruction, max_new_tokens=90, num_beams=1, do_sample=False),
    "beam_4": generate(instruction, max_new_tokens=90, num_beams=4, do_sample=False),
}

torch.manual_seed(42)
comparisons["sampling"] = generate(instruction, max_new_tokens=90, num_beams=1, do_sample=True)

for name, output in comparisons.items():
    print("\n", name, "\n", output)
