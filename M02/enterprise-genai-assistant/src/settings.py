from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    provider: str = Field(default="mock", validation_alias="GENAI_PROVIDER")
    openai_api_key: str | None = Field(default=None, validation_alias="OPENAI_API_KEY")
    openai_model: str | None = Field(default=None, validation_alias="OPENAI_MODEL")
    openai_base_url: str | None = Field(default=None, validation_alias="OPENAI_BASE_URL")
    router_threshold: float = Field(default=0.70, validation_alias="ROUTER_THRESHOLD")
    router_model_version: str = Field(default="m02-v1", validation_alias="ROUTER_MODEL_VERSION")
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
