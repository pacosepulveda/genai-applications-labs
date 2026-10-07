import pytest
import src.text_provider as provider_module
from src.text_provider import MockTextProvider, BedrockLunaProvider, build_text_provider

class StubBedrockClient:
    def converse(self, **kwargs):
        return {
            "output": {"message": {"role": "assistant", "content": [{"text": "respuesta de prueba"}]}},
            "usage": {"inputTokens": 5, "outputTokens": 3, "totalTokens": 8},
            "stopReason": "end_turn",
        }

def test_build_mock():
    p = build_text_provider("mock", "unused", "unused", "us-east-1", "test-model")
    assert isinstance(p, MockTextProvider)

def test_unknown_provider():
    with pytest.raises(ValueError):
        build_text_provider("unknown", "unused", "unused", "us-east-1", "test-model")

def test_bedrock_stub(monkeypatch):
    monkeypatch.setattr(provider_module.boto3, "client", lambda *a, **k: StubBedrockClient())
    p = BedrockLunaProvider("us-east-1", "test-model")
    r = p.generate("hola", 40)
    assert r.text == "respuesta de prueba"
    assert r.input_tokens == 5
    assert r.output_tokens == 3
    assert r.finish_reason == "end_turn"
