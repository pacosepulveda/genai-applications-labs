from fastapi import FastAPI, HTTPException

from .conversation_store import ConversationStore
from .models import TextRequest, TextResponse, ChatRequest, ChatResponse
from .settings import settings
from .text_policy import evaluate_text
from .text_provider import build_text_provider

app = FastAPI(title="Enterprise GenAI Assistant", version="0.5.0-m05")

conversations = ConversationStore(settings.max_history_messages)

@app.get("/health")
def health():
    return {"status":"ok","nlp":True}

def provider_for(name: str | None):
    selected = name or settings.text_provider
    try:
        return build_text_provider(
            selected,
            settings.seq2seq_model_id,
            settings.chat_model_id,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

@app.post("/v1/text", response_model=TextResponse)
def text(req: TextRequest):
    policy = evaluate_text(req.text, settings.max_input_chars)
    if not policy.allowed:
        raise HTTPException(status_code=400, detail=policy.reason)

    provider = provider_for(req.provider)

    # TODO M05.P06:
    # construye prompt según task:
    # SUMMARIZE / TRANSLATE / GENERATE
    # llama provider.generate(...)
    # devuelve TextResponse
    raise NotImplementedError

@app.post("/v1/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    policy = evaluate_text(req.message, settings.max_input_chars)
    if not policy.allowed:
        raise HTTPException(status_code=400, detail=policy.reason)

    provider = provider_for(req.provider)

    conversations.append(req.conversation_id, "user", req.message)
    truncated = conversations.compact(req.conversation_id)
    history = conversations.get(req.conversation_id)

    # TODO M05.P06:
    # result = provider.chat(history,...)
    # añade assistant al historial
    # compact de nuevo
    # devuelve ChatResponse
    raise NotImplementedError
