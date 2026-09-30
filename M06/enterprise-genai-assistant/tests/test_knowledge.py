from pathlib import Path
from src.knowledge import parse_markdown_document, load_current_records

def test_obsolete_document_is_excluded():
    root = Path("data/knowledge_base")
    current = load_current_records(root)
    assert all(x.metadata.get("status") != "OBSOLETE" for x in current)

def test_current_proc_017_is_version_3_2():
    root = Path("data/knowledge_base")
    docs = [
        x for x in load_current_records(root)
        if x.metadata.get("source_id") == "PROC-017"
    ]
    assert len(docs) == 1
    assert docs[0].metadata["version"] == "3.2"
    assert "8 horas" in docs[0].page_content
    assert "24 horas" not in docs[0].page_content
