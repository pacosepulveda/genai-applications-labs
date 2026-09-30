from dataclasses import dataclass

@dataclass
class VisualPolicyDecision:
    allowed: bool
    reason: str | None = None

BLOCKED_PATTERNS = [
    # TODO M04.P06: añade las reglas simplificadas indicadas por el instructor.
]

def evaluate_visual_prompt(prompt: str) -> VisualPolicyDecision:
    if not prompt.strip():
        return VisualPolicyDecision(False, "empty_prompt")

    lower = prompt.lower()
    for pattern in BLOCKED_PATTERNS:
        if pattern in lower:
            return VisualPolicyDecision(False, "visual_policy")

    return VisualPolicyDecision(True)
