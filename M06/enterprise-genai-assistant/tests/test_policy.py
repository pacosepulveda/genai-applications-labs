from src.models import AskRequest, AskTask
from src.policy import choose_mode

def test_authoritative_sources_force_rag():
    req = AskRequest(
        question="¿Cuál es el procedimiento vigente?",
        requires_authoritative_sources=True,
    )
    assert choose_mode(req).mode == "RAG"

def test_corporate_knowledge_forces_rag():
    req = AskRequest(
        question="¿Cuánto dura un acceso privilegiado?",
        task=AskTask.CORPORATE_KNOWLEDGE,
    )
    assert choose_mode(req).mode == "RAG"
