from dataclasses import dataclass


@dataclass
class VisualPolicyDecision:
    allowed: bool
    reason: str | None = None


ALLOWED_PROVIDERS = {"mock", "bedrock"}

# Controles educativos deliberadamente simples.
BLOCKED_PATTERNS = [
    "suplanta a una persona real",
    "hazte pasar por una persona real",
    "impersonate a real person",
    "genera credenciales de acceso",
    "generate access credentials",
    "documento oficial falso",
    "fake official document",
]


def evaluate_visual_request(prompt: str, provider: str) -> VisualPolicyDecision:
    if not prompt.strip():
        return VisualPolicyDecision(False, "empty_prompt")

    if provider not in ALLOWED_PROVIDERS:
        return VisualPolicyDecision(False, "unknown_provider")

    lower = prompt.lower()

    for pattern in BLOCKED_PATTERNS:
        if pattern in lower:
            return VisualPolicyDecision(False, "visual_policy")

    return VisualPolicyDecision(True)
