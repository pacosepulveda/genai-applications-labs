# M07.P02 — Baseline, objetivos SMART y métricas que importan

**Modalidad:** individual o equipos pequeños  
**Entregable:** baseline calculada, objetivo SMART y scorecard de métricas

## Objetivo

Construirás el sistema de medida **antes** de afirmar que la IA mejora algo.

## Dataset

```text
assets/baseline_procedure_search.csv
```

Cada fila representa una búsqueda manual de un procedimiento.

## Tareas

Abre:

```text
notebooks/M07_P02_SMART_Metrics.ipynb
```

### Parte A — Baseline

Calcula:

- media de tiempo;
- mediana;
- p90;
- tasa de documento incorrecto;
- tasa de escalado a experto.

### Parte B — North Star Metric

Elige una métrica principal.

Justifica por qué:

```text
número de prompts
```

no sería adecuada como North Star.

### Parte C — Objetivo SMART

Formula un objetivo para un piloto.

Debe contener:

```text
usuario
baseline
target
counter-metric
periodo
```

### Parte D — Cuatro capas

Define métricas:

```text
MODEL
SYSTEM
USER
BUSINESS
```

Incluye al menos dos por capa.

### Parte E — Counter-metrics

Si optimizamos tiempo, añade controles para evitar:

- respuestas incorrectas;
- uso de fuente obsoleta;
- retrieval no autorizado;
- escalado innecesario.

### Parte F — Diseño de experimento

Propón cómo comparar:

```text
proceso actual
vs
asistente
```

Evita medir únicamente percepción.

## Preguntas

1. ¿Por qué utilizarías mediana además de media?
2. ¿Qué diferencia hay entre una métrica técnica y una métrica de negocio?
3. ¿Qué ocurre si el tiempo baja un 40% pero aumenta el uso de documentos incorrectos?
4. ¿Qué dato falta antes de poder calcular ROI real?
