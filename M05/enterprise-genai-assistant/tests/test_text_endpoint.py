import pytest
from fastapi import HTTPException

import src.main as main_module
from src.models import TextRequest, TextTask


def test_text_endpoint_with_mock():
    response = main_module.text(
        TextRequest(
            task=TextTask.SUMMARIZE,
            text="El servicio estuvo degradado durante diez minutos.",
            provider="mock",
            max_new_tokens=50,
        )
    )

    assert response.provider == "mock"
    assert response.task == "SUMMARIZE"
    assert response.output
    assert response.request_id
    assert response.latency_ms >= 0


def test_translate_requires_target_language():
    with pytest.raises(HTTPException) as exc:
        main_module.text(
            TextRequest(
                task=TextTask.TRANSLATE,
                text="El servicio está disponible.",
                provider="mock",
            )
        )

    assert exc.value.status_code == 400


def test_input_limit(monkeypatch):
    monkeypatch.setattr(main_module.settings, "max_input_chars", 5)

    with pytest.raises(HTTPException) as exc:
        main_module.text(
            TextRequest(
                task=TextTask.GENERATE,
                text="texto demasiado largo",
                provider="mock",
            )
        )

    assert exc.value.detail == "input_too_large"


def test_output_limit_is_capped(monkeypatch):
    class CaptureProvider:
        def __init__(self):
            self.received = None

        def generate(self, prompt, max_new_tokens):
            from src.text_provider import GenerationResult
            self.received = max_new_tokens
            return GenerationResult(
                text="ok",
                provider="capture",
                model="capture-v1",
                input_tokens=1,
                output_tokens=1,
                finish_reason="stop",
            )

    capture = CaptureProvider()
    monkeypatch.setattr(main_module, "text_provider_for", lambda name: capture)
    monkeypatch.setattr(main_module.settings, "max_new_tokens", 32)

    main_module.text(
        TextRequest(
            task=TextTask.GENERATE,
            text="hola",
            provider="mock",
            max_new_tokens=120,
        )
    )

    assert capture.received == 32
