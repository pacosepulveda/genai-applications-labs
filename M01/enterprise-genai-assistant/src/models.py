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
    audience: str = Field(default="professional", min_length=2, max_length=120)
    confidentiality: Confidentiality = Confidentiality.INTERNAL
    requires_authoritative_sources: bool = False

class ResponseMetadata(BaseModel):
    request_id: str
    provider: str
    model: str
    latency_ms: int

class DraftResponse(BaseModel):
    status: Literal["ok", "blocked"]
    content: str | None = None
    warnings: list[str] = []
    metadata: ResponseMetadata

class HealthResponse(BaseModel):
    status: Literal["ok"] = "ok"
    provider: str
