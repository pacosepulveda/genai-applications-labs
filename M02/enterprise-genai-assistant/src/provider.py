class MockProvider:
    def generate(self, task: str) -> str:
        return (
            "BORRADOR DE DEMOSTRACIÓN\n\n"
            "Este contenido procede del provider mock. "
            "La solicitud debe revisarse antes de cualquier uso operativo."
        )
