# M08.P03 — Production Day & Readiness Review

**Modalidad:** equipos pequeños  
**Entregable:** incident decision log + production readiness pack

## Objetivo

Operarás Enterprise GenAI Assistant durante una jornada con degradaciones de disponibilidad, calidad, seguridad y coste.

La práctica termina con una decisión:

```text
READY
READY_WITH_CONDITIONS
NOT_READY
```

## Material

```text
assets/enterprise_genai_assistant_v08_case.md
assets/service_metrics.csv
assets/ai_incidents.json
assets/M08_Tabletop_Injects.md
templates/M08_P03_Production_Readiness_Worksheet.md
```

Todo el contexto necesario está dentro de M08. No necesitas haber realizado los laboratorios de M07.

## Situación inicial

El servicio candidato incluye:

```text
RAG read-only con citas
consulta read-only de incidentes
cálculo determinista de duración
```

y mantiene fuera de alcance:

```text
write tools
cambios automáticos en producción
aprobación automática de accesos
```

## Parte A — SLO y señales

Antes de leer los incidentes, define qué señales considerarías operativas y qué señales describen calidad o seguridad.

Trabaja al menos con:

```text
availability
p95_latency_s
citation_validity
retrieval_hit_rate
unauthorized_retrieval_count
avg_model_calls_per_task
cost_per_task_eur
```

Para cada señal define:

```text
NORMAL
WARNING
CRITICAL
```

No todos los thresholds tienen la misma semántica: una fuga de autorización puede ser crítica aunque solo ocurra una vez.

## Parte B — Roles de incidente

Define quién asume, cuando corresponda:

```text
Incident Commander
Technical Lead
Security
Data / Knowledge
Product
Platform
```

No añadas roles innecesarios a todos los incidentes.

## Parte C — Runbook mínimo

Para cada tipo de incidente utiliza:

```text
DETECT
CONTAIN
RECOVER
VERIFY
COMMUNICATE
```

Las posibles acciones incluyen:

```text
rollback release
rollback index
disable RAG
disable agent feature
disable tool
provider fallback
degraded mode
stop service
```

## Parte D — Tabletop por inyectos

El instructor revelará los inyectos de P03 en orden.

Después de cada uno debes registrar:

```text
what changed
severity
customer/business impact
immediate containment
owner
recovery action
evidence to restore service
```

No esperes al final para tomar todas las decisiones.

## Parte E — FinOps operacional

Cuando aparezca un spike de coste no optimices únicamente tokens.

Relaciona:

```text
model calls/task
cost/task
quality
latency
```

y decide qué control recuperarías primero.

## Parte F — Learning loop

Elige uno de los incidentes y genera un mini-postmortem:

```text
timeline
impact
contributing factors
control failure
corrective action
new_eval_case
```

La acción correctiva debe reducir la probabilidad de repetir el mismo fallo o mejorar su detección/contención.

## Parte G — Production readiness

Con la evidencia acumulada, evalúa si existen capacidades suficientes para:

```text
OBSERVE
RESPOND
RECOVER
OWN
```

Comprueba específicamente:

- owners explícitos;
- release manifest reproducible;
- quality gates;
- staging representativo;
- rollback;
- kill switch;
- fallback evaluado;
- SLO y alertas;
- runbooks;
- incident process;
- cost ownership;
- trazabilidad con redaction y access control.

## Parte H — Decisión final

Elige:

```text
READY
READY_WITH_CONDITIONS
NOT_READY
```

Si existen condiciones abiertas, cada una debe incluir:

```text
owner
evidence_required
what_is_blocked_until_closed
```

## Entregable

Completa:

```text
templates/M08_P03_Production_Readiness_Worksheet.md
```

Debe contener:

```text
SLO/alert posture
incident decision log
recovery actions
postmortem learning
cost decision
readiness assessment
final decision
open conditions
```

## Debrief

1. ¿Por qué HTTP 200 no demuestra salud de una aplicación GenAI?
2. ¿Qué incidente exige contención inmediata aunque las métricas de disponibilidad sean buenas?
3. ¿Cuándo es preferible degradar una capacidad en vez de apagar todo el servicio?
4. ¿Por qué `cost/task` es más útil que mirar tokens de forma aislada?
5. ¿Qué evidencia debe existir antes de declarar el servicio operable?
