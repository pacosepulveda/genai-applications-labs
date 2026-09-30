from pathlib import Path
import pytest

from src.intent_router import IntentRouter

def test_missing_artifact_fails_cleanly(tmp_path):
    router = IntentRouter(tmp_path / "missing.joblib")
    with pytest.raises(Exception):
        router.load()
