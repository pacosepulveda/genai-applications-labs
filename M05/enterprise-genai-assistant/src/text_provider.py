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
    def generate(self, prompt: str, max_new_tokens: int) -> GenerationResult: ...
    def chat(self, messages: list[dict], max_new_tokens: int) -> GenerationResult: ...

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

    def chat(self, messages: list[dict], max_new_tokens: int) -> GenerationResult:
        last = messages[-1]["content"] if messages else ""
        text = "MOCK CHAT: " + last[:200]
        return GenerationResult(
            text=text,
            provider=self.name,
            model=self.model_id,
            input_tokens=max(1, sum(len(m["content"].split()) for m in messages)),
            output_tokens=max(1, len(text.split())),
            finish_reason="stop",
        )

class LocalSeq2SeqProvider:
    name = "local_seq2seq"

    def __init__(self, model_id: str):
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
        self.model_id = model_id
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
        self.model.eval()

    def generate(self, prompt: str, max_new_tokens: int) -> GenerationResult:
        import torch
        encoded = self.tokenizer(prompt, return_tensors="pt", truncation=True)
        with torch.no_grad():
            out = self.model.generate(**encoded, max_new_tokens=max_new_tokens)
        text = self.tokenizer.decode(out[0], skip_special_tokens=True)
        return GenerationResult(
            text=text,
            provider=self.name,
            model=self.model_id,
            input_tokens=int(encoded["input_ids"].numel()),
            output_tokens=int(out[0].numel()),
            finish_reason="stop",
        )

    def chat(self, messages: list[dict], max_new_tokens: int) -> GenerationResult:
        prompt = messages[-1]["content"] if messages else ""
        return self.generate(prompt, max_new_tokens)

class LocalChatProvider:
    name = "local_chat"

    def __init__(self, model_id: str):
        from transformers import AutoTokenizer, AutoModelForCausalLM
        self.model_id = model_id
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(model_id)
        self.model.eval()

    def generate(self, prompt: str, max_new_tokens: int) -> GenerationResult:
        return self.chat([{"role": "user", "content": prompt}], max_new_tokens)

    def chat(self, messages: list[dict], max_new_tokens: int) -> GenerationResult:
        import torch
        rendered = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        )
        encoded = self.tokenizer(rendered, return_tensors="pt")
        input_len = encoded["input_ids"].shape[1]
        with torch.no_grad():
            out = self.model.generate(**encoded, max_new_tokens=max_new_tokens, do_sample=False)
        new_tokens = out[0, input_len:]
        text = self.tokenizer.decode(new_tokens, skip_special_tokens=True)
        return GenerationResult(
            text=text,
            provider=self.name,
            model=self.model_id,
            input_tokens=int(input_len),
            output_tokens=int(new_tokens.numel()),
            finish_reason="stop",
        )

class BedrockLunaProvider:
    name = "bedrock_luna"

    def __init__(self, region: str, model_id: str):
        self.region = region
        self.model_id = model_id
        self.client = boto3.client("bedrock-runtime", region_name=region)

    @staticmethod
    def _to_result(response, provider, model_id):
        content = response["output"]["message"]["content"]
        text = "".join(block.get("text", "") for block in content if isinstance(block, dict))
        usage = response.get("usage", {})
        return GenerationResult(
            text=text,
            provider=provider,
            model=model_id,
            input_tokens=int(usage.get("inputTokens", 0)),
            output_tokens=int(usage.get("outputTokens", 0)),
            finish_reason=str(response.get("stopReason", "stop")),
        )

    def generate(self, prompt: str, max_new_tokens: int) -> GenerationResult:
        response = self.client.converse(
            modelId=self.model_id,
            messages=[{"role": "user", "content": [{"text": prompt}]}],
            inferenceConfig={"maxTokens": max_new_tokens},
        )
        return self._to_result(response, self.name, self.model_id)

    def chat(self, messages: list[dict], max_new_tokens: int) -> GenerationResult:
        system_blocks = []
        converse_messages = []
        for message in messages:
            role = message["role"]
            content = message["content"]
            if role == "system":
                system_blocks.append({"text": content})
            else:
                converse_messages.append({
                    "role": role,
                    "content": [{"text": content}],
                })
        kwargs = {
            "modelId": self.model_id,
            "messages": converse_messages,
            "inferenceConfig": {"maxTokens": max_new_tokens},
        }
        if system_blocks:
            kwargs["system"] = system_blocks
        response = self.client.converse(**kwargs)
        return self._to_result(response, self.name, self.model_id)

def build_text_provider(name, seq2seq_model_id, chat_model_id, bedrock_region, bedrock_model_id):
    normalized = name.strip().lower()
    if normalized == "mock":
        return MockTextProvider()
    if normalized == "local_seq2seq":
        return LocalSeq2SeqProvider(seq2seq_model_id)
    if normalized == "local_chat":
        return LocalChatProvider(chat_model_id)
    if normalized == "bedrock_luna":
        return BedrockLunaProvider(bedrock_region, bedrock_model_id)
    raise ValueError(f"text provider no soportado: {name!r}")
