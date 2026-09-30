from pydantic import BaseModel

class RAGAnswer(BaseModel):
    answer: str
    source_ids: list[str]
    insufficient_evidence: bool

def validate_citations(answer: RAGAnswer, retrieved_docs) -> bool:
    allowed = {
        doc.metadata.get("source_id")
        for doc in retrieved_docs
        if doc.metadata.get("status") == "CURRENT"
    }
    cited = set(answer.source_ids)
    return cited <= allowed

def format_context(retrieved_docs) -> str:
    # TODO M06.P06:
    # asigna IDs de contexto y muestra metadata relevante.
    raise NotImplementedError

class RAGService:
    def __init__(self, knowledge, model):
        self.knowledge = knowledge
        self.model = model

    def ask(self, question: str) -> tuple[RAGAnswer, list]:
        # TODO M06.P06:
        # retrieve -> prompt -> structured output -> validate
        raise NotImplementedError
