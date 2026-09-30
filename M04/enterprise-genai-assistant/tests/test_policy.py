from src.visual_policy import evaluate_visual_prompt

def test_normal_prompt_allowed():
    assert evaluate_visual_prompt("synthetic digit").allowed is True
