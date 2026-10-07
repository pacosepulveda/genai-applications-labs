from PIL import Image

from src.storage import ArtifactStore


def test_store_roundtrip(tmp_path):
    store = ArtifactStore(tmp_path)

    image = Image.new(
        "RGB",
        (8, 8),
        color=(128, 128, 128),
    )

    metadata = {
        "artifact_id": "abc",
        "provider": "mock",
    }

    store.save(
        "abc",
        image,
        metadata,
    )

    loaded = store.load_metadata("abc")

    assert loaded["provider"] == "mock"
    assert (tmp_path / "abc.png").exists()
    assert (tmp_path / "abc.json").exists()
