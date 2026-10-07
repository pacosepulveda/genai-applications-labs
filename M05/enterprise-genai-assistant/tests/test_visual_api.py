from src.models import ImageGenerationRequest
from src.storage import ArtifactStore
import src.main as main_module


def test_generate_image_with_mock(tmp_path):
    original_store = main_module.store

    try:
        main_module.store = ArtifactStore(tmp_path)

        response = main_module.generate_image(
            ImageGenerationRequest(
                prompt="a minimal blue robot",
                provider="mock",
                seed=42,
            )
        )

        assert response.provider == "mock"
        assert response.seed == 42
        assert (tmp_path / f"{response.artifact_id}.png").exists()
        assert (tmp_path / f"{response.artifact_id}.json").exists()

    finally:
        main_module.store = original_store
