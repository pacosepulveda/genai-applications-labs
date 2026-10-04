# M07.P03 — Priorización defendible

**Modalidad:** individual o equipos pequeños  
**Entregable:** ranking explicable y cuatro decisiones de portfolio

## Objetivo

Compararás oportunidades sin convertir una puntuación en una verdad matemática.

## Material

```text
assets/prioritization_candidates.csv
notebooks/M07_P03_Prioritization.ipynb
```

## Parte A — Cinco dimensiones

Revisa cada candidato en:

```text
business_value
technical_feasibility
data_readiness
risk
time_to_value
```

Todos los valores usan una escala 1..5.

En `risk`, 5 significa mayor riesgo.

## Parte B — Score transparente

Construye un score sencillo convirtiendo primero:

```text
risk -> risk_safety = 6 - risk
```

y calcula una media de las cinco dimensiones.

El score sirve para ordenar la conversación, no para decidir automáticamente.

## Parte C — Sensibilidad

Cambia el peso de una sola dimensión y comprueba si cambia el ranking.

Documenta qué supuesto ha movido la decisión.

## Parte D — Portfolio

Elige:

```text
1 QUICK_WIN
1 STRATEGIC_BET
1 NOT_YET
1 NO_GO
```

No tienen por qué ser los cuatro scores más extremos.

## Parte E — Evidencia pendiente

Para cada decisión indica:

```text
current_decision
reason
evidence_that_could_change_it
```

## Preguntas

1. ¿Por qué un caso con valor 5 puede no ser prioritario?
2. ¿Qué casos empeoran al considerar riesgo?
3. ¿Qué diferencia hay entre `NOT_YET` y `NO_GO`?
4. ¿Qué dimensión contiene más incertidumbre en tu ranking?
