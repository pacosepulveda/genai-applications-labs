from src.routers import IntentPrediction


def test_prediction_contract():
    p = IntentPrediction(intent="DRAFT", confidence=0.9)
    assert p.intent == "DRAFT"
    assert 0 <= p.confidence <= 1
