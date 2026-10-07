# Módulo 6 — LangChain, RAG, Tools y Agents

## Objetivo

M06 convierte una llamada a modelo en un sistema:

```text
prompt + contrato
      ↓
retrieval
      ↓
evaluación
      ↓
RAG con fuentes
      ↓
tools / agent
      ↓
integración
```

## Ruta esencial de clase

Se mantienen los **seis laboratorios**, pero cada uno se limita a una evidencia concreta:

```text
M06.P01 -> M06.P02 -> M06.P03 -> M06.P04 -> M06.P05 -> M06.P06
```

- **P01** — prompt, Runnable y structured output.
- **P02** — documentos, metadata, embeddings y retriever.
- **P03** — Hit Rate@k y selección básica de `k`.
- **P04** — two-step RAG, citas y no-answer.
- **P05** — tools read-only y `create_agent`.
- **P06** — integración DIRECT / RAG / AGENT.

Las secciones marcadas como **Ampliación** permiten profundizar sin ser necesarias para completar la ruta esencial.

## Entorno

```text
SageMaker Space
ml.t3.large
CPU
us-east-1
```

### Modelo generativo

```text
GPT-5.6 Luna
Amazon Bedrock
us.openai.gpt-5.6-luna
```

La integración usa `ChatBedrockConverse`.

### Embeddings

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

Se ejecutan localmente en CPU.

## API moderna

Los laboratorios utilizan `Runnable`, structured output, retrievers, `create_agent` y `InMemorySaver`. No se utilizan APIs legacy como patrón principal.

## Material

- `M06_P01_Enunciado.md` … `M06_P06_Enunciado.md`
- `notebooks/`
- `assets/`
- `enterprise-genai-assistant/`
