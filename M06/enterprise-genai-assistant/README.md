# Enterprise GenAI Assistant — M06

La versión 0.6 **extiende v0.5**.

## Conserva

```text
POST /v1/draft
POST /v1/images
POST /v1/text
POST /v1/chat
```

## Añade

```text
POST /v1/ask
POST /v1/operations
GET  /health
```

## Runtime del curso

```text
SageMaker Space: us-east-1
Compute: ml.t3.large · CPU
LLM: us.openai.gpt-5.6-luna
LangChain adapter: ChatBedrockConverse
Embeddings: sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 · local CPU
```

## Modos

```text
DIRECT -> TextModelProvider -> Luna
RAG    -> authorized retrieval -> Luna -> citation validator
AGENT  -> create_agent(Luna) -> read-only tools
```

No se almacenan claves AWS en el proyecto: las llamadas utilizan el SageMaker Execution Role.

Los tests unitarios no deben realizar llamadas reales a Bedrock.
