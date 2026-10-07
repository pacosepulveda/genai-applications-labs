import pytest

import src.text_provider as provider_module
from src.text_provider import (
    BedrockLunaProvider,
    GenerationResult,
    MockTextProvider,
    build_text_provider,
)


def test_mock_generation_contract():
    result = MockTextProvider().generate("hola", max_new_tokens=20)
    assert isinstance(result, GenerationResult)
    assert result.provider == "mock"
    assert result.input_tokens >= 1
    assert result.output_tokens >= 1


def test_build_mock():
    provider = build_text_provider(
        "mock",
        "us-east-1",
        "us.openai.gpt-5.6-luna",
    )
    assert isinstance(provider, MockTextProvider)


def test_unknown_provider():
    with pytest.raises(ValueError):
        build_text_provider(
            "unknown",
            "us-east-1",
            "us.openai.gpt-5.6-luna",
        )


class StubBedrockClient:
    def converse(self, **kwargs):
        assert kwargs["modelId"] == "test-model"
        assert kwargs["inferenceConfig"]["maxTokens"] == 40
        return {
            "output": {
                "message": {
                    "role": "assistant",
                    "content": [{"text": "respuesta de prueba"}],
                }
            },
            "usage": {
                "inputTokens": 5,
                "outputTokens": 3,
                "totalTokens": 8,
            },
            "stopReason": "end_turn",
        }


def test_bedrock_provider_with_stub(monkeypatch):
    monkeypatch.setattr(
        provider_module.boto3,
        "client",
        lambda *args, **kwargs: StubBedrockClient(),
    )

    provider = BedrockLunaProvider("us-east-1", "test-model")
    result = provider.generate("hola", max_new_tokens=40)

    assert result.text == "respuesta de prueba"
    assert result.provider == "bedrock_luna"
    assert result.model == "test-model"
    assert result.input_tokens == 5
    assert result.output_tokens == 3
    assert result.finish_reason == "end_turn"
