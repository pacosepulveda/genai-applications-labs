from src.main import draft
import src.main as main_module
from src.models import DraftRequest, Confidentiality
from src.routers import IntentPrediction


class FakeRouter:
    def __init__(self, intent="DRAFT", confidence=0.95):
        self.intent = intent
        self.confidence = confidence

    def predict(self, **features):
        return IntentPrediction(
            intent=self.intent,
            confidence=self.confidence,
        )


def test_confidential_is_blocked_before_router():
    class ShouldNotRun:
        def predict(self, **features):
            raise AssertionError("El router no debería ejecutarse")

    main_module.router = ShouldNotRun()
    response = draft(
        DraftRequest(
            task="Resume esta información",
            confidentiality=Confidentiality.CONFIDENTIAL,
        )
    )
    assert response.status == "blocked"
    assert response.routing.intent == "NOT_EVALUATED"


def test_generation_route():
    main_module.router = FakeRouter(intent="DRAFT", confidence=0.95)
    response = draft(DraftRequest(task="Prepara un borrador sobre mantenimiento"))
    assert response.status == "ok"
    assert response.routing.route == "GENERATION"
    assert response.content is not None


def test_low_confidence_goes_to_review():
    main_module.router = FakeRouter(intent="DRAFT", confidence=0.20)
    response = draft(DraftRequest(task="Prepara un borrador sobre mantenimiento"))
    assert response.status == "review"
    assert response.routing.route == "REVIEW"


def test_authoritative_sources_force_controlled_flow():
    main_module.router = FakeRouter(intent="DRAFT", confidence=0.95)
    response = draft(
        DraftRequest(
            task="Indica la política vigente",
            requires_authoritative_sources=True,
        )
    )
    assert response.status == "review"
    assert response.routing.route == "CONTROLLED_KNOWLEDGE_FLOW"


def test_unsupported_is_blocked():
    main_module.router = FakeRouter(intent="UNSUPPORTED", confidence=0.95)
    response = draft(DraftRequest(task="Realiza una operación externa"))
    assert response.status == "blocked"
    assert response.routing.route == "BLOCK"
