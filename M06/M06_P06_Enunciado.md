# M06.P06 — Enterprise GenAI Assistant v0.6: RAG obligatorio y agente controlado

**Modalidad:** individual o parejas  
**Entregable:** aplicación integrada con RAG, citations, tools read-only, state y tests

## Objetivo

Integrarás los componentes de M06 en la aplicación transversal.

La aplicación tendrá tres modos claramente separados:

```text
DIRECT
RAG
AGENT
```

## Arquitectura

```text
request
  ↓
policy
  ↓
task router
  ├── DIRECT -> text provider
  ├── RAG    -> retriever -> model -> citation validator
  └── AGENT  -> create_agent -> read-only tools
```

## Parte A — Knowledge service

Completa:

```text
src/knowledge.py
```

Responsabilidades:

- cargar documentos;
- excluir obsoletos;
- dividir;
- indexar;
- recuperar;
- devolver metadata.

## Parte B — RAG service

Completa:

```text
src/rag.py
```

Debe producir:

```python
RAGAnswer
```

y validar que sus fuentes pertenecen a los chunks recuperados.

## Parte C — Regla obligatoria

Si:

```text
task = CORPORATE_KNOWLEDGE
```

o:

```text
requires_authoritative_sources = true
```

el flujo debe ser:

```text
RAG
```

Nunca `DIRECT`.

Si retrieval no encuentra evidencia suficiente:

```text
NO_EVIDENCE
```

### Parte D — Agent

El modo `OPERATIONS_ASSIST` puede utilizar:

- `search_knowledge_base`;
- `get_incident`;
- `calculate_duration_minutes`.

No añadas tools de escritura.

### Parte E — Thread state

El endpoint del agente aceptará:

```text
conversation_id
```

que se mapeará a:

```text
thread_id
```

del checkpointer.

### Parte F — API

Completa:

```text
POST /v1/ask
POST /v1/operations
GET  /health
```

`/v1/ask` devuelve como mínimo:

```text
mode
answer
source_ids
insufficient_evidence
```

### Parte G — Observabilidad mínima

Registra sin prompts completos:

```text
request_id
mode
retrieved_source_ids
model/provider
latency
citation_validation
```

### Parte H — Tests

Incluye tests para:

1. documento obsoleto excluido;
2. `PROC-017` devuelve 8 horas y no 24;
3. corporate knowledge nunca usa direct fallback;
4. source IDs inventados son rechazados;
5. pregunta sin evidencia produce `insufficient_evidence`;
6. tools son read-only;
7. threads se mantienen aislados;
8. provider/model puede sustituirse sin cambiar la policy.

## Preguntas finales

1. ¿Qué partes de v0.6 son LangChain y cuáles son lógica de dominio?
2. ¿Qué cambiaría al sustituir `InMemoryVectorStore` por un backend persistente?
3. ¿Qué cambiaría al sustituir el modelo por otro proveedor?
4. ¿Qué componentes escalarían por separado en producción?
5. ¿Qué riesgos quedan pendientes antes de desplegar el sistema?
