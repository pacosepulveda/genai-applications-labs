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
        # TODO heredado de M04.P06:
        # conserva la carga de gan_config.json, Generator y generator.pt.
        self.generator = None
        self.latent_dim = None
        self.model_version = None

    def generate(self, prompt: str, seed: int) -> VisualResult:
        # TODO heredado de M04.P06.
        raise NotImplementedError


class BedrockVisualProvider:
    name = "bedrock"

    def __init__(self, region: str, model_id: str):
        self.region = region
        self.model_id = model_id
        self.client = boto3.client("bedrock-runtime", region_name=region)

    def generate(self, prompt: str, seed: int) -> VisualResult:
        # TODO heredado de M04.P06:
        # conserva la implementación validada con Stable Diffusion 3.5 Large.
        raise NotImplementedError


def build_visual_provider(
    name: str,
    artifact_dir: str | Path,
    bedrock_region: str,
    bedrock_model_id: str,
):
    # TODO heredado de M04.P06: conserva tu factoría v0.4.
    raise NotImplementedError
