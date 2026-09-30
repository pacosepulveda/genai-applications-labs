from dataclasses import dataclass
from pathlib import Path
import json
import joblib
import numpy as np
import pandas as pd
import torch

from .neural_model import NeuralIntentMLP

@dataclass
class IntentPrediction:
    intent: str
    confidence: float

def _frame(**kwargs):
    return pd.DataFrame([kwargs])

class ClassicRouter:
    def __init__(self, artifact_path):
        self.pipeline = joblib.load(artifact_path)

    def predict(self, **features) -> IntentPrediction:
        # TODO M03.P06
        raise NotImplementedError

class NeuralRouter:
    def __init__(self, artifact_dir):
        artifact_dir = Path(artifact_dir)
        # TODO M03.P06:
        # cargar config, preprocessor, label encoder y state_dict
        self.model = None
        self.preprocessor = None
        self.label_encoder = None

    def predict(self, **features) -> IntentPrediction:
        # TODO M03.P06
        raise NotImplementedError

def build_router(backend: str, artifact_dir: str | Path):
    artifact_dir = Path(artifact_dir)
    # TODO M03.P06
    raise NotImplementedError
