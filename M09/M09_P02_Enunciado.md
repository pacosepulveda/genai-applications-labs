# M09.P02 — Adaptive Architecture & Human Control

**Modalidad:** equipos pequeños  
**Entregable:** `M09_P02_Adaptive_Architecture_Board.md`

## Objetivo

Diseñar una arquitectura adaptativa que seleccione la **capability mínima suficiente** para cada request sin fingir que todos los backends son equivalentes.

Los principios del ejercicio son:

```text
smallest adequate model
least agency
minimum useful context
human accountability
```

## Material

```text
assets/model_capabilities.csv
assets/adaptive_routing_requests.csv
assets/current_architecture_metrics.csv
templates/M09_P02_Adaptive_Architecture_Board.md
```

## Situación

Enterprise GenAI Assistant puede combinar rutas distintas:

```text
EDGE_SLM
CLOUD_STANDARD
CLOUD_REASONING
CLOUD_MULTIMODAL
RAG
TOOL_API
```

Cada una tiene capacidades, coste, latencia y calidad proxy diferentes.

El objetivo no es elegir una ruta global. El objetivo es definir qué debería ocurrir con cada tipo de petición.

## Parte A — Capability matching

Para cada request `R01–R08`, identifica primero los requisitos no negociables:

```text
modality
privacy
offline_required
authoritative_knowledge
realtime_state
impact
action_required
```

Después asigna una ruta o una composición de rutas.

No elijas por precio antes de comprobar capability y policy.

## Parte B — Regla de routing

Para cada decisión documenta:

```text
selected_route
why_this_route
rejected_alternatives
policy_constraints
expected_cost
expected_latency
human_gate
fallback
```

Si ninguna ruta aislada satisface el caso, diseña una composición explícita.

## Caso crítico — R06

`R06` combina:

```text
complexity=HIGH
privacy=HIGH
realtime_state=TRUE
impact=CRITICAL
action_required=TRUE
```

No respondas automáticamente "agent".

Decide:

- qué componente obtiene estado real;
- qué componente puede razonar;
- qué acción puede proponerse;
- quién autoriza la ejecución;
- qué kill switch debe existir.

Aplica `least agency`.

## Parte C — Long context vs RAG vs reasoning

Para los requests con conocimiento autoritativo o complejidad alta, decide qué mecanismo resuelve realmente el problema:

```text
long context
RAG
reasoning-time compute
```

No los trates como sustitutos equivalentes.

## Parte D — Human + AI

Clasifica cada request como:

```text
AUGMENT
AUTOMATE_BOUNDED
HUMAN_APPROVAL_REQUIRED
HUMAN_ONLY
```

Justifica usando:

```text
impact
reversibility
accountability
reviewability
```

## Inyecto 1 — El cloud reasoning baja de precio

El coste de `CLOUD_REASONING` cae de `0.090 €` a `0.030 €` por tarea y su latencia baja a `1.3 s`.

La calidad proxy no cambia.

Revisa solo las rutas cuya decisión debería cambiar realmente.

Pregunta:

> ¿Una caída de precio justifica enviar por reasoning tareas simples que ya resolvía un backend más pequeño?

## Inyecto 2 — Nueva restricción de privacidad

Security establece que todo request con:

```text
privacy=HIGH
impact>=HIGH
```

debe minimizar exposición de contenido y conservar una ruta de revisión humana si existe una acción sobre sistemas reales.

Revisa `R05`, `R06` y `R08`.

Documenta qué decisiones cambian y cuáles permanecen.

## Parte E — Optionality

Identifica qué interfaces merece la pena mantener portables:

```text
model provider
retrieval
eval suite
routing policy
tool schemas
```

No abstraigas todo.

Para cada abstracción propuesta indica:

```text
strategic_dependency
switching_cost_avoided
complexity_added
```

## Debrief

1. ¿Por qué una interfaz común no significa que todos los modelos sean equivalentes?
2. ¿Dónde aporta valor real un SLM local?
3. ¿Qué requests justifican reasoning adicional?
4. ¿Qué decisiones no debería tomar un agent de forma autónoma?
5. ¿Qué parte de la arquitectura debe seguir siendo portable aunque no cambiemos proveedor hoy?
