# M09.P02 — Arquitectura adaptativa: Edge, Cloud, RAG y Multimodal

**Modalidad:** individual o parejas  
**Entregable:** política de routing + análisis de coste/latencia

## Objetivo

Implementar un router sencillo que seleccione la capacidad adecuada según:

```text
modality
complexity
risk
classification
offline capability
authoritative knowledge
realtime state
cost
latency
```

## Material

```text
assets/adaptive_routing_requests.csv
assets/model_capabilities.csv
```

Abre:

```text
notebooks/M09_P02_Adaptive_Architecture.ipynb
```

## Parte A — Reglas mínimas

Diseña reglas como:

```text
authoritative knowledge
→ RAG

realtime system state
→ TOOL/API

image + high complexity
→ CLOUD_MULTIMODAL

offline/private simple task
→ EDGE

complex reasoning
→ CLOUD_REASONING
```

## Parte B — Router

Implementa `route_request(row)`.

El resultado debe incluir:

```text
route
reason
human_gate
```

## Parte C — Riesgo

Las tareas `CRITICAL` no pueden pasar automáticamente a una ruta que ejecute cambios.

El router debe poder responder:

```text
HUMAN_APPROVAL_REQUIRED
```

o:

```text
UNSUPPORTED_AUTONOMY
```

## Parte D — Coste y latencia

Usando `model_capabilities.csv`, estima:

```text
total_cost
mean_latency
```

de la política elegida.

## Parte E — Comparación

Compara:

```text
ALL_CLOUD_REASONING
vs
ADAPTIVE_ROUTING
```

en coste y latencia.

## Parte F — Reflexión

¿Dónde sacrificarías coste para ganar calidad?

¿Dónde sacrificarías calidad para garantizar privacidad/offline?

## Preguntas

1. ¿Por qué un único modelo para todo puede ser subóptimo?
2. ¿Qué requests deben ir necesariamente a RAG y cuáles a una tool/API?
3. ¿Cuándo edge aporta valor real?
4. ¿Qué control nunca debe delegarse al modelo?
