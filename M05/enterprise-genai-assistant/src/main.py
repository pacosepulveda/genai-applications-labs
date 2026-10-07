from datetime import datetime, timezone
from pathlib import Path
import time
import uuid
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

from .conversation_store import ConversationStore
from .models import (
    DraftRequest, DraftResponse, RoutingMetadata,
    ImageGenerationRequest, ImageGenerationResponse,
    TextRequest, TextResponse, TextTask, ChatRequest, ChatResponse,
)
from .policy import evaluate_request
from .provider import MockProvider
from .routers import build_router
from .settings import settings
from .storage import ArtifactStore
from .text_policy import evaluate_text
from .text_provider import build_text_provider
from .visual_policy import evaluate_visual_request
from .visual_provider import build_visual_provider

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
GENERATED = ROOT / "generated"
app = FastAPI(title="Enterprise GenAI Assistant", version="0.5.0-m05")
store = ArtifactStore(GENERATED)
draft_provider = MockProvider()
router = None
conversations = ConversationStore(settings.max_history_messages)
app.mount("/generated", StaticFiles(directory=GENERATED), name="generated")

def get_router():
    global router
    if router is None:
        router = build_router(settings.router_backend, ARTIFACTS)
    return router

def text_provider_for(name: str | None):
    selected = name or settings.text_provider
    try:
        return build_text_provider(
            selected,
            settings.seq2seq_model_id,
            settings.chat_model_id,
            settings.bedrock_text_region,
            settings.bedrock_text_model_id,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

@app.get("/health")
def health():
    return {
        "status": "ok",
        "version": "0.5",
        "router_backend": settings.router_backend,
        "visual_provider": settings.visual_provider,
        "text_provider": settings.text_provider,
        "nlp": True,
        "visual": True,
    }

@app.post("/v1/draft", response_model=DraftResponse)
def draft(req: DraftRequest):
    started = time.perf_counter()
    request_id = str(uuid.uuid4())
    policy = evaluate_request(req)
    if not policy.allowed:
        return DraftResponse(
            status="blocked", content=None,
            warnings=[f"Bloqueado: {policy.reason}"],
            routing=RoutingMetadata(
                backend=settings.router_backend,
                intent="NOT_EVALUATED", confidence=0.0,
                route="BLOCK", model_version=settings.router_model_version,
            ),
            request_id=request_id,
            latency_ms=int((time.perf_counter()-started)*1000),
        )
    prediction = get_router().predict(
        request_text=req.task,
        channel=req.channel,
        business_unit=req.business_unit,
        language=req.language,
        urgency=req.urgency,
        requires_authoritative_sources=req.requires_authoritative_sources,
    )
    if req.requires_authoritative_sources:
        route = "CONTROLLED_KNOWLEDGE_FLOW"
    elif prediction.confidence < settings.router_threshold:
        route = "REVIEW"
    elif prediction.intent == "CORPORATE_KNOWLEDGE":
        route = "CONTROLLED_KNOWLEDGE_FLOW"
    elif prediction.intent == "UNSUPPORTED":
        route = "BLOCK"
    else:
        route = "GENERATION"
    routing = RoutingMetadata(
        backend=settings.router_backend,
        intent=prediction.intent,
        confidence=prediction.confidence,
        route=route,
        model_version=settings.router_model_version,
    )
    if route == "BLOCK":
        return DraftResponse(
            status="blocked", content=None,
            warnings=policy.warnings + ["La intención no permite generación directa."],
            routing=routing, request_id=request_id,
            latency_ms=int((time.perf_counter()-started)*1000),
        )
    if route in {"REVIEW", "CONTROLLED_KNOWLEDGE_FLOW"}:
        return DraftResponse(
            status="review", content=None,
            warnings=policy.warnings + [f"Ruta controlada: {route}"],
            routing=routing, request_id=request_id,
            latency_ms=int((time.perf_counter()-started)*1000),
        )
    return DraftResponse(
        status="ok",
        content=draft_provider.generate(req.task),
        warnings=policy.warnings,
        routing=routing,
        request_id=request_id,
        latency_ms=int((time.perf_counter()-started)*1000),
    )

@app.post("/v1/images", response_model=ImageGenerationResponse)
def generate_image(req: ImageGenerationRequest):
    provider_name = req.provider or settings.visual_provider
    policy = evaluate_visual_request(req.prompt, provider_name)
    if not policy.allowed:
        raise HTTPException(status_code=400, detail=policy.reason)
    visual_provider = build_visual_provider(
        provider_name,
        settings.bedrock_image_region,
        settings.bedrock_image_model_id,
    )
    result = visual_provider.generate(req.prompt, req.seed)
    artifact_id = str(uuid.uuid4())
    metadata = {
        "artifact_id": artifact_id,
        "provider": result.provider,
        "model_version": result.model_version,
        "seed": req.seed,
        "width": result.image.width,
        "height": result.image.height,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    store.save(artifact_id, result.image, metadata)
    return ImageGenerationResponse(
        artifact_id=artifact_id,
        provider=result.provider,
        model_version=result.model_version,
        seed=req.seed,
        width=result.image.width,
        height=result.image.height,
        image_url=f"/generated/{artifact_id}.png",
        metadata_url=f"/v1/images/{artifact_id}",
    )

@app.get("/v1/images/{artifact_id}")
def image_metadata(artifact_id: str):
    try:
        return store.load_metadata(artifact_id)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="artifact_not_found")

def build_task_prompt(req: TextRequest):
    if req.task == TextTask.GENERATE:
        return req.text
    if req.task == TextTask.SUMMARIZE:
        return "Resume de forma fiel y concisa el siguiente texto:\n\n" + req.text
    if req.task == TextTask.TRANSLATE:
        if not req.target_language:
            raise HTTPException(status_code=400, detail="target_language_required")
        return (
            f"Traduce al idioma {req.target_language}. Conserva exactamente identificadores, "
            f"códigos, rutas y placeholders:\n\n{req.text}"
        )
    raise HTTPException(status_code=400, detail="unsupported_task")

@app.post("/v1/text", response_model=TextResponse)
def text(req: TextRequest):
    started = time.perf_counter()
    request_id = str(uuid.uuid4())
    policy = evaluate_text(req.text, settings.max_input_chars)
    if not policy.allowed:
        raise HTTPException(status_code=400, detail=policy.reason)
    provider = text_provider_for(req.provider)
    prompt = build_task_prompt(req)
    effective_max = min(req.max_new_tokens, settings.max_new_tokens)
    result = provider.generate(prompt, effective_max)
    return TextResponse(
        output=result.text,
        provider=result.provider,
        model=result.model,
        task=req.task.value,
        input_tokens=result.input_tokens,
        output_tokens=result.output_tokens,
        finish_reason=result.finish_reason,
        request_id=request_id,
        latency_ms=int((time.perf_counter()-started)*1000),
    )

@app.post("/v1/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    started = time.perf_counter()
    request_id = str(uuid.uuid4())
    policy = evaluate_text(req.message, settings.max_input_chars)
    if not policy.allowed:
        raise HTTPException(status_code=400, detail=policy.reason)
    provider = text_provider_for(req.provider)
    conversations.ensure_system(req.conversation_id, settings.chat_system_prompt)
    conversations.append(req.conversation_id, "user", req.message)
    truncated = conversations.compact(req.conversation_id)
    history = conversations.get(req.conversation_id)
    effective_max = min(req.max_new_tokens, settings.max_new_tokens)
    result = provider.chat(history, effective_max)
    conversations.append(req.conversation_id, "assistant", result.text)
    truncated = conversations.compact(req.conversation_id) or truncated
    return ChatResponse(
        conversation_id=req.conversation_id,
        answer=result.text,
        provider=result.provider,
        model=result.model,
        input_tokens=result.input_tokens,
        output_tokens=result.output_tokens,
        finish_reason=result.finish_reason,
        history_truncated=truncated,
        request_id=request_id,
        latency_ms=int((time.perf_counter()-started)*1000),
    )
