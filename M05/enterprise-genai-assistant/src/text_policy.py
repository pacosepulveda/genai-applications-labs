from dataclasses import dataclass

@dataclass
class TextPolicyDecision:
    allowed: bool
    reason: str | None = None

def evaluate_text(text: str, max_chars: int) -> TextPolicyDecision:
    if not text.strip():
        return TextPolicyDecision(False, "empty_input")

    if len(text) > max_chars:
        return TextPolicyDecision(False, "input_too_large")

    # Política simplificada de laboratorio:
    if "CONFIDENTIAL:" in text or "RESTRICTED:" in text:
        return TextPolicyDecision(False, "data_classification")

    return TextPolicyDecision(True)
