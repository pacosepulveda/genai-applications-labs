from pathlib import Path
import time, uuid
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from .conversation_store import ConversationStore
from .models import DraftRequest,DraftResponse,ImageGenerationRequest,ImageGenerationResponse,TextRequest,TextResponse,ChatRequest,ChatResponse,AskRequest,AskResponse,OperationsRequest,OperationsResponse
from .settings import settings
from .storage import ArtifactStore
from .policy import choose_mode

ROOT=Path(__file__).resolve().parents[1]
ARTIFACTS=ROOT/"artifacts"
GENERATED=ROOT/"generated"
app=FastAPI(title="Enterprise GenAI Assistant",version="0.6.0-m06")
store=ArtifactStore(GENERATED)
conversations=ConversationStore(settings.max_history_messages)
app.mount("/generated",StaticFiles(directory=GENERATED),name="generated")

@app.get("/health")
def health():
    return {"status":"ok","version":"0.6","model_provider":settings.model_provider,"model_id":settings.model_id,"model_region":settings.model_region,"text_provider":settings.text_provider,"visual_provider":settings.visual_provider,"rag":True,"agent":True}

# Capacidades heredadas: conserva aquí las implementaciones completadas en v0.5.
@app.post("/v1/draft",response_model=DraftResponse)
def draft(req:DraftRequest): raise NotImplementedError

@app.post("/v1/images",response_model=ImageGenerationResponse)
def generate_image(req:ImageGenerationRequest): raise NotImplementedError

@app.get("/v1/images/{artifact_id}")
def image_metadata(artifact_id:str):
    try: return store.load_metadata(artifact_id)
    except FileNotFoundError: raise HTTPException(status_code=404,detail="artifact_not_found")

@app.post("/v1/text",response_model=TextResponse)
def text(req:TextRequest): raise NotImplementedError

@app.post("/v1/chat",response_model=ChatResponse)
def chat(req:ChatRequest): raise NotImplementedError

# Nuevas capacidades M06.
@app.post("/v1/ask",response_model=AskResponse)
def ask(req:AskRequest):
    started=time.perf_counter(); request_id=uuid.uuid4().hex; route=choose_mode(req)
    if route.mode=="RAG":
        # TODO: RAG obligatorio; nunca fallback DIRECT ante NO_EVIDENCE.
        raise NotImplementedError
    # TODO: DIRECT reutiliza TextModelProvider/bedrock_luna de v0.5.
    raise NotImplementedError

@app.post("/v1/operations",response_model=OperationsResponse)
def operations(req:OperationsRequest):
    # TODO: AgentService; conversation_id -> thread_id.
    raise NotImplementedError
