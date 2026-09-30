class AgentService:
    def __init__(self, model, tools):
        # TODO M06.P06:
        # create_agent(..., checkpointer=InMemorySaver())
        self.agent = None

    def ask(self, conversation_id: str, message: str) -> str:
        # TODO:
        # conversation_id -> thread_id
        raise NotImplementedError
