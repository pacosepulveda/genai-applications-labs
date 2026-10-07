from datetime import datetime, timezone
from pathlib import Path
import time
import uuid

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

from .models import (
    DraftRequest,
    DraftResponse,
    RoutingMetadata,
    ImageGenerationRequest,
    ImageGenerationResponse,
)
from .policy import evaluate_request
from .provider import MockProvider
from .routers import build_router
from .settings import settings
from .storage import ArtifactStore
from .visual_policy import evaluate_visual_request
from .visual_provider import build_visual_provider

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
GENERATED = ROOT / "generated"

app = FastAPI(title="Enterprise GenAI Assistant", version="0.4.0-m04")
store = ArtifactStore(GENERATED)
text_provider = MockProvider()
router = None

app.mount("/generated", StaticFiles(directory=GENERATED), name="generated")


def get_router():
    global router
    if router is None:
        router = build_router(settings.router_backend, ARTIFACTS)
    return router


@app.get("/health")
def health():
    return {
        "status": "ok",
        "router_backend": settings.router_backend,
        "router_loaded": router is not None,
        "router_model_version": settings.router_model_version,
        "visual": True,
        "visual_provider": settings.visual_provider,
    }


@app.post("/v1/draft", response_model=DraftResponse)
def draft(req: DraftRequest):
    started = time.perf_counter()
    request_id = str(uuid.uuid4())
    policy = evaluate_request(req)

    if not policy.allowed:
        return DraftResponse(
            status="blocked",
            content=None,
            warnings=[f"Bloqueado: {policy.reason}"],
            routing=RoutingMetadata(
                backend=settings.router_backend,
                intent="NOT_EVALUATED",
                confidence=0.0,
                route="BLOCK",
                model_version=settings.router_model_version,
            ),
            request_id=request_id,
            latency_ms=int((time.perf_counter() - started) * 1000),
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
            status="blocked",
            content=None,
            warnings=policy.warnings + ["La intención no permite generación directa."],
            routing=routing,
            request_id=request_id,
            latency_ms=int((time.perf_counter() - started) * 1000),
        )

    if route in {"REVIEW", "CONTROLLED_KNOWLEDGE_FLOW"}:
        return DraftResponse(
            status="review",
            content=None,
            warnings=policy.warnings + [f"Ruta controlada: {route}"],
            routing=routing,
            request_id=request_id,
            latency_ms=int((time.perf_counter() - started) * 1000),
        )

    return DraftResponse(
        status="ok",
        content=text_provider.generate(req.task),
        warnings=policy.warnings,
        routing=routing,
        request_id=request_id,
        latency_ms=int((time.perf_counter() - started) * 1000),
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
