from src.conversation_store import ConversationStore

def test_history_append():
    store = ConversationStore(max_messages=4)
    store.append("c1","user","hola")
    assert store.get("c1")[-1]["content"] == "hola"
