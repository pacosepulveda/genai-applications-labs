from src.models import DraftRequest, Confidentiality
from src.policy import evaluate_request

def test_internal_draft_is_allowed():
    req = DraftRequest(task="Redacta un borrador de aviso de mantenimiento", confidentiality=Confidentiality.INTERNAL)
    assert evaluate_request(req).allowed is True

def test_confidential_is_blocked_for_m01():
    req = DraftRequest(task="Resume este documento", confidentiality=Confidentiality.CONFIDENTIAL)
    assert evaluate_request(req).allowed is False

def test_authoritative_source_request_is_blocked_without_rag():
    req = DraftRequest(task="Dime la política vigente", requires_authoritative_sources=True)
    assert evaluate_request(req).allowed is False
