# Módulo 6 — LangChain, RAG, Tools y Agents

## Objetivo

En M06 dejamos de estudiar el modelo de forma aislada y construimos una aplicación alrededor de él.

La progresión es:

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

## Entorno

Todos los laboratorios están diseñados para ejecutarse desde el entorno web facilitado por el instructor.

No se requiere instalar software en el equipo del alumno ni utilizar credenciales personales.

El laboratorio distingue dos tipos de componentes:

### Componentes locales

Funcionan sin consumir un modelo generativo gestionado:

- carga de documentos;
- splitting;
- vector store;
- retrieval;
- evaluación;
- tools deterministas;
- tests.

### Componentes con modelo

El entorno facilitado por el instructor proporcionará un modelo compatible para las celdas de generación y agent.

El código mantiene el proveedor desacoplado.

## Orden recomendado

```text
M06.P01 -> M06.P02 -> M06.P03 -> M06.P04 -> M06.P05 -> M06.P06
```

## API moderna

Los laboratorios utilizan la API actual de LangChain:

- `Runnable`s;
- `create_agent`;
- `InMemorySaver`;
- structured output;
- retrievers actuales.

No utilizan `LLMChain`, `ConversationBufferMemory` ni `AgentExecutor` como patrón principal.

## Material

- `M06_P01_Enunciado.md`
- `M06_P02_Enunciado.md`
- `M06_P03_Enunciado.md`
- `M06_P04_Enunciado.md`
- `M06_P05_Enunciado.md`
- `M06_P06_Enunciado.md`
- `notebooks/`
- `assets/`
- `enterprise-genai-assistant/`
