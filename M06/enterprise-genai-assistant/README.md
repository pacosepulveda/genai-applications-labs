# Enterprise GenAI Assistant — M06 v0.6

Aplicación acumulativa completamente implementada para trabajar arquitectura, pruebas y comportamiento sin completar scaffolds.

## Modos

```text
DIRECT -> generación textual
RAG    -> conocimiento corporativo con fuentes
AGENT  -> operaciones con tools read-only
```

## Capacidades acumulativas

```text
POST /v1/draft
POST /v1/images
POST /v1/text
POST /v1/chat
POST /v1/ask
POST /v1/operations
GET  /health
```

## Ejecutar tests

```bash
python -m pytest -q
```

Los tests no necesitan realizar llamadas reales a Bedrock para validar routing, citas, vigencia documental y funciones deterministas.

## Arrancar API

```bash
uvicorn src.main:app --reload --port 8080
```

## Trabajo de la práctica

El código necesario está implementado. Inspecciona routing, fuerza casos de error, prueba citas falsas, compara `CURRENT/OBSOLETE`, provoca `NO_EVIDENCE` y observa las tool calls del agent.

## Runtime del curso

```text
SageMaker Space: us-east-1
Compute: ml.t3.large · CPU
LLM: us.openai.gpt-5.6-luna
Embeddings: sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 · CPU
```

Las llamadas AWS utilizan el SageMaker Execution Role; no se almacenan API keys en el repositorio.
