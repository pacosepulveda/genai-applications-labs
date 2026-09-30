from dataclasses import dataclass
from pathlib import Path
import pandas as pd
import joblib

@dataclass
class IntentPrediction:
    intent: str
    confidence: float

class IntentRouter:
    def __init__(self, artifact_path: str | Path):
        self.artifact_path = Path(artifact_path)
        self.pipeline = None

    def load(self):
        # TODO M02.P05
        # Carga self.artifact_path con joblib y guarda el pipeline.
        raise NotImplementedError

    def predict(
        self,
        *,
        request_text: str,
        channel: str,
        business_unit: str,
        language: str,
        urgency: str,
        requires_authoritative_sources: bool,
    ) -> IntentPrediction:
        # TODO M02.P05
        # 1. Construye un DataFrame con una fila.
        # 2. Ejecuta predict_proba.
        # 3. Devuelve clase con mayor probabilidad y confianza.
        raise NotImplementedError
