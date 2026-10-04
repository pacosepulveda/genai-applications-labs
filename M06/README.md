# Módulo 6 — LangChain, RAG, Tools y Agents

## Objetivo

En M06 dejamos de estudiar el modelo de forma aislada y construimos una aplicación alrededor de él.

```text
Runnable + prompt + structured output
              ↓
documents + metadata + chunking
              ↓
embeddings + vector store + retriever
              ↓
retrieval evaluation
              ↓
two-step RAG + citations
              ↓
tools + create_agent + state
              ↓
Enterprise GenAI Assistant v0.6
```

## Entorno de laboratorio

Todo se ejecuta desde el SageMaker Space facilitado por el instructor:

- `ml.t3.large`;
- CPU, sin GPU;
- navegador únicamente;
- SageMaker en `us-east-1`.

### Modelo generativo

Las prácticas que necesitan generación, structured output o tool calling utilizan:

```text
GPT-5.6 Luna
Amazon Bedrock
region: us-east-1
model/inference profile: us.openai.gpt-5.6-luna
```

La integración LangChain utiliza `ChatBedrockConverse`.

### Embeddings

El retrieval utiliza un modelo local de embeddings precargado en el entorno:

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

Se ejecuta en CPU. No requiere un segundo modelo Bedrock ni permisos adicionales.

El notebook P02 incluye además una alternativa didáctica local para distinguir claramente:

```text
embedding model != vector store != retriever
```

## Orden recomendado

```text
M06.P01 -> M06.P02 -> M06.P03 -> M06.P04 -> M06.P05 -> M06.P06
```

## API moderna

Los laboratorios trabajan con:

- `Runnable`;
- `ChatBedrockConverse`;
- `create_agent`;
- `InMemorySaver`;
- structured output;
- retrievers actuales.

No utilizan `LLMChain`, `ConversationBufferMemory` ni `AgentExecutor` como patrón principal.

## Continuidad

`Enterprise GenAI Assistant v0.6` **extiende v0.5**. No elimina las capacidades anteriores.

A los endpoints ya construidos se añaden:

```text
POST /v1/ask
POST /v1/operations
```

## Material

- `M06_P01_Enunciado.md` … `M06_P06_Enunciado.md`
- `notebooks/`
- `assets/`
- `enterprise-genai-assistant/`
