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
        return VisualResult(img, self.name, "mock-v1")


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

        # TODO M04.P06:
        # 1. invoca self.client.invoke_model(...);
        # 2. convierte response["body"] a JSON;
        # 3. decodifica payload["images"][0] desde base64;
        # 4. abre los bytes con PIL y devuelve VisualResult.
        raise NotImplementedError


def build_visual_provider(
    name: str,
    bedrock_region: str,
    bedrock_model_id: str,
):
    # TODO M04.P06:
    # mock -> MockVisualProvider()
    # bedrock -> BedrockVisualProvider(...)
    # cualquier otro valor -> ValueError
    raise NotImplementedError
