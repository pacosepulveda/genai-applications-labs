from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    router_backend: str = Field(default="classic", validation_alias="ROUTER_BACKEND")
    router_threshold: float = Field(default=0.70, validation_alias="ROUTER_THRESHOLD")
    router_model_version: str = Field(default="m03", validation_alias="ROUTER_MODEL_VERSION")

    visual_provider: str = Field(default="mock", validation_alias="VISUAL_PROVIDER")
    bedrock_image_region: str = Field(default="us-west-2", validation_alias="BEDROCK_IMAGE_REGION")
    bedrock_image_model_id: str = Field(
        default="stability.sd3-5-large-v1:0",
        validation_alias="BEDROCK_IMAGE_MODEL_ID",
    )

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
