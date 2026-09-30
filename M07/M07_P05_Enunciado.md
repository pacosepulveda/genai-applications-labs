# M07.P05 — Portfolio, TCO, ROI y priorización ajustada por riesgo

**Modalidad:** individual o equipos pequeños  
**Entregable:** ranking explicable, escenarios económicos y recomendación de portfolio

## Objetivo

Priorizarás iniciativas sin confundir un score con una verdad objetiva.

## Dataset

```text
assets/portfolio_candidates.csv
assets/portfolio_weights.json
```

## Tareas

Abre:

```text
notebooks/M07_P05_Portfolio_TCO_ROI.ipynb
```

### Parte A — Score de capacidad

Calcula un score ponderado con:

```text
business_value
strategic_alignment
data_readiness
technical_feasibility
user_readiness
time_to_value
```

Los pesos están en el JSON.

### Parte B — Ajuste por riesgo

Crea una función explícita de penalización.

Ejemplo conceptual:

```text
risk 1 -> 1.00
risk 2 -> 0.90
risk 3 -> 0.75
risk 4 -> 0.55
risk 5 -> 0.30
```

Justifica tus factores.

### Parte C — Beneficio anual

Estima capacidad liberada:

```text
annual_successful_tasks =
monthly_volume * 12 * adoption_rate * success_rate

hours_saved =
annual_successful_tasks * minutes_saved_per_success / 60
```

Valor económico:

```text
hours_saved * loaded_hourly_cost_eur
```

### Parte D — TCO

Incluye:

```text
annual_fixed_cost
+
annual_successful_tasks * variable_cost_per_task
```

Discute qué costes faltan en el fichero:

- integración;
- soporte;
- governance;
- evaluación;
- human review.

### Parte E — ROI

Calcula un ROI simplificado.

Después realiza tres escenarios:

```text
CONSERVATIVE
BASE
OPTIMISTIC
```

variando:

- adoption;
- success rate;
- variable cost.

### Parte F — Portfolio

Selecciona:

```text
2 quick wins
1 capability builder / strategic bet
1 NOT YET
1 NO-GO
```

No elijas automáticamente las cinco puntuaciones más altas.

## Preguntas

1. ¿Qué diferencia hay entre cost/request y cost/task?
2. ¿Qué iniciativa queda peor al ajustar por riesgo?
3. ¿Qué supuesto domina más el ROI?
4. ¿Por qué una iniciativa con ROI negativo inicial podría seguir siendo un capability builder?
