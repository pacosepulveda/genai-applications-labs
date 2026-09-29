import logging
import time
import uuid
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from .models import DraftRequest, DraftResponse, HealthResponse, ResponseMetadata
from .policy import evaluate_request
from .prompts import build_user_prompt
from .providers.factory import get_provider
from .settings import settings

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("enterprise_genai_assistant")
app = FastAPI(title="Enterprise GenAI Assistant", version="0.1.0-m01")

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

@app.get("/health", response_model=HealthResponse)
def health():
    return HealthResponse(provider=settings.provider)

@app.post("/v1/draft", response_model=DraftResponse)
def draft(req: DraftRequest):
    started = time.perf_counter()
    request_id = str(uuid.uuid4())
    decision = evaluate_request(req)

    if not decision.allowed:
        latency = int((time.perf_counter() - started) * 1000)
        log.info("request_id=%s status=blocked reason=%s", request_id, decision.reason)
        return DraftResponse(
            status="blocked",
            content=None,
            warnings=[f"Petición bloqueada: {decision.reason}"],
            metadata=ResponseMetadata(
                request_id=request_id,
                provider="none",
                model="none",
                latency_ms=latency,
            ),
        )

    provider = get_provider()
    prompt = build_user_prompt(req.task, req.audience)
    result = provider.generate(prompt)
    latency = int((time.perf_counter() - started) * 1000)

    # Por defecto registramos metadatos, no el prompt completo.
    if settings.log_prompts:
        log.warning("LOG_PROMPTS=true: request_id=%s prompt=%r", request_id, prompt)
    else:
        log.info("request_id=%s status=ok provider=%s model=%s", request_id, result.provider, result.model)

    return DraftResponse(
        status="ok",
        content=result.text,
        warnings=decision.warnings,
        metadata=ResponseMetadata(
            request_id=request_id,
            provider=result.provider,
            model=result.model,
            latency_ms=latency,
        ),
    )
