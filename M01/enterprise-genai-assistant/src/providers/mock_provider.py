from .base import GenerationResult

class MockProvider:
    def generate(self, prompt: str) -> GenerationResult:
        # El mock hace el laboratorio reproducible y permite probar la arquitectura sin credenciales.
        text = (
            "BORRADOR DE DEMOSTRACIÓN\n\n"
            "Objetivo: producir una primera versión revisable del contenido solicitado.\n\n"
            "Contenido: este resultado procede del provider mock; sustituye esta respuesta "
            "por un modelo real únicamente en un entorno autorizado.\n\n"
            "Supuestos: no se ha consultado ninguna fuente corporativa ni externa."
        )
        return GenerationResult(text=text, provider="mock", model="deterministic-demo")
