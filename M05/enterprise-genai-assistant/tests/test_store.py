from PIL import Image

from src.conversation_store import ConversationStore
from src.storage import ArtifactStore


def test_history_append():
    store = ConversationStore(max_messages=4)
    store.append("c1", "user", "hola")
    assert store.get("c1")[-1]["content"] == "hola"


def test_system_is_inserted_once():
    store = ConversationStore(max_messages=4)
    store.ensure_system("c1", "system")
    store.ensure_system("c1", "system")
    assert [m["role"] for m in store.get("c1")].count("system") == 1


def test_visual_artifact_store_regression(tmp_path):
    store = ArtifactStore(tmp_path)
    image = Image.new("L", (8, 8), color=128)
    store.save("abc", image, {"artifact_id": "abc", "provider": "mock"})
    assert store.load_metadata("abc")["provider"] == "mock"
