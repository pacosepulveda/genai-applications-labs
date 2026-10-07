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
        frame = _frame(**features)
        probabilities = self.pipeline.predict_proba(frame)[0]
        index = int(np.argmax(probabilities))
        classes = self.pipeline.named_steps["model"].classes_
        return IntentPrediction(
            intent=str(classes[index]),
            confidence=float(probabilities[index]),
        )


class NeuralRouter:
    def __init__(self, artifact_dir):
        artifact_dir = Path(artifact_dir)
        config = json.loads(
            (artifact_dir / "neural_router_config.json").read_text(encoding="utf-8")
        )
        self.preprocessor = joblib.load(artifact_dir / "neural_preprocessor.joblib")
        self.label_encoder = joblib.load(artifact_dir / "neural_label_encoder.joblib")
        self.model = NeuralIntentMLP(
            input_dim=int(config["input_dim"]),
            num_classes=int(config["num_classes"]),
            hidden_dim=int(config["hidden_dim"]),
        )
        state = torch.load(
            artifact_dir / "neural_router.pt",
            map_location="cpu",
            weights_only=True,
        )
        self.model.load_state_dict(state)
        self.model.eval()

    def predict(self, **features) -> IntentPrediction:
        frame = _frame(**features)
        x = self.preprocessor.transform(frame)
        if hasattr(x, "toarray"):
            x = x.toarray()
        x = np.asarray(x, dtype="float32")
        with torch.no_grad():
            logits = self.model(torch.tensor(x, dtype=torch.float32))
            probabilities = torch.softmax(logits, dim=-1)[0]
            index = int(torch.argmax(probabilities).item())
        intent = self.label_encoder.inverse_transform([index])[0]
        return IntentPrediction(
            intent=str(intent),
            confidence=float(probabilities[index].item()),
        )


def build_router(backend: str, artifact_dir: str | Path):
    artifact_dir = Path(artifact_dir)
    normalized = backend.strip().lower()
    if normalized == "classic":
        return ClassicRouter(artifact_dir / "classic_router.joblib")
    if normalized == "neural":
        return NeuralRouter(artifact_dir)
    raise ValueError(f"ROUTER_BACKEND no soportado: {backend!r}")
