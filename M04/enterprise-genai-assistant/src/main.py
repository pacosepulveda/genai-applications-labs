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
provider = MockProvider()
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

    current_router = get_router()

    # TODO heredado de M03.P06:
    # conserva tu implementación completada de routing y generación textual.
    # El nuevo servicio visual no debe alterar estas políticas.
    raise NotImplementedError


@app.post("/v1/images", response_model=ImageGenerationResponse)
def generate_image(req: ImageGenerationRequest):
    provider_name = req.provider or settings.visual_provider

    policy = evaluate_visual_request(req.prompt, provider_name)
    if not policy.allowed:
        raise HTTPException(status_code=400, detail=policy.reason)

    # TODO M04.P06:
    # visual_provider = build_visual_provider(
    #     provider_name,
    #     ARTIFACTS,
    #     settings.bedrock_image_region,
    #     settings.bedrock_image_model_id,
    # )
    # result = visual_provider.generate(req.prompt, req.seed)
    # artifact_id = str(uuid.uuid4())
    # metadata = {
    #     "artifact_id": artifact_id,
    #     "provider": result.provider,
    #     "model_version": result.model_version,
    #     "seed": req.seed,
    #     "width": result.image.width,
    #     "height": result.image.height,
    #     "created_at": datetime.now(timezone.utc).isoformat(),
    # }
    # store.save(artifact_id, result.image, metadata)
    # return ImageGenerationResponse(...)
    raise NotImplementedError


@app.get("/v1/images/{artifact_id}")
def image_metadata(artifact_id: str):
    try:
        return store.load_metadata(artifact_id)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="artifact_not_found")
