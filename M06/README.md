# Módulo 6 — LangChain, RAG, Tools y Agents

## Objetivo

M06 convierte una llamada a un modelo en un sistema de aplicación:

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
integración DIRECT / RAG / AGENT
```

## Formato de los laboratorios

Los notebooks, scripts y la aplicación están **completamente implementados**. No es necesario copiar código ni rellenar `TODOs`.

El trabajo práctico sigue este patrón:

```text
ejecutar -> inspeccionar -> modificar -> comparar -> explicar
```

## Ruta de clase

Se mantienen las seis prácticas porque cada una introduce una pieza distinta:

```text
M06.P01 -> M06.P02 -> M06.P03 -> M06.P04 -> M06.P05 -> M06.P06
```

- **P01** — prompt, Runnable y structured output.
- **P02** — documentos, metadata, embeddings y retriever.
- **P03** — evaluación de retrieval y `NO_EVIDENCE`.
- **P04** — two-step RAG, citas y no-answer.
- **P05** — tools read-only y `create_agent`.
- **P06** — integración DIRECT / RAG / AGENT.

Las ampliaciones están preparadas para quien quiera profundizar, pero no son necesarias para seguir la ruta de clase.

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

### Embeddings

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

Se ejecutan localmente en CPU.

## Material

- `M06_P01_Enunciado.md` … `M06_P06_Enunciado.md`
- `notebooks/` — notebooks ejecutables
- `scripts/` — equivalentes `.py` ejecutables
- `assets/` — corpus, incidentes y casos de evaluación
- `enterprise-genai-assistant/` — aplicación v0.6 completa
