from dataclasses import dataclass, field
from .models import DraftRequest, Confidentiality
from .settings import settings

@dataclass
class PolicyDecision:
    allowed: bool
    reason: str | None = None
    warnings: list[str] = field(default_factory=list)

def evaluate_request(req: DraftRequest) -> PolicyDecision:
    if len(req.task) > settings.max_input_chars:
        return PolicyDecision(False, "input_too_long")

    # TODO M01.P03
    # 1) bloquear CONFIDENTIAL y RESTRICTED
    # 2) bloquear requires_authoritative_sources=True

    # TODO M01.P04
    # Añadir detección educativa de prompt injection directa y posibles secretos.

    return PolicyDecision(True, warnings=["La salida es un borrador y requiere revisión humana."])
