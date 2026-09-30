from src.text_policy import evaluate_text

def test_normal_text_allowed():
    assert evaluate_text("hola", 100).allowed is True

def test_large_text_blocked():
    assert evaluate_text("x"*101, 100).allowed is False

def test_confidential_blocked():
    assert evaluate_text("CONFIDENTIAL: secreto", 1000).allowed is False
