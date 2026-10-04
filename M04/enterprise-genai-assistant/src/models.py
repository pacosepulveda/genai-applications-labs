from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field


class Confidentiality(str, Enum):
    PUBLIC = "PUBLIC"
    INTERNAL = "INTERNAL"
    CONFIDENTIAL = "CONFIDENTIAL"
    RESTRICTED = "RESTRICTED"


class DraftRequest(BaseModel):
    task: str = Field(min_length=3, max_length=4000)
    audience: str = "professional"
    channel: str = "web"
    business_unit: str = "Corporate"
    language: str = "es"
    urgency: str = "medium"
    confidentiality: Confidentiality = Confidentiality.INTERNAL
    requires_authoritative_sources: bool = False


class RoutingMetadata(BaseModel):
    backend: str
    intent: str
    confidence: float
    route: str
    model_version: str


class DraftResponse(BaseModel):
    status: Literal["ok", "blocked", "review"]
    content: str | None = None
    warnings: list[str] = []
    routing: RoutingMetadata
    request_id: str
    latency_ms: int


class ImageGenerationRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=10000)
    provider: str | None = None
    seed: int = Field(default=42, ge=0, le=4294967294)


class ImageGenerationResponse(BaseModel):
    artifact_id: str
    provider: str
    model_version: str
    seed: int
    width: int
    height: int
    image_url: str
    metadata_url: str
