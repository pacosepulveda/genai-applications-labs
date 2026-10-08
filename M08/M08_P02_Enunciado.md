# M08.P02 — Release Gate & Platform Decisions

**Modalidad:** equipos pequeños  
**Entregable:** release decision record + promotion plan + platform split

## Objetivo

Tratarás una release GenAI como una combinación exacta de artefactos que puede cambiar el comportamiento del sistema aunque el código de aplicación no cambie.

La pregunta no es simplemente:

> ¿Pasan los tests?

La pregunta es:

> ¿Existe evidencia suficiente para promover exactamente esta combinación de artefactos y limitar el blast radius si aparece una regresión?

## Material

```text
assets/change_catalog.csv
assets/quality_gates.csv
assets/platform_capabilities.csv
assets/trace_samples.jsonl
assets/M08_Tabletop_Injects.md
templates/release_manifest.json
templates/M08_P02_Release_Gate_Worksheet.md
```

## Situación inicial

Se prepara una release candidata de Enterprise GenAI Assistant que incluye varios cambios del catálogo.

Debéis decidir qué cambios pueden viajar juntos y cuáles deberían separarse.

## Parte A — Release contract

Revisa `templates/release_manifest.json` y fija explícitamente:

```text
app_version
git_commit
model_id
prompt_version
index_version
policy_version
eval_suite_version
thresholds_version
```

La combinación evaluada debe ser exactamente la que se promueve.

## Parte B — Riesgo por cambio

Utiliza `change_catalog.csv` y revisa los niveles:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

Puedes cambiar la clasificación si justificas la decisión.

Para cada cambio identifica:

```text
failure_mode
required_evidence
owner
rollback_unit
```

## Parte C — Quality gates

A partir de `quality_gates.csv`, decide qué gates son obligatorios para cada cambio:

```text
unit_tests
schema_tests
policy_tests
prompt_eval
retrieval_eval
model_eval
security_eval
authorization_tests
cost_latency_eval
human_approval
rollback_plan
```

No apliques todos los gates mecánicamente a todo. Relaciónalos con el tipo de regresión posible.

## Parte D — Promotion strategy

Diseña el recorrido:

```text
DEV
→ STAGING
→ EVAL
→ APPROVAL
→ CANARY / SHADOW
→ PROD
```

Para cada cambio decide entre:

```text
CANARY
SHADOW
DIRECT_PROMOTION
DO_NOT_PROMOTE
```

## Parte E — Platform split

Revisa `platform_capabilities.csv` y clasifica cada capability como:

```text
SHARED_PLATFORM
PRODUCT_OWNED
SHARED_WITH_PRODUCT_OWNER
```

No construyas una gran plataforma teórica. Elige solo capacidades que ya se repiten y necesiten estandarización.

Debes tratar explícitamente:

- model access;
- CI/CD templates;
- eval tooling;
- tracing;
- RAG infrastructure;
- corpus ownership;
- quality thresholds;
- product runbook.

## Parte F — Trace contract

Revisa `trace_samples.jsonl` y decide qué campos:

```text
KEEP
REDACT
DROP
```

Incluye al menos:

```text
trace_id
user_id
user_email
prompt_text
model_id
prompt_version
source_ids
tool_calls
tokens
latency
outcome
api_key
```

Después define:

```text
retention
access_control
```

## Inyectos

El instructor revelará secuencialmente los inyectos de P02 contenidos en:

```text
assets/M08_Tabletop_Injects.md
```

Después de cada inyecto debes mantener o revisar tu decisión de promoción.

## Entregable

Completa:

```text
templates/M08_P02_Release_Gate_Worksheet.md
```

Debe contener:

```text
release manifest
change risk table
required gates
promotion strategy
rollback target
platform split
trace contract
final decision
```

## Debrief

1. ¿Por qué un cambio de índice es un cambio productivo?
2. ¿Qué ocurre si evaluamos una combinación y promovemos otra?
3. ¿Qué cambio del catálogo tiene mayor necesidad de autorización humana?
4. ¿Por qué Shared Platform no se convierte en owner del outcome del producto?
5. ¿Qué dato de una traza es útil para depurar y a la vez peligroso de conservar sin control?
