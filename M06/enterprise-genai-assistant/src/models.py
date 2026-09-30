from enum import Enum
from pydantic import BaseModel, Field

class AskTask(str, Enum):
    DIRECT = "DIRECT"
    CORPORATE_KNOWLEDGE = "CORPORATE_KNOWLEDGE"

class AskRequest(BaseModel):
    question: str = Field(min_length=1, max_length=12000)
    task: AskTask = AskTask.DIRECT
    requires_authoritative_sources: bool = False

class AskResponse(BaseModel):
    mode: str
    answer: str
    source_ids: list[str] = []
    insufficient_evidence: bool = False
    request_id: str
    citation_validation: bool | None = None

class OperationsRequest(BaseModel):
    conversation_id: str = Field(min_length=1)
    message: str = Field(min_length=1, max_length=12000)

class OperationsResponse(BaseModel):
    conversation_id: str
    answer: str
    mode: str = "AGENT"
