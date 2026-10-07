# M06.P06 — Enterprise GenAI Assistant v0.6: integración guiada

**Modalidad:** individual o parejas  
**Entregable:** routing DIRECT/RAG/AGENT y pruebas críticas

## Objetivo

Integrarás las piezas ya construidas. **No vuelvas a implementar desde cero P02, P04 o P05.**

La arquitectura es:

```text
request
  ↓
policy / routing
  ├── DIRECT
  ├── RAG
  └── AGENT
```

## Parte A — Reutilización

Lleva al scaffold de `enterprise-genai-assistant/` las implementaciones que ya tienes de:

- knowledge/retrieval;
- RAG + citation validator;
- tools/agent.

Los endpoints de M05 se conservan; no son el foco de esta práctica.

## Parte B — Regla de routing

Debe cumplirse:

```text
requires_authoritative_sources=true -> RAG
CORPORATE_KNOWLEDGE              -> RAG
```

La decisión no se delega al modelo.

## Parte C — `/v1/ask`

Completa el flujo:

```text
DIRECT -> provider textual
RAG    -> RAGService
```

Si RAG devuelve evidencia insuficiente:

```text
NO_EVIDENCE
```

Nunca hagas fallback silencioso a DIRECT.

## Parte D — `/v1/operations`

Conecta el `AgentService` de P05.

La práctica utiliza únicamente tools read-only.

## Parte E — Pruebas críticas

Comprueba como mínimo:

1. `PROC-017 v2.1 OBSOLETE` no se utiliza;
2. `PROC-017` vigente indica **8 horas**, no 24;
3. una cita inventada se rechaza;
4. corporate knowledge no hace fallback DIRECT;
5. el caso sin evidencia devuelve no-answer.

## Ampliación

- aislamiento de threads;
- observabilidad detallada;
- regresión de todos los endpoints de v0.5.

## Preguntas finales

1. ¿Qué responsabilidad pertenece a policy y cuál al modelo?
2. ¿Qué cambiaría al sustituir el vector store?
3. ¿Qué cambiaría al sustituir Luna?
4. ¿Por qué DIRECT, RAG y AGENT no deberían convertirse en un único flujo opaco?
