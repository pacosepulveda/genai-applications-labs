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
    TextRequest,
    TextResponse,
    ChatRequest,
)
from .policy import evaluate_request
from .provider import MockProvider
from .routers import build_router
from .settings import settings
from .storage import ArtifactStore
from .text_policy import evaluate_text
from .text_provider import build_text_provider
from .visual_policy import evaluate_visual_request


ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
GENERATED = ROOT / "generated"

app = FastAPI(title="Enterprise GenAI Assistant", version="0.5.0-m05")

store = ArtifactStore(GENERATED)
draft_provider = MockProvider()
router = None

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


# ---------------------------------------------------------------------
# Capacidades heredadas de módulos anteriores
# ---------------------------------------------------------------------

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

    # TODO heredado:
    # conserva tu implementación anterior si quieres utilizar este endpoint.
    raise NotImplementedError


@app.post("/v1/images", response_model=ImageGenerationResponse)
def generate_image(req: ImageGenerationRequest):
    provider_name = req.provider or settings.visual_provider

    policy = evaluate_visual_request(req.prompt, provider_name)
    if not policy.allowed:
        raise HTTPException(status_code=400, detail=policy.reason)

    # TODO heredado:
    # conserva tu implementación de M04 si quieres utilizar este endpoint.
    raise NotImplementedError


@app.get("/v1/images/{artifact_id}")
def image_metadata(artifact_id: str):
    try:
        return store.load_metadata(artifact_id)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="artifact_not_found")


# ---------------------------------------------------------------------
# Ruta principal M05
# ---------------------------------------------------------------------

@app.post("/v1/text", response_model=TextResponse)
def text(req: TextRequest):
    started = time.perf_counter()
    request_id = str(uuid.uuid4())

    policy = evaluate_text(req.text, settings.max_input_chars)
    if not policy.allowed:
        raise HTTPException(status_code=400, detail=policy.reason)

    provider = text_provider_for(req.provider)

    # TODO M05.P06:
    # 1. construye el prompt para GENERATE / SUMMARIZE / TRANSLATE;
    # 2. en TRANSLATE exige target_language;
    # 3. effective_max = min(req.max_new_tokens, settings.max_new_tokens);
    # 4. result = provider.generate(prompt, effective_max);
    # 5. devuelve TextResponse con request_id y latency_ms.
    raise NotImplementedError


# ---------------------------------------------------------------------
# Ampliación opcional
# ---------------------------------------------------------------------

@app.post("/v1/chat")
def chat(req: ChatRequest):
    raise HTTPException(
        status_code=501,
        detail="optional_extension_not_implemented",
    )
