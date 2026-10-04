from dataclasses import dataclass


@dataclass
class VisualPolicyDecision:
    allowed: bool
    reason: str | None = None


ALLOWED_PROVIDERS = {"mock", "local_gan", "bedrock"}

BLOCKED_PATTERNS = [
    # TODO M04.P06:
    # añade expresiones simples para las categorías indicadas en el enunciado.
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
