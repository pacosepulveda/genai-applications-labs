# M09.P01 — Technology Radar & Adoption Board

**Modalidad:** equipos pequeños  
**Entregable:** `M09_P01_Technology_Radar_Board.md`

## Objetivo

Convertir señales tecnológicas en hipótesis revisables y decisiones explícitas.

No se trata de elegir la tecnología más novedosa. Se trata de responder:

```text
¿qué capability aporta?
¿qué use case mejora?
¿qué evidencia tenemos?
¿qué riesgo y complejidad añade?
¿merece cambiar el roadmap?
```

## Material

```text
assets/technology_radar_candidates.csv
templates/M09_P01_Technology_Radar_Board.md
```

## Situación

Formas parte del Architecture & Product Board de Enterprise GenAI Assistant.

El producto ya tiene una arquitectura estable. El board revisa tecnologías que podrían ampliar capacidades, reducir coste o aumentar autonomía.

Tu trabajo no es aprobarlas todas. Tu trabajo es evitar dos errores:

```text
perseguir cada novedad
ignorar una capability que sí cambia el producto
```

## Parte A — Radar inicial

Para cada candidato revisa:

```text
business_value
technical_maturity
strategic_relevance
evidence_strength
risk
operational_complexity
switching_cost
reference_horizon
```

Asigna una posición propia:

```text
NOW
NEXT
WATCH
```

Puedes discrepar del `reference_horizon`, pero debes justificarlo.

## Parte B — De radar a lifecycle

Ahora toma una decisión distinta del horizonte:

```text
ADOPT
TRIAL
WATCH
REJECT
```

El radar expresa madurez relativa.

La decisión expresa qué debe hacer **nuestro producto**.

Por ejemplo, una tecnología puede estar en `NOW` y aun así ser `REJECT` para este caso de uso.

## Parte C — Evidence gap

Para cada candidato que marques como `TRIAL`, define el experimento mínimo que permitiría tomar una decisión posterior.

Incluye:

```text
hypothesis
workload
eval_set
success_threshold
cost_limit
risk_check
exit_condition
```

No aceptes como evidencia suficiente:

```text
vendor demo
benchmark genérico
popularidad
```

## Inyecto 1 — El benchmark espectacular

Un proveedor publica un benchmark donde un nuevo agent runtime consigue un 35 % más de tareas completadas que su versión anterior.

No se proporciona:

- distribución de tipos de tarea;
- número de tool calls;
- coste por tarea;
- tasa de acciones incorrectas;
- resultados sobre vuestro eval set.

El sponsor pide mover `Durable agent runtime` directamente a `ADOPT`.

Decide:

```text
ACCEPT
TRIAL_FIRST
KEEP_WATCHING
REJECT_FOR_NOW
```

Documenta qué evidencia falta.

## Inyecto 2 — Una capability sí resuelve un problema real

Operations informa de que el 28 % de los procedimientos críticos incluyen diagramas y tablas cuya semántica se pierde al convertirlos a texto plano.

El candidato `Multimodal document understanding` ya estaba en el radar.

Revisa:

- su horizonte;
- su lifecycle decision;
- qué eval específico necesitas;
- qué nueva superficie de ataque debes contemplar.

## Parte D — Cadencia del radar

Define una política simple:

```text
watchlist frecuente
radar periódico
major release -> eval candidate
```

Indica quién puede mover un elemento de `WATCH` a `TRIAL` y qué evidencia debe acompañar el cambio.

## Debrief

1. ¿Por qué `NOW` no significa automáticamente `ADOPT`?
2. ¿Qué diferencia hay entre una señal externa y evidencia interna?
3. ¿Qué candidato tiene mayor riesgo de hype en este caso?
4. ¿Qué tecnología merece un trial aunque todavía no sea una decisión de producción?
5. ¿Qué condición haría retirar una tecnología que hoy está adoptada?
