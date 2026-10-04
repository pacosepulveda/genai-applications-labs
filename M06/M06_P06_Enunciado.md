# M06.P06 — Enterprise GenAI Assistant v0.6: RAG obligatorio y agente controlado

**Modalidad:** individual o parejas  
**Entregable:** aplicación integrada con RAG, citations, tools read-only, state y tests

## Objetivo

Extenderás **Enterprise GenAI Assistant v0.5**. La v0.6 no sustituye capacidades anteriores.

Debe conservar `/v1/draft`, `/v1/images`, `/v1/text` y `/v1/chat`, y añadir `/v1/ask` y `/v1/operations`.

## Arquitectura

```text
request
  ↓
policy
  ↓
task router
  ├── DIRECT -> TextModelProvider -> GPT-5.6 Luna
  ├── RAG    -> retriever -> Luna -> citation validator
  └── AGENT  -> create_agent(Luna) -> read-only tools
```

### Parte A — Knowledge service

Completa `src/knowledge.py`: cargar, excluir obsoletos, dividir, indexar, recuperar y devolver metadata.

### Parte B — RAG service

Completa `src/rag.py`. Debe producir `RAGAnswer` y validar citas.

### Parte C — Regla obligatoria

`CORPORATE_KNOWLEDGE` o `requires_authoritative_sources=true` siempre seleccionan RAG. Si no hay evidencia, `NO_EVIDENCE`. Nunca fallback DIRECT.

### Parte D — Agent

`OPERATIONS_ASSIST` puede utilizar únicamente `search_knowledge_base`, `get_incident` y `calculate_duration_minutes`. No añadas tools de escritura.

### Parte E — Thread state

`conversation_id` se mapea a `thread_id` del checkpointer.

### Parte F — API

Completa `/v1/ask`, `/v1/operations` y conserva los endpoints heredados.

### Parte G — Observabilidad mínima

Registra, sin prompts completos: `request_id`, `mode`, `retrieved_source_ids`, `model/provider`, latencia y `citation_validation`.

### Parte H — Tests

Incluye pruebas para documento obsoleto excluido; `PROC-017` devuelve 8 horas y no 24; corporate knowledge nunca usa direct fallback; citas inventadas rechazadas; no-evidence; tools read-only; threads aislados; provider sustituible sin cambiar policy; y endpoints de v0.5 conservados.

## Preguntas finales

1. ¿Qué partes son LangChain y cuáles lógica de dominio?
2. ¿Qué cambia con un vector store persistente?
3. ¿Qué cambia al sustituir el modelo?
4. ¿Qué componentes escalarían por separado?
5. ¿Qué riesgos quedan pendientes antes de producción?
