import pytest
from fastapi import HTTPException
import src.main as main_module
from src.models import TextRequest, TextTask, ChatRequest


def test_text_mock():
    r = main_module.text(TextRequest(task=TextTask.SUMMARIZE, text="El servicio estuvo degradado.", provider="mock", max_new_tokens=40))
    assert r.provider == "mock"
    assert r.task == "SUMMARIZE"
    assert r.output
    assert r.request_id


def test_translate_requires_language():
    with pytest.raises(HTTPException) as exc:
        main_module.text(TextRequest(task=TextTask.TRANSLATE, text="Hola", provider="mock"))
    assert exc.value.detail == "target_language_required"


def test_output_cap(monkeypatch):
    class Capture:
        received = None
        def generate(self, prompt, max_new_tokens):
            from src.text_provider import GenerationResult
            self.received = max_new_tokens
            return GenerationResult("ok", "capture", "v1", 1, 1)
    c = Capture()
    monkeypatch.setattr(main_module, "text_provider_for", lambda name: c)
    monkeypatch.setattr(main_module.settings, "max_new_tokens", 32)
    main_module.text(TextRequest(task=TextTask.GENERATE, text="hola", provider="mock", max_new_tokens=120))
    assert c.received == 32


def test_chat_mock_keeps_history(monkeypatch):
    from src.conversation_store import ConversationStore
    monkeypatch.setattr(main_module, "conversations", ConversationStore(max_messages=4))
    r1 = main_module.chat(ChatRequest(conversation_id="c1", message="hola", provider="mock"))
    r2 = main_module.chat(ChatRequest(conversation_id="c1", message="segunda", provider="mock"))
    assert r1.answer
    assert r2.answer
    history = main_module.conversations.get("c1")
    assert history[0]["role"] == "system"
    assert len(history) <= 4
