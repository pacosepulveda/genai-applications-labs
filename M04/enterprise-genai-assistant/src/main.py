from datetime import datetime, timezone
from pathlib import Path
import uuid

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

from .models import ImageGenerationRequest, ImageGenerationResponse
from .visual_policy import evaluate_visual_prompt
from .visual_provider import build_visual_provider
from .storage import ArtifactStore

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
GENERATED = ROOT / "generated"

app = FastAPI(title="Enterprise GenAI Assistant", version="0.4.0-m04")
store = ArtifactStore(GENERATED)
app.mount("/generated", StaticFiles(directory=GENERATED), name="generated")

@app.get("/health")
def health():
    return {"status":"ok","visual":True}

@app.post("/v1/images", response_model=ImageGenerationResponse)
def generate_image(req: ImageGenerationRequest):
    policy = evaluate_visual_prompt(req.prompt)
    if not policy.allowed:
        raise HTTPException(status_code=400, detail=policy.reason)

    # TODO M04.P06:
    # provider_name = req.provider or ...
    # provider = build_visual_provider(...)
    # result = provider.generate(...)
    # crear artifact_id
    # guardar imagen + metadata
    # devolver URLs
    raise NotImplementedError

@app.get("/v1/images/{artifact_id}")
def image_metadata(artifact_id: str):
    try:
        return store.load_metadata(artifact_id)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="artifact_not_found")
