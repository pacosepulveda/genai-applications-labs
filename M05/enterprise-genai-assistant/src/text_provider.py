from dataclasses import dataclass
from typing import Protocol

import boto3


@dataclass
class GenerationResult:
    text: str
    provider: str
    model: str
    input_tokens: int
    output_tokens: int
    finish_reason: str = "stop"


class TextModelProvider(Protocol):
    def generate(self, prompt: str, max_new_tokens: int) -> GenerationResult:
        ...


class MockTextProvider:
    name = "mock"
    model_id = "mock-text-v1"

    def generate(self, prompt: str, max_new_tokens: int) -> GenerationResult:
        text = "MOCK: " + prompt[:200]
        return GenerationResult(
            text=text,
            provider=self.name,
            model=self.model_id,
            input_tokens=max(1, len(prompt.split())),
            output_tokens=max(1, len(text.split())),
            finish_reason="stop",
        )


class BedrockLunaProvider:
    name = "bedrock_luna"

    def __init__(self, region: str, model_id: str):
        self.region = region
        self.model_id = model_id
        self.client = boto3.client("bedrock-runtime", region_name=region)

    def generate(self, prompt: str, max_new_tokens: int) -> GenerationResult:
        # TODO M05.P06:
        # 1. llama a self.client.converse(...)
        # 2. messages debe contener un mensaje user con el prompt
        # 3. inferenceConfig debe incluir maxTokens
        # 4. extrae output.message.content, usage y stopReason
        # 5. devuelve GenerationResult
        raise NotImplementedError


def build_text_provider(
    name: str,
    bedrock_region: str,
    bedrock_model_id: str,
):
    # TODO M05.P06:
    # mock -> MockTextProvider()
    # bedrock_luna -> BedrockLunaProvider(bedrock_region, bedrock_model_id)
    # otro valor -> ValueError
    raise NotImplementedError
