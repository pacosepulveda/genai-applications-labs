from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    text_provider: str = Field(default="mock", validation_alias="TEXT_PROVIDER")
    max_input_chars: int = Field(default=12000, validation_alias="MAX_INPUT_CHARS")
    max_new_tokens: int = Field(default=256, validation_alias="MAX_NEW_TOKENS")
    max_history_messages: int = Field(default=8, validation_alias="MAX_HISTORY_MESSAGES")
    seq2seq_model_id: str = Field(default="google/flan-t5-small", validation_alias="SEQ2SEQ_MODEL_ID")
    chat_model_id: str = Field(default="HuggingFaceTB/SmolLM2-135M-Instruct", validation_alias="CHAT_MODEL_ID")
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
