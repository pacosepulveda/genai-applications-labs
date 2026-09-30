from dataclasses import dataclass, field
from .models import DraftRequest, Confidentiality

@dataclass
class PolicyDecision:
    allowed: bool
    reason: str | None = None
    warnings: list[str] = field(default_factory=list)

def evaluate_request(req: DraftRequest) -> PolicyDecision:
    if req.confidentiality in {Confidentiality.CONFIDENTIAL, Confidentiality.RESTRICTED}:
        return PolicyDecision(False, "data_classification")
    return PolicyDecision(True, warnings=["La salida requiere revisión humana."])
