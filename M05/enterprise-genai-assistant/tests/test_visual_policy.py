from src.visual_policy import evaluate_visual_request


def test_empty_prompt_is_blocked():
    d = evaluate_visual_request("   ", "mock")
    assert d.allowed is False
    assert d.reason == "empty_prompt"


def test_unknown_provider_is_blocked():
    d = evaluate_visual_request("a blue robot", "unknown")
    assert d.allowed is False
    assert d.reason == "unknown_provider"


def test_normal_prompt_is_allowed():
    d = evaluate_visual_request(
        "a blue robot on white background",
        "mock",
    )
    assert d.allowed is True


def test_impersonation_is_blocked():
    d = evaluate_visual_request(
        "suplanta a una persona real en una fotografía",
        "mock",
    )
    assert d.allowed is False
    assert d.reason == "visual_policy"
