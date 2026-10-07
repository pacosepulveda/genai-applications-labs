from dataclasses import dataclass, field
import re

from .models import DraftRequest, Confidentiality


@dataclass
class PolicyDecision:
    allowed: bool
    reason: str | None = None
    warnings: list[str] = field(default_factory=list)


_PROMPT_INJECTION_PATTERNS = (
    r"\bignora\b.{0,60}\binstrucciones\b",
    r"\bolvida\b.{0,60}\b(?:reglas|instrucciones)\b",
    r"\bsystem\s+prompt\b",
    r"\binstrucciones\s+internas\b",
    r"\bmodo\s+administrador\b",
)

_SECRET_PATTERNS = (
    r"\bapi[_-]?key\s*[:=]\s*\S+",
    r"\b(?:password|passwd|secret|token)\s*[:=]\s*\S+",
    r"\bsk-[A-Za-z0-9_-]{10,}\b",
)


def _matches_any(text: str, patterns: tuple[str, ...]) -> bool:
    return any(
        re.search(pattern, text, flags=re.IGNORECASE)
        for pattern in patterns
    )


def evaluate_request(req: DraftRequest) -> PolicyDecision:
    if req.confidentiality in {
        Confidentiality.CONFIDENTIAL,
        Confidentiality.RESTRICTED,
    }:
        return PolicyDecision(False, "data_classification")

    if _matches_any(req.task, _PROMPT_INJECTION_PATTERNS):
        return PolicyDecision(False, "prompt_injection")

    if _matches_any(req.task, _SECRET_PATTERNS):
        return PolicyDecision(False, "sensitive_information")

    return PolicyDecision(
        True,
        warnings=["La salida requiere revisión humana."],
    )
