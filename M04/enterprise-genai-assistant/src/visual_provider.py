from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
import base64
import json
import random

import boto3
import numpy as np
import torch
from PIL import Image, ImageDraw

from .gan_model import Generator


@dataclass
class VisualResult:
    image: Image.Image
    provider: str
    model_version: str


class MockVisualProvider:
    name = "mock"

    def generate(self, prompt: str, seed: int) -> VisualResult:
        rng = random.Random(seed)
        img = Image.new("L", (256, 256), color=245)
        draw = ImageDraw.Draw(img)
        x = rng.randint(30, 170)
        y = rng.randint(30, 170)
        draw.rectangle((x, y, x + 50, y + 50), outline=20, width=4)
        return VisualResult(img, self.name, "mock-v1")


class LocalGANProvider:
    name = "local_gan"

    def __init__(self, artifact_dir: str | Path):
        artifact_dir = Path(artifact_dir)
        # TODO M04.P06:
        # 1. cargar gan_config.json;
        # 2. construir Generator(latent_dim, hidden_dim);
        # 3. cargar generator.pt con map_location="cpu";
        # 4. model.eval().
        self.generator = None
        self.latent_dim = None
        self.model_version = None

    def generate(self, prompt: str, seed: int) -> VisualResult:
        # La GAN del laboratorio es incondicional: prompt no controla la imagen.
        # TODO M04.P06:
        # usa torch.Generator(device="cpu").manual_seed(seed), genera z,
        # ejecuta inference_mode(), transforma [-1,1] -> [0,255] y devuelve PIL.Image.
        raise NotImplementedError


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
        # response = self.client.invoke_model(modelId=self.model_id, body=json.dumps(body))
        # payload = json.loads(response["body"].read())
        # image_bytes = base64.b64decode(payload["images"][0])
        # image = Image.open(BytesIO(image_bytes)).convert("RGB")
        # return VisualResult(image, self.name, self.model_id)
        raise NotImplementedError


def build_visual_provider(
    name: str,
    artifact_dir: str | Path,
    bedrock_region: str,
    bedrock_model_id: str,
):
    # TODO M04.P06:
    # mock -> MockVisualProvider()
    # local_gan -> LocalGANProvider(artifact_dir)
    # bedrock -> BedrockVisualProvider(bedrock_region, bedrock_model_id)
    # otro valor -> ValueError
    raise NotImplementedError
