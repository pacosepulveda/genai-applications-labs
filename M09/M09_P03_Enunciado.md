# M09.P03 — Future Scenario Stress Test

**Modalidad:** equipos pequeños  
**Entregable:** respuestas a escenarios + Architecture Resilience Report

## Objetivo

Comprobar si la arquitectura y el operating model sobreviven a cambios tecnológicos, económicos y regulatorios.

## Material

```text
assets/future_scenarios.json
assets/current_architecture_metrics.csv
```

Abre:

```text
notebooks/M09_P03_Future_Scenario_Stress_Test.ipynb
```

## Parte A — Baseline

Resume la arquitectura actual con quality, latency, cost/task, energy index, citation validity y authorization.

## Parte B — Escenarios

Analiza los 8 escenarios. Para cada uno responde:

```text
impact
decision
architecture_change
eval_needed
risk_change
owner
trigger / deadline
```

## Parte C — Decisión

Utiliza cuando proceda:

```text
KEEP
ADOPT
TRIAL
WATCH
REJECT
RETIRE
```

No tienes que seleccionar las opciones sugeridas en el JSON.

## Parte D — Scenario Matrix

Construye una matriz:

```text
scenario
→ affected components
→ resilience
→ action
```

## Parte E — Stress score

Define una escala 1–5 para adaptability, vendor portability, regulatory readiness, cost resilience y operational resilience.

## Parte F — Top 3 improvements

Selecciona las tres mejoras que aumentarían más la capacidad de adaptación. Pueden ser `portable eval set`, `model registry`, `feature flags` o `exit plan`.

## Preguntas

1. ¿Qué escenario exige actuar aunque no cambie el modelo?
2. ¿Qué escenario no justifica una migración inmediata?
3. ¿Cuál muestra mejor el valor de un eval set portable?
4. ¿Qué mejora de arquitectura ofrece opcionalidad sin sobrearquitectura?
