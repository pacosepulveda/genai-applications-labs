# M09.P02 — Arquitectura adaptativa: routing por capability

**Modalidad:** individual o parejas  
**Entregable:** política de routing y comparación coste/latencia

## Objetivo

Implementar un router sencillo que no trate todos los backends como equivalentes.

## Material

```text
assets/adaptive_routing_requests.csv
assets/model_capabilities.csv
notebooks/M09_P02_Adaptive_Architecture.ipynb
```

## Parte A — Requests

Cada petición describe:

```text
modality
complexity
privacy
offline_required
authoritative_knowledge
realtime_state
impact
```

## Parte B — Backends

Trabajarás con capacidades abstractas:

```text
EDGE_SLM
CLOUD_STANDARD
CLOUD_REASONING
CLOUD_MULTIMODAL
RAG
TOOL_API
```

No representan proveedores concretos.

## Parte C — Router

Implementa:

```python
route_request(row)
```

El resultado debe incluir:

```text
route
reason
human_gate
```

Reglas mínimas:

```text
authoritative_knowledge -> RAG
realtime_state          -> TOOL_API
offline/private simple  -> EDGE_SLM
image                    -> CLOUD_MULTIMODAL
complex reasoning       -> CLOUD_REASONING
otherwise               -> CLOUD_STANDARD
```

## Parte D — Human gate

Una tarea de impacto `HIGH` o `CRITICAL` que pueda ejecutar acciones debe requerir:

```text
HUMAN_APPROVAL_REQUIRED
```

## Parte E — Coste y latencia

Estima:

```text
total_cost
mean_latency
```

para:

```text
ALL_CLOUD_REASONING
vs
ADAPTIVE_ROUTING
```

## Parte F — Decisión

Explica qué requests justificarían pagar más por capability y cuáles priorizan privacidad/offline.

## Preguntas

1. ¿Por qué una interfaz común no implica capabilities equivalentes?
2. ¿Cuándo RAG es mejor que long context?
3. ¿Cuándo edge aporta valor real?
4. ¿Qué decisión nunca debería inferirse solo desde coste?
