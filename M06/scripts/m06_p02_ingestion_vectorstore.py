from pathlib import Path
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

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
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )
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
