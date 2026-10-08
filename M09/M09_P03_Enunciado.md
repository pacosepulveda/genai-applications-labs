# M09.P03 — Future Scenario Stress Test & Lifecycle Board

**Modalidad:** equipos pequeños  
**Entregable:** `M09_P03_Architecture_Evolution_Pack.md`

## Objetivo

Comprobar si una arquitectura sigue siendo razonable cuando cambia el entorno y cerrar el curso con decisiones explícitas de lifecycle.

No buscamos acertar un único futuro.

Buscamos una estrategia que pueda adaptarse sin reconstruir el producto cada vez que aparezca un nuevo modelo, runtime o restricción.

## Material

```text
assets/enterprise_genai_assistant_v10_case.md
assets/current_architecture_metrics.csv
assets/future_scenarios.json
assets/v10_component_candidates.csv
assets/technology_radar_candidates.csv
assets/model_capabilities.csv
assets/adaptive_routing_requests.csv
templates/M09_P03_Architecture_Evolution_Pack.md
```

## Situación inicial

Enterprise GenAI Assistant ya dispone de un baseline operativo descrito en el caso.

Las métricas actuales son el punto de comparación:

```text
quality
p95_latency_s
cost_per_task_eur
energy_index
citation_validity
authorization_pass_rate
```

No supongas que una arquitectura nueva es mejor solo porque utiliza tecnología más reciente.

## Parte A — Stress test de cuatro futuros

Evalúa los escenarios:

```text
CLOUD_ACCELERATES
EDGE_ACCELERATES
REGULATION_INCREASES
COST_ENERGY_CONSTRAINS
```

Para cada uno responde:

```text
what_breaks
what_becomes_more_valuable
what_should_remain_portable
new_evidence_needed
architecture_response
```

La misma decisión no tiene por qué ser óptima en los cuatro escenarios.

## Parte B — Architecture runway

Identifica qué inversiones mantienen opciones abiertas en varios futuros.

Considera:

```text
portable eval suite
provider interface
routing policy
versioned prompts
versioned indexes
tool contracts
audit evidence
```

Clasifica cada inversión:

```text
KEEP
BUILD_NOW
BUILD_WHEN_TRIGGERED
AVOID_OVERENGINEERING
```

## Inyecto 1 — Major model release

Aparece un nuevo proveedor/modelo que anuncia:

```text
+12 % quality en benchmark externo
-35 % coste/token
2x context window
```

No hay todavía resultados sobre vuestro workload, retrieval, authorization ni tool use.

El sponsor propone migrar el 100 % del tráfico la semana siguiente.

Define el proceso `eval-first migration`:

```text
candidate
→ same eval suite
→ compare quality/cost/latency/risk
→ limited rollout
→ decision
```

Decide qué evidencia bloquearía la migración aunque el benchmark externo sea mejor.

## Inyecto 2 — Restricción simultánea

Dos semanas después ocurre lo siguiente:

- el presupuesto operativo debe reducirse un 25 %;
- las tareas de alto impacto requieren evidencia de revisión humana;
- aumenta el volumen de documentos con diagramas y tablas.

Revisa la arquitectura propuesta.

No puedes resolver las tres presiones simplemente eligiendo "el modelo más potente".

## Parte C — Lifecycle Board v1.0

Revisa `v10_component_candidates.csv`.

Para cada componente decide:

```text
ADOPT
TRIAL
WATCH
REJECT
RETIRE
```

Puedes mantener o cambiar la propuesta inicial del fichero.

Para cada cambio debes indicar:

```text
reason
evidence
owner
next_review_trigger
exit_plan
```

## Parte D — Capstone: arquitectura adaptativa

Diseña el mapa final de v1.0 con estas capas:

```text
INTAKE
text · image · other supported modalities

DECISION
identity · policy · task/capability router · human gate

EXECUTION
edge/SLM · cloud · RAG · tool/agent runtime

TRANSVERSAL
evals · observability · cost · security · audit
```

No necesitas dibujar componentes físicos exhaustivos.

El objetivo es mostrar **qué decisión ocurre antes de qué capacidad**.

## Parte E — Exit plan

Elige dos dependencias estratégicas y responde:

```text
¿Qué tendría que cambiar para abandonar esta tecnología?
¿Qué activos portables necesitaríamos para migrar?
¿Qué coste de switching aceptamos?
¿Cómo demostraríamos que la alternativa es mejor?
```

## Parte F — Decisión final

Resume la estrategia en cinco decisiones:

1. una capability que adoptarías;
2. una que mantendrías en trial;
3. una que dejarías en watch;
4. una que rechazarías por ahora;
5. una dependencia que diseñarías con exit plan desde el principio.

## Debrief final del curso

1. ¿Qué hace que una arquitectura sea adaptable sin convertirse en una capa de abstracción infinita?
2. ¿Por qué la misma eval suite es uno de los activos más importantes para migrar?
3. ¿Qué decisiones tecnológicas deben tener trigger de revisión?
4. ¿Qué componente sería el primero que retirarías si deja de aportar valor medido?
5. ¿Qué criterio del curso debería permanecer aunque cambien todos los modelos disponibles?
