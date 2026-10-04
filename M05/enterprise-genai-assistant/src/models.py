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


class TextTask(str, Enum):
    GENERATE = "GENERATE"
    SUMMARIZE = "SUMMARIZE"
    TRANSLATE = "TRANSLATE"


class TextRequest(BaseModel):
    task: TextTask
    text: str = Field(min_length=1)
    provider: str | None = None
    target_language: str | None = None
    max_new_tokens: int = Field(default=120, ge=1, le=512)


class TextResponse(BaseModel):
    output: str
    provider: str
    model: str
    task: str
    input_tokens: int
    output_tokens: int
    finish_reason: str
    request_id: str
    latency_ms: int


class ChatRequest(BaseModel):
    conversation_id: str
    message: str = Field(min_length=1)
    provider: str | None = None
    max_new_tokens: int = Field(default=120, ge=1, le=512)


class ChatResponse(BaseModel):
    conversation_id: str
    answer: str
    provider: str
    model: str
    input_tokens: int
    output_tokens: int
    finish_reason: str
    history_truncated: bool
    request_id: str
    latency_ms: int
