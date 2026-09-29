from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    provider: str = Field(default="mock", validation_alias="GENAI_PROVIDER")
    openai_api_key: str | None = Field(default=None, validation_alias="OPENAI_API_KEY")
    openai_model: str | None = Field(default=None, validation_alias="OPENAI_MODEL")
    openai_base_url: str | None = Field(default=None, validation_alias="OPENAI_BASE_URL")
    log_prompts: bool = Field(default=False, validation_alias="LOG_PROMPTS")
    max_input_chars: int = Field(default=4000, validation_alias="MAX_INPUT_CHARS")
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
