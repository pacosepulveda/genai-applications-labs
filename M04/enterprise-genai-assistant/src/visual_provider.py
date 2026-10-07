from dataclasses import dataclass
from io import BytesIO
import base64
import json
import random

import boto3
from PIL import Image, ImageDraw


@dataclass
class VisualResult:
    image: Image.Image
    provider: str
    model_version: str


class MockVisualProvider:
    name = "mock"

    def generate(self, prompt: str, seed: int) -> VisualResult:
        rng = random.Random(seed)
        img = Image.new("RGB", (256, 256), color=(245, 245, 245))
        draw = ImageDraw.Draw(img)
        x = rng.randint(30, 170)
        y = rng.randint(30, 170)
        draw.rectangle((x, y, x + 50, y + 50), outline=(20, 20, 20), width=4)
        return VisualResult(image=img, provider=self.name, model_version="mock-v1")


class BedrockVisualProvider:
    name = "bedrock"

    def __init__(self, region: str, model_id: str):
        self.region = region
        self.model_id = model_id
        self.client = boto3.client("bedrock-runtime", region_name=region)

    def generate(self, prompt: str, seed: int) -> VisualResult:
        body = {
            "prompt": prompt,
            "seed": seed,
            "output_format": "png",
        }
        response = self.client.invoke_model(
            modelId=self.model_id,
            contentType="application/json",
            accept="application/json",
            body=json.dumps(body),
        )
        payload = json.loads(response["body"].read())
        image_bytes = base64.b64decode(payload["images"][0])
        image = Image.open(BytesIO(image_bytes)).convert("RGB")
        return VisualResult(
            image=image,
            provider=self.name,
            model_version=self.model_id,
        )


def build_visual_provider(name: str, bedrock_region: str, bedrock_model_id: str):
    normalized = name.strip().lower()
    if normalized == "mock":
        return MockVisualProvider()
    if normalized == "bedrock":
        return BedrockVisualProvider(bedrock_region, bedrock_model_id)
    raise ValueError(f"visual provider no soportado: {name!r}")
