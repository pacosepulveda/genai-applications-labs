from types import SimpleNamespace
from src.rag import RAGAnswer, validate_citations

def doc(source_id, status="CURRENT"):
    return SimpleNamespace(metadata={"source_id":source_id,"status":status})

def test_valid_citations():
    answer = RAGAnswer(
        answer="Respuesta",
        source_ids=["PROC-017"],
        insufficient_evidence=False,
    )
    assert validate_citations(answer,[doc("PROC-017")]) is True

def test_invented_citation_rejected():
    answer = RAGAnswer(
        answer="Respuesta",
        source_ids=["FAKE-999"],
        insufficient_evidence=False,
    )
    assert validate_citations(answer,[doc("PROC-017")]) is False

def test_obsolete_citation_rejected():
    answer = RAGAnswer(
        answer="Respuesta",
        source_ids=["PROC-017"],
        insufficient_evidence=False,
    )
    assert validate_citations(answer,[doc("PROC-017","OBSOLETE")]) is False
