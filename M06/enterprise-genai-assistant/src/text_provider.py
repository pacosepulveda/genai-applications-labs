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

    def chat(self, messages: list[dict], max_new_tokens: int) -> GenerationResult:
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
            input_tokens=len(prompt.split()),
            output_tokens=len(text.split()),
        )

    def chat(self, messages: list[dict], max_new_tokens: int) -> GenerationResult:
        last = messages[-1]["content"] if messages else ""
        text = f"MOCK CHAT: {last[:200]}"
        return GenerationResult(
            text=text,
            provider=self.name,
            model=self.model_id,
            input_tokens=sum(len(m["content"].split()) for m in messages),
            output_tokens=len(text.split()),
        )


class LocalSeq2SeqProvider:
    name = "local_seq2seq"

    def __init__(self, model_id: str):
        # TODO M05.P06: lazy-load tokenizer y AutoModelForSeq2SeqLM.
        self.model_id = model_id

    def generate(self, prompt: str, max_new_tokens: int) -> GenerationResult:
        # TODO M05.P06
        raise NotImplementedError

    def chat(self, messages: list[dict], max_new_tokens: int) -> GenerationResult:
        prompt = messages[-1]["content"] if messages else ""
        return self.generate(prompt, max_new_tokens)


class LocalChatProvider:
    name = "local_chat"

    def __init__(self, model_id: str):
        # TODO M05.P06: lazy-load tokenizer y AutoModelForCausalLM.
        self.model_id = model_id

    def generate(self, prompt: str, max_new_tokens: int) -> GenerationResult:
        # TODO: tratar como un único mensaje user y reutilizar chat().
        raise NotImplementedError

    def chat(self, messages: list[dict], max_new_tokens: int) -> GenerationResult:
        # TODO:
        # tokenizer.apply_chat_template(..., add_generation_prompt=True)
        # model.generate(...)
        # decodificar SOLO tokens nuevos.
        raise NotImplementedError


class BedrockLunaProvider:
    name = "bedrock_luna"

    def __init__(self, region: str, model_id: str):
        self.region = region
        self.model_id = model_id
        self.client = boto3.client("bedrock-runtime", region_name=region)

    def generate(self, prompt: str, max_new_tokens: int) -> GenerationResult:
        # TODO M05.P06:
        # llama a self.client.converse(
        #   modelId=self.model_id,
        #   messages=[{"role":"user","content":[{"text": prompt}]}],
        #   inferenceConfig={"maxTokens": max_new_tokens},
        # )
        # extrae output.message.content, usage y stopReason.
        raise NotImplementedError

    def chat(self, messages: list[dict], max_new_tokens: int) -> GenerationResult:
        # TODO M05.P06:
        # adapta roles/contenido al contrato Converse.
        # El system message debe enviarse como system, no como un mensaje user.
        raise NotImplementedError


def build_text_provider(
    name: str,
    seq2seq_model_id: str,
    chat_model_id: str,
    bedrock_region: str,
    bedrock_model_id: str,
):
    # TODO M05.P06:
    # mock -> MockTextProvider()
    # local_seq2seq -> LocalSeq2SeqProvider(seq2seq_model_id)
    # local_chat -> LocalChatProvider(chat_model_id)
    # bedrock_luna -> BedrockLunaProvider(bedrock_region, bedrock_model_id)
    # otro -> ValueError
    raise NotImplementedError
