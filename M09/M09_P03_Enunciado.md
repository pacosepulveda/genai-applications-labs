# M09.P03 — Future Scenario Stress Test

**Modalidad:** equipos pequeños  
**Entregable:** Architecture Resilience Report

## Objetivo

Comprobar si la arquitectura sigue siendo defendible en varios futuros sin
intentar acertar un único forecast.

## Material

```text
assets/future_scenarios.json
assets/current_architecture_metrics.csv
notebooks/M09_P03_Future_Scenario_Stress_Test.ipynb
```

## Parte A — Baseline

Resume el estado actual:

```text
quality
latency
cost/task
energy_index
citation_validity
authorization
```

## Parte B — Cuatro futuros

Analiza:

```text
CLOUD_ACCELERATES
EDGE_ACCELERATES
REGULATION_INCREASES
COST_ENERGY_CONSTRAINS
```

Para cada uno documenta:

```text
affected_components
what_stays
what_changes
eval_needed
risk_change
owner
```

## Parte C — Decisión

Utiliza cuando proceda:

```text
KEEP
TRIAL
WATCH
REJECT
RETIRE
```

## Parte D — Resilience score

Puntúa de 1 a 5:

```text
adaptability
vendor_portability
regulatory_readiness
cost_resilience
```

## Parte E — Top 3 improvements

Selecciona solo tres mejoras que aumenten más la opcionalidad.

Ejemplos:

```text
portable eval set
feature flags
policy-as-code
documented provider interface
versioned routing policy
exit plan
```

No sobrearquitectes.

## Preguntas

1. ¿Qué escenario exige actuar aunque el modelo no cambie?
2. ¿Cuál no justifica una migración inmediata?
3. ¿Qué activo hace más barata una futura comparación?
4. ¿Qué abstracción estratégica merece conservarse?
