from dataclasses import dataclass
import re

@dataclass
class TextPolicyDecision:
    allowed: bool
    reason: str | None = None

_PROMPT_INJECTION_PATTERNS = (
    r"\bignora\b.{0,60}\binstrucciones\b",
    r"\bolvida\b.{0,60}\b(?:reglas|instrucciones)\b",
    r"\bsystem\s+prompt\b",
    r"\binstrucciones\s+internas\b",
)
_SECRET_PATTERNS = (
    r"\bapi[_-]?key\s*[:=]\s*\S+",
    r"\b(?:password|passwd|secret|token)\s*[:=]\s*\S+",
    r"\bsk-[A-Za-z0-9_-]{10,}\b",
)

def _matches_any(text: str, patterns: tuple[str, ...]) -> bool:
    return any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in patterns)

def evaluate_text(text: str, max_chars: int) -> TextPolicyDecision:
    if not text.strip():
        return TextPolicyDecision(False, "empty_input")
    if len(text) > max_chars:
        return TextPolicyDecision(False, "input_too_large")
    if "CONFIDENTIAL:" in text or "RESTRICTED:" in text:
        return TextPolicyDecision(False, "data_classification")
    if _matches_any(text, _PROMPT_INJECTION_PATTERNS):
        return TextPolicyDecision(False, "prompt_injection")
    if _matches_any(text, _SECRET_PATTERNS):
        return TextPolicyDecision(False, "sensitive_information")
    return TextPolicyDecision(True)
