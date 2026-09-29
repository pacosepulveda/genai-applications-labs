# Enterprise GenAI Assistant — M01 starter

Primera vertical funcional del proyecto transversal. En M01 no incorpora RAG ni herramientas.

## Arranque

```bash
python -m venv .venv
pip install -r requirements.txt
cp .env.example .env
uvicorn src.main:app --reload --port 8080
```

Visita `http://localhost:8080/docs`.

## Modo mock

`GENAI_PROVIDER=mock` permite ejecutar todo sin credenciales.

## Modo OpenAI opcional

Configura en `.env`:

```text
GENAI_PROVIDER=openai
OPENAI_API_KEY=...
OPENAI_MODEL=...
```

La implementación usa la Responses API y solicita `store=False`.
