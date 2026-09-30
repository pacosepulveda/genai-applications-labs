import time
import uuid
from fastapi import FastAPI, HTTPException

from .models import AskRequest, AskResponse, OperationsRequest, OperationsResponse
from .policy import choose_mode
from .settings import settings

app = FastAPI(title="Enterprise GenAI Assistant", version="0.6.0-m06")

@app.get("/health")
def health():
    return {
        "status": "ok",
        "version": "0.6.0-m06",
        "ai_runtime": settings.ai_runtime,
    }

@app.post("/v1/ask", response_model=AskResponse)
def ask(req: AskRequest):
    request_id = uuid.uuid4().hex
    route = choose_mode(req)

    if route.mode == "RAG":
        # TODO M06.P06:
        # RAG obligatorio. No fallback directo si falla/no hay evidencia.
        raise NotImplementedError

    # TODO M06.P06:
    # flujo DIRECT para casos que no exigen fuente autoritativa
    raise NotImplementedError

@app.post("/v1/operations", response_model=OperationsResponse)
def operations(req: OperationsRequest):
    # TODO M06.P06:
    # AgentService con conversation_id -> thread_id
    raise NotImplementedError
