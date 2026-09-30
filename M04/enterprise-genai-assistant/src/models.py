from pydantic import BaseModel, Field

class ImageGenerationRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=1000)
    provider: str | None = None
    seed: int = 42

class ImageGenerationResponse(BaseModel):
    artifact_id: str
    provider: str
    model_version: str
    seed: int
    width: int
    height: int
    image_url: str
    metadata_url: str
