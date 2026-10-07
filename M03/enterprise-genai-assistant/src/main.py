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
        "status": "ok",
        "router_backend": settings.router_backend,
        "router_loaded": router is not None,
        "model_version": settings.router_model_version,
    }


def _metadata(prediction, route: str) -> RoutingMetadata:
    return RoutingMetadata(
        backend=settings.router_backend,
        intent=prediction.intent,
        confidence=prediction.confidence,
        route=route,
        model_version=settings.router_model_version,
    )


@app.post("/v1/draft", response_model=DraftResponse)
def draft(req: DraftRequest):
    started = time.perf_counter()
    request_id = str(uuid.uuid4())

    policy = evaluate_request(req)

    # La política determinista se ejecuta ANTES del router aprendido.
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

    prediction = router.predict(
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

    if route == "BLOCK":
        return DraftResponse(
            status="blocked",
            content=None,
            warnings=policy.warnings + [
                "La intención clasificada no permite generación directa."
            ],
            routing=_metadata(prediction, route),
            request_id=request_id,
            latency_ms=int((time.perf_counter() - started) * 1000),
        )

    if route in {"REVIEW", "CONTROLLED_KNOWLEDGE_FLOW"}:
        warning = (
            "La petición requiere revisión por baja confianza."
            if route == "REVIEW"
            else "La petición requiere un flujo controlado con fuentes autoritativas."
        )
        return DraftResponse(
            status="review",
            content=None,
            warnings=policy.warnings + [warning],
            routing=_metadata(prediction, route),
            request_id=request_id,
            latency_ms=int((time.perf_counter() - started) * 1000),
        )

    content = provider.generate(req.task)

    return DraftResponse(
        status="ok",
        content=content,
        warnings=policy.warnings,
        routing=_metadata(prediction, route),
        request_id=request_id,
        latency_ms=int((time.perf_counter() - started) * 1000),
    )
