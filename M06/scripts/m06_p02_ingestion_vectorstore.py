from pathlib import Path
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
if not KB.exists():
    KB = Path("assets/knowledge_base")

documents, chunks, store = build_store(KB)

print("DOCUMENTOS")
for doc in documents:
    print(doc.metadata.get("source_id"), doc.metadata.get("version"), doc.metadata.get("status"))
print("\nCHUNKS:", len(chunks))

queries = [
    "¿Cuánto dura un acceso privilegiado?",
    "¿Cuándo se envían actualizaciones de un P1?",
]

for query in queries:
    print("\nQUERY:", query)
    docs = store.similarity_search(query, k=4)
    for doc in docs:
        print(
            doc.metadata.get("source_id"),
            doc.metadata.get("version"),
            doc.metadata.get("status"),
            doc.page_content[:120].replace("\n", " "),
        )
    safe_docs = only_current(docs)
    assert all(d.metadata.get("status") == "CURRENT" for d in safe_docs)
    print("CURRENT:", [(d.metadata.get("source_id"), d.metadata.get("version")) for d in safe_docs])
