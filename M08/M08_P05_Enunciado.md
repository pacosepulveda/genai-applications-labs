# M08.P05 — Enterprise GenAI Assistant v0.8: Production Readiness Pack

**Modalidad:** equipos pequeños  
**Entregable:** `M08_Production_Readiness_Pack.md`

## Objetivo

Integrarás todo M08 para decidir si el piloto definido en M07 está preparado
para convertirse en un servicio operable.

## Material

```text
assets/enterprise_genai_assistant_v08_case.md
assets/ownership_activities.csv
assets/change_catalog.csv
assets/service_metrics.csv
assets/ai_incidents.json
templates/release_manifest.json
notebooks/M08_P05_Production_Readiness.ipynb
```

Además reutiliza las decisiones de P01–P04.

## Parte A — Ownership

Documenta owner para:

```text
product
service
prompt
knowledge corpus
index
model access
eval suite
risk
cost
incident response
```

## Parte B — Release contract

Incluye un release manifest inmutable con versiones exactas.

## Parte C — Delivery

Resume:

```text
change
-> checks
-> staging
-> eval
-> approval
-> canary/shadow
-> production
```

## Parte D — Observability

Define:

```text
SLO
dashboard
alerts
trace contract
redaction
retention
```

## Parte E — Recovery

Comprueba:

```text
rollback
kill switch
fallback
runbooks
incident commander
```

## Parte F — Cost ownership

Define quién observa y decide sobre:

```text
cost/task
agent loops
retries
model routing
```

## Parte G — Readiness decision

Elige:

```text
READY
READY_WITH_CONDITIONS
NOT_READY
```

Cada condición pendiente debe tener:

```text
owner
evidence_required
```

## Parte H — Pack

Genera:

```text
M08_Production_Readiness_Pack.md
```

con:

```text
Executive summary
Readiness decision
Ownership
Release manifest
Quality gates
Platform dependencies
Observability
SLO and alerts
Incident response
Recovery
Cost ownership
Open conditions
```

## Preguntas finales

1. ¿Qué evidencia permite decir que el servicio es operable?
2. ¿Qué dependencia compartida tiene mayor blast radius?
3. ¿Qué capacidad debe tener kill switch antes de producción?
4. ¿Quién es accountable del servicio productivo?
5. ¿Qué debe quedar preparado para que M09 pueda cambiar componentes con seguridad?
