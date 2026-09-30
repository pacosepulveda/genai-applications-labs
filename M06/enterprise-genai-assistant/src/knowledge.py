from dataclasses import dataclass
from pathlib import Path
import re

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
            raw_meta = parts[1]
            body = parts[2].strip()
            for line in raw_meta.splitlines():
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
    def __init__(self, root: Path, embedding_model_id: str, top_k: int = 3):
        self.root = root
        self.embedding_model_id = embedding_model_id
        self.top_k = top_k
        self.vector_store = None

    def build(self):
        # TODO M06.P06:
        # 1) KnowledgeRecord -> LangChain Document
        # 2) RecursiveCharacterTextSplitter
        # 3) embeddings
        # 4) InMemoryVectorStore
        raise NotImplementedError

    def retrieve(self, query: str):
        # TODO M06.P06
        raise NotImplementedError
