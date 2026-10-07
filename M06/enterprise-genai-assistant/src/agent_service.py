class AgentService:
    def __init__(self, model, tools):
        from langchain.agents import create_agent
        from langgraph.checkpoint.memory import InMemorySaver

        self.agent = create_agent(
            model=model,
            tools=tools,
            checkpointer=InMemorySaver(),
            system_prompt=(
                "Eres un asistente de operaciones. "
                "Utiliza únicamente tools read-only. "
                "No inventes datos operativos."
            ),
        )

    def ask(self, conversation_id: str, message: str) -> str:
        result = self.agent.invoke(
            {"messages": [{"role": "user", "content": message}]},
            config={"configurable": {"thread_id": conversation_id}},
        )
        messages = result.get("messages", [])
        if not messages:
            return ""
        last = messages[-1]
        return getattr(last, "content", str(last))
