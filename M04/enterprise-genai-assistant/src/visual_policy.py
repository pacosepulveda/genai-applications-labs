from dataclasses import dataclass


@dataclass
class VisualPolicyDecision:
    allowed: bool
    reason: str | None = None


ALLOWED_PROVIDERS = {"mock", "bedrock"}

# Reglas educativas deliberadamente sencillas.
# TODO M04.P06: completa una o más expresiones representativas
# para cada una de las categorías del enunciado.
BLOCKED_PATTERNS = [
    # suplantación explícita de una persona real
    # generación de credenciales de acceso
    # documento oficial falso
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
