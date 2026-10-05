# M09.P01 — Technology Radar: señal, evidencia y decisión

**Modalidad:** equipos pequeños  
**Entregable:** Technology Radar razonado

## Objetivo

Separar dos preguntas diferentes:

```text
¿qué madurez tiene esta capability?
```

y:

```text
¿qué decisión debemos tomar nosotros?
```

## Material

```text
assets/technology_radar_candidates.csv
templates/technology_radar_template.md
notebooks/M09_P01_Technology_Radar.ipynb
```

## Parte A — Horizon

Clasifica cada candidato:

```text
NOW
NEXT
WATCH
```

`NOW` no significa automáticamente `ADOPT`.

## Parte B — Filtro común

Para cada candidato analiza:

```text
capability
use case
evidence
risk / operations
```

Construye una puntuación orientativa con:

```text
business_value
technical_maturity
strategic_relevance
evidence_strength
```

y penaliza:

```text
risk
operational_complexity
switching_cost
```

Los pesos deben ser explícitos.

## Parte C — Decisión de lifecycle

Selecciona:

```text
ADOPT
TRIAL
WATCH
REJECT
RETIRE
```

El score ayuda a discutir. No decide automáticamente.

## Parte D — Internal eval

Para cada `TRIAL`, define qué prueba ejecutarías sobre nuestro workload:

```text
quality
cost/task
latency
risk
```

## Parte E — Revisit trigger

Para cada `WATCH` o `REJECT`, define qué evidencia obligaría a revisar la decisión.

## Preguntas

1. ¿Por qué `NOW` y `ADOPT` no son sinónimos?
2. ¿Qué candidato parece maduro pero aporta poco valor al caso?
3. ¿Cuál tiene valor potencial alto pero evidencia insuficiente?
4. ¿Por qué un benchmark externo solo selecciona candidatos?
