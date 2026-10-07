from src.visual_policy import evaluate_visual_request


def test_empty_prompt_is_blocked():
    decision = evaluate_visual_request("   ", "mock")
    assert decision.allowed is False
    assert decision.reason == "empty_prompt"


def test_unknown_provider_is_blocked():
    decision = evaluate_visual_request("a blue robot", "unknown")
    assert decision.allowed is False
    assert decision.reason == "unknown_provider"


def test_normal_prompt_is_allowed():
    decision = evaluate_visual_request("a blue robot on white background", "mock")
    assert decision.allowed is True
