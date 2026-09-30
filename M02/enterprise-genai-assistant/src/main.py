from pathlib import Path
import time
import uuid
from fastapi import FastAPI

from .models import DraftRequest, DraftResponse, RoutingMetadata
from .policy import evaluate_request
from .intent_router import IntentRouter
from .provider import MockProvider
from .settings import settings

app = FastAPI(title="Enterprise GenAI Assistant", version="0.2.0-m02")
ARTIFACT = Path(__file__).resolve().parents[1] / "artifacts" / "intent_router.joblib"
router = IntentRouter(ARTIFACT)
provider = MockProvider()

@app.on_event("startup")
def startup():
    if ARTIFACT.exists():
        router.load()

@app.get("/health")
def health():
    return {
        "status":"ok",
        "router_loaded": router.pipeline is not None,
        "model_version": settings.router_model_version,
    }

@app.post("/v1/draft", response_model=DraftResponse)
def draft(req: DraftRequest):
    started = time.perf_counter()
    request_id = str(uuid.uuid4())

    policy = evaluate_request(req)
    if not policy.allowed:
        latency = int((time.perf_counter()-started)*1000)
        return DraftResponse(
            status="blocked",
            content=None,
            warnings=[f"Bloqueado: {policy.reason}"],
            routing=RoutingMetadata(
                intent="NOT_EVALUATED",
                confidence=0.0,
                route="BLOCK",
                model_version=settings.router_model_version,
            ),
            request_id=request_id,
            latency_ms=latency,
        )

    # TODO M02.P05
    # 1. Ejecuta router.predict(...)
    # 2. Aplica la política de routing:
    #    - confidence < threshold -> REVIEW
    #    - CORPORATE_KNOWLEDGE -> CONTROLLED_KNOWLEDGE_FLOW
    #    - UNSUPPORTED -> BLOCK
    #    - resto -> GENERATION
    # 3. Solo llama al provider en GENERATION.
    raise NotImplementedError
