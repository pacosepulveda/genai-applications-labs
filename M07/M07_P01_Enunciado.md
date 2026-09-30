# M07.P01 — De pain point a caso de uso defendible

**Modalidad:** individual o equipos pequeños  
**Entregable:** portfolio clasificado y tres Use Case Cards

## Objetivo

No empezarás seleccionando un modelo.

Empezarás identificando:

```text
problema
tarea
usuario
alternativas
valor potencial
```

## Dataset

Abre:

```text
assets/opportunity_backlog.csv
```

y el notebook:

```text
notebooks/M07_P01_Opportunity_Discovery.ipynb
```

## Parte A — Analizar tareas

Para cada caso determina:

```text
GOOD_GENAI_FIT
HYBRID
BETTER_DETERMINISTIC
HIGH_RISK_REVIEW
```

Justifica la decisión.

No todo caso de alto valor debe clasificarse como buen candidato para GenAI.

## Parte B — Alternativa no-IA

Para cada iniciativa identifica al menos una alternativa:

- reglas;
- búsqueda;
- workflow;
- ML clásico;
- BI;
- rediseño del proceso.

## Parte C — Volumen de fricción

Calcula:

```text
monthly_hours =
monthly_volume * avg_minutes_per_case / 60
```

No interpretes todo ese tiempo como ahorro potencial.

## Parte D — Process decomposition

Elige un proceso de la lista y divídelo en tareas.

Para cada tarea marca:

```text
DETERMINISTIC
AI_ASSISTED
HUMAN_ONLY
```

## Parte E — Use Case Cards

Selecciona tres iniciativas y completa:

```text
problem
user
job_to_be_done
current_process
proposed_capability
data
baseline_needed
value_hypothesis
risk
owner
```

Una de las tres debe ser un caso que **no recomendarías avanzar**.

## Preguntas

1. ¿Qué diferencia hay entre problema y solución?
2. ¿Qué casos del dataset están intentando sustituir lógica determinista por probabilística?
3. ¿Qué tarea tiene mucho volumen pero no necesariamente mucho riesgo?
4. ¿Qué caso merece un `NOT YET` aunque su valor potencial sea alto?
