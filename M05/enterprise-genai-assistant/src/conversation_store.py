class ConversationStore:
    def __init__(self, max_messages: int = 8):
        self.max_messages = max_messages
        self._conversations: dict[str, list[dict]] = {}

    def get(self, conversation_id: str):
        return list(self._conversations.get(conversation_id, []))

    def append(self, conversation_id: str, role: str, content: str):
        history = self._conversations.setdefault(conversation_id, [])
        history.append({"role": role, "content": content})

    def ensure_system(self, conversation_id: str, content: str):
        history = self._conversations.setdefault(conversation_id, [])
        if not history or history[0].get("role") != "system":
            history.insert(0, {"role": "system", "content": content})

    def compact(self, conversation_id: str):
        history = self._conversations.get(conversation_id, [])
        if len(history) <= self.max_messages:
            return False

        # TODO M05.P06:
        # conserva system si existe y después los últimos mensajes
        # hasta max_messages. No resumas ni crees memoria externa.
        raise NotImplementedError
