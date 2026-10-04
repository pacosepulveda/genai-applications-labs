class MockProvider:
    def generate(self, task: str) -> str:
        return (
            "BORRADOR DE DEMOSTRACIÓN\n\n"
            "Contenido generado por el provider mock. "
            "Debe revisarse antes de uso operativo."
        )
