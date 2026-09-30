from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT = Path(__file__).resolve().parents[1]

class Settings(BaseSettings):
    ai_runtime: str = Field(default="mock", validation_alias="AI_RUNTIME")
    model_provider: str = Field(default="instructor", validation_alias="MODEL_PROVIDER")
    model_id: str = Field(default="", validation_alias="MODEL_ID")
    embedding_model_id: str = Field(
        default="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        validation_alias="EMBEDDING_MODEL_ID",
    )
    top_k: int = Field(default=3, validation_alias="TOP_K")
    min_relevance_score: float = Field(default=0.20, validation_alias="MIN_RELEVANCE_SCORE")
    max_input_chars: int = Field(default=12000, validation_alias="MAX_INPUT_CHARS")
    knowledge_dir: Path = ROOT / "data" / "knowledge_base"
    incidents_file: Path = ROOT / "data" / "incidents.json"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
