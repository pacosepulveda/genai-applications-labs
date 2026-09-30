# M09.P01 — Technology Radar: ADOPT, TRIAL, WATCH, REJECT

**Modalidad:** equipos pequeños  
**Entregable:** Technology Radar razonado

## Objetivo

Evaluar tecnologías emergentes sin confundir:

```text
new
=
better
```

## Material

```text
assets/technology_radar_candidates.csv
templates/technology_radar_template.md
```

Abre:

```text
notebooks/M09_P01_Technology_Radar.ipynb
```

## Parte A — Revisar el radar inicial

El dataset contiene tecnologías de multimodalidad, agents, MCP/interoperabilidad, Edge AI, model architectures, long context, adaptive routing, memory y hardware.

La columna `reference_horizon` es solo un punto de partida. Puedes cambiarla.

## Parte B — Score

Construye una puntuación usando:

```text
business_value
technical_maturity
strategic_relevance
```

y penalizando:

```text
risk
switching_cost
operational_complexity
```

Los pesos deben ser explícitos.

## Parte C — Decisión

Para cada tecnología selecciona:

```text
ADOPT
TRIAL
WATCH
REJECT
RETIRE
```

No conviertas el score en una decisión automática.

## Parte D — Revisit trigger

Para cada `WATCH`, define qué evidencia haría que pasara a `TRIAL`.

Ejemplos:

```text
GA del proveedor
quality threshold
cost reduction
security control available
```

## Parte E — Portfolio

Comprueba que no has creado un radar lleno de `ADOPT`. Un radar sano también contiene `WATCH` y `REJECT`.

## Preguntas

1. ¿Qué diferencia existe entre `NOW` y `ADOPT`?
2. ¿Qué tecnologías tienen alta madurez pero bajo valor para nuestro caso?
3. ¿Qué tecnología tiene valor alto pero riesgo/operación excesivos?
4. ¿Por qué un benchmark o anuncio no es evidencia suficiente?
