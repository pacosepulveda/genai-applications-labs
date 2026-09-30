from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    router_backend: str = Field(default="classic", validation_alias="ROUTER_BACKEND")
    router_threshold: float = Field(default=0.70, validation_alias="ROUTER_THRESHOLD")
    router_model_version: str = Field(default="m03", validation_alias="ROUTER_MODEL_VERSION")
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
