
from transformers import (
    AutoConfig,
    AutoTokenizer,
    AutoModel,
    AutoModelForCausalLM,
    AutoModelForSeq2SeqLM,
)
import torch
import pandas as pd

MODEL_IDS = {
    "BERT": "google/bert_uncased_L-2_H-128_A-2",
    "Decoder": "HuggingFaceTB/SmolLM2-135M-Instruct",
    "T5": "google/flan-t5-small",
}

config_rows = []
for family, model_id in MODEL_IDS.items():
    cfg = AutoConfig.from_pretrained(model_id)
    config_rows.append({
        "family": family,
        "model_id": model_id,
        "model_type": getattr(cfg, "model_type", None),
        "is_encoder_decoder": getattr(cfg, "is_encoder_decoder", False),
        "hidden_size": getattr(cfg, "hidden_size", getattr(cfg, "d_model", None)),
        "vocab_size": getattr(cfg, "vocab_size", None),
    })
print(pd.DataFrame(config_rows).to_string(index=False))

bert_tok = AutoTokenizer.from_pretrained(MODEL_IDS["BERT"])
bert = AutoModel.from_pretrained(MODEL_IDS["BERT"])
bert.eval()
bert_inputs = bert_tok("The service is available.", return_tensors="pt")
with torch.no_grad():
    bert_out = bert(**bert_inputs)
print("BERT last_hidden_state:", tuple(bert_out.last_hidden_state.shape))

chat_tok = AutoTokenizer.from_pretrained(MODEL_IDS["Decoder"])
chat_model = AutoModelForCausalLM.from_pretrained(MODEL_IDS["Decoder"])
chat_model.eval()

messages = [
    {"role": "system", "content": "You are a concise technical assistant."},
    {"role": "user", "content": "Explain what an API gateway is in one sentence."},
]

formatted = chat_tok.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
print("\nCHAT TEMPLATE\n", formatted)

chat_inputs = chat_tok(formatted, return_tensors="pt")
with torch.no_grad():
    generated = chat_model.generate(
        **chat_inputs,
        max_new_tokens=40,
        do_sample=False,
    )
new_tokens = generated[0, chat_inputs["input_ids"].shape[1]:]
print("Respuesta:", chat_tok.decode(new_tokens, skip_special_tokens=True))

seq_tok = AutoTokenizer.from_pretrained(MODEL_IDS["T5"])
seq_model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_IDS["T5"])
seq_model.eval()

text = (
    "summarize: The service was degraded for twenty minutes because of an incorrect "
    "configuration. There was no data loss and the change was rolled back."
)
seq_inputs = seq_tok(text, return_tensors="pt", truncation=True)
with torch.no_grad():
    seq_out = seq_model.generate(**seq_inputs, max_new_tokens=40)
print("T5:", seq_tok.decode(seq_out[0], skip_special_tokens=True))

architecture_table = pd.DataFrame([
    {"task": "clasificación", "fit": "encoder-only"},
    {"task": "NER", "fit": "encoder-only"},
    {"task": "completado", "fit": "decoder-only"},
    {"task": "chatbot", "fit": "decoder-only / chat model"},
    {"task": "traducción", "fit": "encoder-decoder o LLM generativo"},
    {"task": "resumen", "fit": "encoder-decoder o LLM generativo"},
])
print("\nArquitecturas orientativas")
print(architecture_table.to_string(index=False))
