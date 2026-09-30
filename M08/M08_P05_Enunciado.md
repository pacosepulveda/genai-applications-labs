# M08.P05 — Operar IA: métricas, alertas e incidentes

**Modalidad:** equipos pequeños  
**Entregable:** alert policy, ownership, runbooks y postmortem

## Objetivo

Demostrar que un servicio AI puede estar disponible técnicamente y, sin embargo, estar fallando.

## Material

```text
assets/service_metrics.csv
assets/ai_incidents.json
```

## Tareas

Abre:

```text
notebooks/M08_P05_AI_Operations.ipynb
```

### Parte A — SLO/SLI

Propón thresholds para:

```text
availability
p95 latency
citation validity
retrieval hit rate
unauthorized retrieval
cost per query
```

### Parte B — Detección

Implementa alertas.

Una condición de seguridad como:

```text
unauthorized_retrieval_count > 0
```

debe tratarse de forma distinta a una ligera subida de latencia.

### Parte C — Incident routing

Para cada incidente asigna:

```text
Incident Commander / Service Owner
Technical Lead
Security
Data/Knowledge
Product
```

según proceda.

### Parte D — Runbook

Para cada escenario define:

```text
detect
contain
recover
verify
communicate
```

### Parte E — Kill switch / rollback

Decide qué se deshabilita:

- provider;
- RAG version;
- agent feature;
- tool;
- whole service.

### Parte F — Postmortem

Elige un incidente y genera:

```text
timeline
impact
root/cause factors
control failure
corrective actions
eval cases to add
```

## Preguntas

1. ¿Por qué HTTP 200 no significa que la aplicación AI esté sana?
2. ¿Quién debería estar on-call?
3. ¿Cuándo debe activarse un kill switch?
4. ¿Cómo convierte un postmortem un fallo en una mejora del sistema?
