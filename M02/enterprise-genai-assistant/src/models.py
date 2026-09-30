from enum import Enum
from typing import Literal
from pydantic import BaseModel, Field

class Confidentiality(str, Enum):
    PUBLIC="PUBLIC"
    INTERNAL="INTERNAL"
    CONFIDENTIAL="CONFIDENTIAL"
    RESTRICTED="RESTRICTED"

class DraftRequest(BaseModel):
    task: str = Field(min_length=3, max_length=4000)
    audience: str = Field(default="professional", min_length=2, max_length=120)
    channel: str = "web"
    business_unit: str = "Corporate"
    language: str = "es"
    urgency: str = "medium"
    confidentiality: Confidentiality = Confidentiality.INTERNAL
    requires_authoritative_sources: bool = False

class RoutingMetadata(BaseModel):
    intent: str
    confidence: float
    route: str
    model_version: str

class DraftResponse(BaseModel):
    status: Literal["ok","blocked","review"]
    content: str | None = None
    warnings: list[str] = []
    routing: RoutingMetadata
    request_id: str
    latency_ms: int
