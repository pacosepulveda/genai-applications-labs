from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT = Path(__file__).resolve().parents[1]

class Settings(BaseSettings):
    router_backend: str = Field(default="classic", validation_alias="ROUTER_BACKEND")
    router_threshold: float = Field(default=0.70, validation_alias="ROUTER_THRESHOLD")
    router_model_version: str = Field(default="m03", validation_alias="ROUTER_MODEL_VERSION")
    visual_provider: str = Field(default="mock", validation_alias="VISUAL_PROVIDER")
    bedrock_image_region: str = Field(default="us-west-2", validation_alias="BEDROCK_IMAGE_REGION")
    bedrock_image_model_id: str = Field(default="stability.sd3-5-large-v1:0", validation_alias="BEDROCK_IMAGE_MODEL_ID")
    text_provider: str = Field(default="bedrock_luna", validation_alias="TEXT_PROVIDER")
    max_input_chars: int = Field(default=12000, validation_alias="MAX_INPUT_CHARS")
    max_new_tokens: int = Field(default=256, validation_alias="MAX_NEW_TOKENS")
    max_history_messages: int = Field(default=8, validation_alias="MAX_HISTORY_MESSAGES")
    chat_system_prompt: str = Field(default="You are a concise technical assistant.", validation_alias="CHAT_SYSTEM_PROMPT")
    seq2seq_model_id: str = Field(default="google/flan-t5-small", validation_alias="SEQ2SEQ_MODEL_ID")
    chat_model_id: str = Field(default="HuggingFaceTB/SmolLM2-135M-Instruct", validation_alias="CHAT_MODEL_ID")
    bedrock_text_region: str = Field(default="us-east-1", validation_alias="BEDROCK_TEXT_REGION")
    bedrock_text_model_id: str = Field(default="us.openai.gpt-5.6-luna", validation_alias="BEDROCK_TEXT_MODEL_ID")
    ai_runtime: str = Field(default="bedrock", validation_alias="AI_RUNTIME")
    model_provider: str = Field(default="bedrock", validation_alias="MODEL_PROVIDER")
    model_id: str = Field(default="us.openai.gpt-5.6-luna", validation_alias="MODEL_ID")
    model_region: str = Field(default="us-east-1", validation_alias="MODEL_REGION")
    embedding_model_id: str = Field(default="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", validation_alias="EMBEDDING_MODEL_ID")
    top_k: int = Field(default=3, validation_alias="TOP_K")
    min_relevance_score: float = Field(default=0.20, validation_alias="MIN_RELEVANCE_SCORE")
    knowledge_dir: Path = ROOT / "data" / "knowledge_base"
    incidents_file: Path = ROOT / "data" / "incidents.json"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
