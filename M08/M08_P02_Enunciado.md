# M08.P02 — Release manifest y quality gates GenAI

**Modalidad:** individual o parejas  
**Entregable:** release manifest validado, matriz de gates y estrategia de rollout

## Objetivo

Tratarás una release GenAI como una combinación exacta de artefactos que modifica
el comportamiento del sistema.

## Material

```text
assets/change_catalog.csv
assets/quality_gates.csv
templates/release_manifest.json
notebooks/M08_P02_Release_Quality_Gates.ipynb
```

## Parte A — Release manifest

Completa una release con:

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

La versión evaluada debe ser exactamente la que se pretende promover.

## Parte B — Riesgo del cambio

Revisa los cambios del catálogo y su nivel:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

Puedes modificarlo si lo justificas.

## Parte C — Quality gates

Define `required_gates(change)` utilizando:

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

## Parte D — Evidencia específica

Añade reglas según el artefacto:

```text
MODEL
PROMPT
INDEX
TOOL_READ
TOOL_WRITE
POLICY
CONFIG
```

## Parte E — Promotion

Diseña:

```text
DEV
-> STAGING
-> EVAL
-> APPROVAL
-> CANARY/SHADOW
-> PROD
```

y explica cuándo utilizarías:

```text
CANARY
SHADOW
DIRECT_PROMOTION
```

## Parte F — Rollback

Define qué versiones exactas se restauran si la release falla.

## Preguntas

1. ¿Por qué un cambio de índice es un cambio productivo?
2. ¿Qué diferencia hay entre evaluar una configuración y promover otra?
3. ¿Por qué una tool de escritura necesita más evidencia que un prompt?
4. ¿Qué artefactos deben quedar fijados en un rollback?
