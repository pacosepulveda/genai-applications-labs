# M09.P04 — Enterprise GenAI Assistant v1.0: Architecture Evolution Decision Pack

**Modalidad:** equipos pequeños  
**Entregable:** `Architecture_Evolution_Decision_Pack.md`

## Objetivo

Cerrar el proyecto transversal con **la siguiente arquitectura defendible**.

No hay que activar todas las tendencias del módulo.

## Material

```text
assets/enterprise_genai_assistant_v10_case.md
assets/v10_component_candidates.csv
templates/architecture_evolution_decision_pack.md
notebooks/M09_P04_Capstone_v10.ipynb
```

Además reutiliza P01–P03.

## Parte A — Component decisions

Para cada componente decide:

```text
KEEP
TRIAL
WATCH
REJECT
RETIRE
```

Incluye:

```text
why
evidence_needed
revisit_trigger
```

## Parte B — Target architecture

Diseña únicamente las rutas necesarias:

```text
intake
identity / policy
task router
edge / cloud
RAG
bounded agent runtime
tools
human gates
```

Transversalmente deben existir:

```text
evals
observability
cost
security
audit
```

## Parte C — Eval-first migration

Elige un cambio candidato y define:

```text
candidate
same eval set
comparison
gate
decision
rollback
```

## Parte D — Human + AI

Identifica una tarea para:

```text
AUGMENT
AUTOMATE_WITH_LIMITS
HUMAN_DECISION
```

La supervisión debe poder intervenir realmente.

## Parte E — Optionality / exit

Selecciona qué activos deben mantenerse portables:

```text
data
prompts
evals
interfaces
routing policy
```

Describe cómo cambiarías un proveedor o backend sin reconstruir el producto.

## Parte F — Lifecycle roadmap

Resume:

```text
ADOPT / KEEP NOW
TRIAL NEXT
WATCH
REJECT
RETIRE
```

## Parte G — Final Decision Pack

Genera:

```text
Architecture_Evolution_Decision_Pack.md
```

con:

```text
Executive summary
Component decisions
Target architecture
Routing policy
Eval-first migration
Human gates
Constraints
Portable assets
Exit plan
Technology lifecycle
```

## Preguntas finales

1. ¿Qué parte de M01–M08 conservarías intacta?
2. ¿Qué tendencia aporta valor inmediato?
3. ¿Qué mantendrías en WATCH?
4. ¿Qué activo reduce más el switching cost futuro?
5. ¿Qué significa una arquitectura preparada para cambiar?
