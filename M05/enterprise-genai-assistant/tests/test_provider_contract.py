from src.text_provider import GenerationResult, MockTextProvider


def test_mock_generation_contract():
    result = MockTextProvider().generate("hola", max_new_tokens=20)
    assert isinstance(result, GenerationResult)
    assert result.provider == "mock"
    assert result.input_tokens >= 1
    assert result.output_tokens >= 1
