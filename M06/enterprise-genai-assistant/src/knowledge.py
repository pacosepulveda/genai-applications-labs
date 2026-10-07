from dataclasses import dataclass
from pathlib import Path

@dataclass
class KnowledgeRecord:
    page_content: str
    metadata: dict


def parse_markdown_document(path: Path) -> KnowledgeRecord:
    text = path.read_text(encoding="utf-8")
    metadata = {"file": path.name}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            body = parts[2].strip()
            for line in parts[1].splitlines():
                if ":" in line:
                    key, value = line.split(":", 1)
                    metadata[key.strip()] = value.strip().strip('"')
    return KnowledgeRecord(page_content=body, metadata=metadata)


def load_current_records(root: Path) -> list[KnowledgeRecord]:
    records = []
    for path in sorted(root.glob("*.md")):
        record = parse_markdown_document(path)
        if record.metadata.get("status") == "OBSOLETE":
            continue
        records.append(record)
    return records


class KnowledgeService:
    def __init__(
        self,
        root: Path,
        embedding_model_id: str,
        top_k: int = 3,
        min_relevance_score: float = 0.20,
    ):
        self.root = root
        self.embedding_model_id = embedding_model_id
        self.top_k = top_k
        self.min_relevance_score = min_relevance_score
        self.vector_store = None

    def build(self):
        from langchain_core.documents import Document
        from langchain_text_splitters import RecursiveCharacterTextSplitter
        from langchain_huggingface import HuggingFaceEmbeddings
        from langchain_core.vectorstores import InMemoryVectorStore

        records = load_current_records(self.root)
        documents = [
            Document(page_content=r.page_content, metadata=r.metadata)
            for r in records
        ]
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=80,
        )
        chunks = splitter.split_documents(documents)
        embeddings = HuggingFaceEmbeddings(
            model_name=self.embedding_model_id,
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
        )
        self.vector_store = InMemoryVectorStore(embeddings)
        self.vector_store.add_documents(chunks)
        return self

    def retrieve(self, query: str):
        if self.vector_store is None:
            self.build()

        if hasattr(self.vector_store, "similarity_search_with_score"):
            scored = self.vector_store.similarity_search_with_score(
                query,
                k=self.top_k,
            )
            docs = [
                doc for doc, score in scored
                if float(score) >= self.min_relevance_score
            ]
        else:
            docs = self.vector_store.similarity_search(query, k=self.top_k)

        return [
            d for d in docs
            if d.metadata.get("status") == "CURRENT"
        ]
