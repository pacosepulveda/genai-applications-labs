from dataclasses import dataclass
from .models import AskRequest, AskTask

@dataclass
class RouteDecision:
    mode: str

def choose_mode(req: AskRequest) -> RouteDecision:
    # Regla determinista: fuentes autoritativas => RAG obligatorio.
    if req.requires_authoritative_sources:
        return RouteDecision("RAG")

    if req.task == AskTask.CORPORATE_KNOWLEDGE:
        return RouteDecision("RAG")

    return RouteDecision("DIRECT")
