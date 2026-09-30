from src.storage import ArtifactStore
from PIL import Image

def test_store_roundtrip(tmp_path):
    store = ArtifactStore(tmp_path)
    image = Image.new("L",(8,8),color=128)
    metadata = {"artifact_id":"abc","provider":"mock"}
    store.save("abc", image, metadata)
    assert store.load_metadata("abc")["provider"] == "mock"
