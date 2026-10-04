# M07.P01 — De pain point a caso de uso defendible

**Modalidad:** individual o equipos pequeños  
**Entregable:** backlog clasificado, descomposición de un proceso y una Use Case Card

## Objetivo

Partirás de fricciones observables y decidirás qué tecnología encaja con cada tarea.

## Material

```text
assets/opportunity_backlog.csv
notebooks/M07_P01_Opportunity_Discovery.ipynb
```

## Parte A — Fricción

Calcula:

```text
monthly_hours_of_friction =
monthly_volume * avg_minutes_per_case / 60
```

Este valor describe volumen de fricción; **no equivale automáticamente a ahorro**.

## Parte B — Fit

Clasifica cada caso como:

```text
GOOD_GENAI_FIT
HYBRID
BETTER_DETERMINISTIC
HIGH_RISK_REVIEW
```

Justifica la decisión utilizando:

- tipo de tarea;
- tolerancia al error;
- necesidad de exactitud;
- impacto de la decisión.

## Parte C — Alternativa

Para cada caso indica una alternativa razonable:

```text
RULES
SEARCH
WORKFLOW
CLASSIC_ML
GENAI
RAG
HYBRID
```

## Parte D — Process decomposition

Elige un proceso y divídelo en tareas.

Para cada tarea marca:

```text
DETERMINISTIC
AI_ASSISTED
HUMAN_DECISION
```

y un nivel de autonomía `L1..L4`.

## Parte E — Use Case Card

Completa una única ficha con:

```text
user
problem
task
current_process
baseline_needed
proposed_capability
alternative_without_genai
required_data
main_risk
owner
success_criterion
```

## Parte F — Decisión negativa

Selecciona una oportunidad que **no avanzarías** y explica por qué.

## Preguntas

1. ¿Qué diferencia hay entre problema y solución?
2. ¿Qué casos intentan sustituir una regla conocida por comportamiento probabilístico?
3. ¿Qué caso tiene alto volumen pero riesgo relativamente bajo?
4. ¿Qué evidencia te haría cambiar una decisión negativa?
