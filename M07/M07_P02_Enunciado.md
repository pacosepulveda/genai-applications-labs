# M07.P02 — Baseline, target y scorecard

**Modalidad:** individual o equipos pequeños  
**Entregable:** baseline calculado, objetivo de piloto y scorecard

## Objetivo

Construirás el sistema de medida **antes** de afirmar que la IA aporta valor.

## Material

```text
assets/baseline_procedure_search.csv
notebooks/M07_P02_Baseline_Metrics.ipynb
```

## Parte A — Baseline

Calcula:

- media;
- mediana;
- p90;
- tasa de documento incorrecto;
- tasa de escalado a experto.

Comprueba que el dataset reproduce aproximadamente el baseline del caso:

```text
11 min de mediana
6% documento incorrecto
18% escalado a experto
```

## Parte B — Target

Define un piloto de 8 semanas cuyo objetivo principal sea:

```text
reducir al menos un 30% el tiempo mediano
```

sin empeorar calidad ni seguridad.

## Parte C — Scorecard

Define al menos una métrica por capa:

```text
MODEL
SYSTEM
USER
BUSINESS
```

## Parte D — Counter-metrics

Incluye, como mínimo:

- documento o fuente incorrecta;
- retrieval no autorizado;
- escalado a experto;
- retrabajo.

## Parte E — Diseño de comparación

Explica cómo compararías:

```text
proceso actual
vs
asistente read-only
```

evitando medir únicamente percepción.

## Preguntas

1. ¿Por qué usar mediana además de media?
2. ¿Por qué `número de prompts` no es una North Star útil?
3. ¿Qué decisión tomarías si el tiempo baja un 40% pero aumentan los errores?
4. ¿Qué métrica de negocio conectaría mejor el piloto con capacidad operativa?
