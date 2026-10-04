from pathlib import Path
import time
import uuid
from fastapi import FastAPI

from .models import DraftRequest, DraftResponse, RoutingMetadata
from .policy import evaluate_request
from .provider import MockProvider
from .routers import build_router
from .settings import settings

app = FastAPI(title="Enterprise GenAI Assistant", version="0.3.0-m03")
ARTIFACTS = Path(__file__).resolve().parents[1] / "artifacts"
router = None
provider = MockProvider()

@app.on_event("startup")
def startup():
    global router
    router = build_router(settings.router_backend, ARTIFACTS)

@app.get("/health")
def health():
    return {
        "status":"ok",
        "router_backend":settings.router_backend,
        "router_loaded":router is not None,
        "model_version":settings.router_model_version,
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
            latency_ms=int((time.perf_counter()-started)*1000),
        )

    # TODO M03.P06:
    # 1. prediction = router.predict(...)
    # 2. Aplica la política de routing sin permitir que ML anule la seguridad:
    #    - requires_authoritative_sources=True -> CONTROLLED_KNOWLEDGE_FLOW
    #    - confidence < threshold -> REVIEW
    #    - CORPORATE_KNOWLEDGE -> CONTROLLED_KNOWLEDGE_FLOW
    #    - UNSUPPORTED -> BLOCK
    #    - resto -> GENERATION
    # 3. Solo llama al provider en GENERATION.
    raise NotImplementedError
