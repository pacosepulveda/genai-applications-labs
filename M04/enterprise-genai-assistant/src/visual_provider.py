from dataclasses import dataclass
from pathlib import Path
import json
import random
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
        img = Image.new("L", (256,256), color=245)
        draw = ImageDraw.Draw(img)
        x = rng.randint(30,170)
        y = rng.randint(30,170)
        draw.rectangle((x,y,x+50,y+50), outline=20, width=4)
        return VisualResult(img, self.name, "mock-v1")

class LocalGANProvider:
    name = "local_gan"

    def __init__(self, artifact_dir: str | Path):
        # TODO M04.P06:
        # cargar gan_config.json, construir Generator y cargar generator.pt
        self.generator = None
        self.latent_dim = None
        self.model_version = None

    def generate(self, prompt: str, seed: int) -> VisualResult:
        # El GAN del laboratorio es incondicional: prompt no controla la imagen.
        # TODO M04.P06
        raise NotImplementedError

def build_visual_provider(name: str, artifact_dir: str | Path):
    # TODO M04.P06
    raise NotImplementedError
