from openai import OpenAI
from .base import GenerationResult
from ..settings import settings
from ..prompts import SYSTEM_PROMPT

class OpenAIProvider:
    def __init__(self):
        if not settings.openai_api_key:
            raise RuntimeError("OPENAI_API_KEY no configurada")
        if not settings.openai_model:
            raise RuntimeError("OPENAI_MODEL no configurado")
        kwargs = {"api_key": settings.openai_api_key}
        if settings.openai_base_url:
            kwargs["base_url"] = settings.openai_base_url
        self.client = OpenAI(**kwargs)

    def generate(self, prompt: str) -> GenerationResult:
        response = self.client.responses.create(
            model=settings.openai_model,
            instructions=SYSTEM_PROMPT,
            input=prompt,
            store=False,
        )
        return GenerationResult(
            text=response.output_text,
            provider="openai",
            model=settings.openai_model,
        )
