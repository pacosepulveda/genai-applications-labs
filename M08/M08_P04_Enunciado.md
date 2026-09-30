# M08.P04 — Git, MLOps y LLMOps: diseñar quality gates

**Modalidad:** individual o parejas  
**Entregable:** política de release y matriz de herramientas

## Objetivo

Tratar cambios de IA como cambios de software/producto que pueden provocar regresiones.

## Material

```text
assets/change_catalog.csv
assets/quality_gates.csv
assets/tooling_scenarios.csv
templates/release_policy.yaml
```

## Tareas

Abre:

```text
notebooks/M08_P04_LLMOps_Quality_Gates.ipynb
```

### Parte A — Clasificar cambios

Revisa el nivel de riesgo propuesto para cada cambio.

Puedes modificarlo si lo justificas.

### Parte B — Quality gates

Define qué checks exige:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

Ejemplos:

- unit tests;
- prompt eval;
- retrieval eval;
- model eval;
- security review;
- cost review;
- authorization tests;
- human approval;
- rollback plan.

### Parte C — Artifact-specific gates

Un cambio `MODEL` no necesita exactamente los mismos checks que `INDEX` o `TOOL_WRITE`.

Define reglas adicionales.

### Parte D — Validador

Implementa:

```python
required_gates(change)
```

y comprueba automáticamente el catálogo.

### Parte E — Tool selection

Para cada escenario T01–T05 decide cuándo usar:

```text
Git/CI
MLflow
MLflow GenAI/tracing
Kubeflow Pipelines
ninguna herramienta adicional
```

No selecciones herramientas porque “son de IA”.

### Parte F — Release flow

Diseña:

```text
PR
-> automated checks
-> staging
-> eval
-> approval if needed
-> canary/shadow
-> production
```

## Preguntas

1. ¿Qué añade LLMOps a MLOps?
2. ¿Por qué cambiar el índice es un cambio productivo?
3. ¿Cuándo Kubeflow sería excesivo?
4. ¿Qué artefactos deben poder hacer rollback?
