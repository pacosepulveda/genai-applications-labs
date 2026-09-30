class ConversationStore:
    def __init__(self, max_messages: int = 8):
        self.max_messages = max_messages
        self._conversations: dict[str, list[dict]] = {}

    def get(self, conversation_id: str):
        return list(self._conversations.get(conversation_id, []))

    def append(self, conversation_id: str, role: str, content: str):
        history = self._conversations.setdefault(conversation_id, [])
        history.append({"role": role, "content": content})

    def compact(self, conversation_id: str):
        history = self._conversations.get(conversation_id, [])
        if len(history) <= self.max_messages:
            return False

        # TODO M05.P06:
        # conserva como máximo los últimos max_messages.
        # No hay memoria externa ni resumen en esta versión.
        raise NotImplementedError
