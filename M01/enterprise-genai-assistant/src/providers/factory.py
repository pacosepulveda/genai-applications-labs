from .mock_provider import MockProvider
from .openai_provider import OpenAIProvider
from ..settings import settings

def get_provider():
    name = settings.provider.lower().strip()
    if name == "mock":
        return MockProvider()
    if name == "openai":
        return OpenAIProvider()
    raise RuntimeError(f"Provider no soportado: {settings.provider}")
