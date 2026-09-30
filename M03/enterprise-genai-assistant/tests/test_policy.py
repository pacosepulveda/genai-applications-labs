from src.models import DraftRequest, Confidentiality
from src.policy import evaluate_request

def test_confidential_is_blocked_before_router():
    req = DraftRequest(
        task="Resume este documento",
        confidentiality=Confidentiality.CONFIDENTIAL
    )
    decision = evaluate_request(req)
    assert decision.allowed is False
