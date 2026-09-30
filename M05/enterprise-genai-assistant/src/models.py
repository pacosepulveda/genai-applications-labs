from enum import Enum
from pydantic import BaseModel, Field

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
    history_truncated: bool
