# M08.P04 — AI Operations: SLO, incidentes y FinOps

**Modalidad:** equipos pequeños  
**Entregable:** alert policy, runbooks y postmortem con nuevo caso de evaluación

## Objetivo

Demostrarás que una aplicación GenAI puede estar disponible técnicamente y,
sin embargo, estar fallando en calidad, seguridad o coste.

## Material

```text
assets/service_metrics.csv
assets/ai_incidents.json
notebooks/M08_P04_AI_Operations.ipynb
```

## Parte A — SLO y señales

Define thresholds para:

```text
availability
p95_latency_s
citation_validity
retrieval_hit_rate
unauthorized_retrieval_count
avg_model_calls_per_task
cost_per_task_eur
```

## Parte B — Alertas

Clasifica cada señal:

```text
INFO
WARNING
CRITICAL
```

Una fuga de autorización debe tratarse de forma distinta a una subida moderada
de latencia.

## Parte C — Incident routing

Para cada incidente asigna:

```text
Incident Commander
Technical Lead
Security
Data/Knowledge
Product
```

solo cuando sea necesario.

## Parte D — Runbook

Define:

```text
detect
contain
recover
verify
communicate
```

## Parte E — Recovery

Decide entre:

```text
rollback release
rollback index
disable agent feature
disable tool
provider fallback
degraded mode
stop service
```

## Parte F — FinOps

No optimices únicamente tokens.

Analiza:

```text
calls/task
cost/task
quality
latency
```

y propone una mejora que mantenga la calidad.

## Parte G — Learning loop

Para un incidente genera:

```text
timeline
impact
cause factors
control failure
corrective actions
new_eval_case
```

## Preguntas

1. ¿Por qué HTTP 200 no demuestra salud del servicio?
2. ¿Cuándo usarías degradación en lugar de apagarlo todo?
3. ¿Por qué cost/task es mejor unidad económica que cost/request?
4. ¿Cómo convierte el postmortem un incidente en una regresión futura?
