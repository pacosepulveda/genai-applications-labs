# TODO M01.P03: sustituye este texto por instrucciones que reflejen las reglas del laboratorio.
SYSTEM_PROMPT = """
Eres un asistente de redacción técnica.

TODO M01.P03
""".strip()

def build_user_prompt(task: str, audience: str) -> str:
    return f"Audiencia: {audience}\n\nTarea: {task}"
