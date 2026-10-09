from pathlib import Path
import json
import torch
from transformers import AutoTokenizer, AutoModel
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore

class LocalHFEmbeddings:
    def __init__(self, model_name: str):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        self.model.eval()

    def _encode(self, texts):
        batch = self.tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
        with torch.no_grad():
            hidden = self.model(**batch).last_hidden_state
        mask = batch["attention_mask"].unsqueeze(-1).to(hidden.dtype)
        pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1e-9)
        normalized = torch.nn.functional.normalize(pooled, p=2, dim=1)
        return normalized.cpu().tolist()

    def embed_documents(self, texts):
        return self._encode(texts)

    def embed_query(self, text):
        return self._encode([text])[0]

def parse_markdown(path: Path) -> Document:
    text = path.read_text(encoding="utf-8")
    metadata = {"file": path.name}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        raw_meta = parts[1]
        body = parts[2].strip()
        for line in raw_meta.splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                metadata[key.strip()] = value.strip().strip('"')
    return Document(page_content=body, metadata=metadata)

def build_store(kb_path: Path):
    documents = [parse_markdown(p) for p in sorted(kb_path.glob("*.md"))]
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=80)
    chunks = splitter.split_documents(documents)
    embeddings = LocalHFEmbeddings("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    store = InMemoryVectorStore(embeddings)
    store.add_documents(chunks)
    return documents, chunks, store

def only_current(docs):
    return [d for d in docs if d.metadata.get("status") == "CURRENT"]

KB = Path("../assets/knowledge_base")
EVAL = Path("../assets/retrieval_eval.jsonl")
if not KB.exists():
    KB = Path("assets/knowledge_base")
    EVAL = Path("assets/retrieval_eval.jsonl")

_, _, store = build_store(KB)
cases = [json.loads(line) for line in EVAL.read_text(encoding="utf-8").splitlines() if line.strip()]

def evaluate_case(case, k):
    docs = only_current(store.similarity_search(case["question"], k=k))
    source_ids = [d.metadata.get("source_id") for d in docs]
    if case["expected_status"] == "NO_EVIDENCE":
        return {
            "id": case["id"],
            "expected": [],
            "retrieved": source_ids,
            "is_no_evidence_case": True,
            "hit": None,
        }
    hit = any(s in case["expected_source_ids"] for s in source_ids)
    return {
        "id": case["id"],
        "expected": case["expected_source_ids"],
        "retrieved": source_ids,
        "is_no_evidence_case": False,
        "hit": hit,
    }

def hit_rate_at_k(rows):
    positive = [r for r in rows if not r["is_no_evidence_case"]]
    return sum(bool(r["hit"]) for r in positive) / len(positive) if positive else 0.0

for k in [2, 4]:
    rows = [evaluate_case(case, k) for case in cases]
    print("\nk =", k)
    for row in rows:
        print(row)
    print("Hit Rate@", k, "=", hit_rate_at_k(rows))

print("\nDecisión recomendada: empezar con k=2 y aumentar solo si el eval set demuestra falta de cobertura.")
