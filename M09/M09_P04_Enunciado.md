# M09.P04 — Enterprise GenAI Assistant v1.0: Capstone final

**Modalidad:** equipos pequeños  
**Entregable:** `Architecture_Evolution_Decision_Pack.md`

## Objetivo

Cerrar el proyecto transversal integrando lo aprendido de M01 a M09.

No debes diseñar “la arquitectura más futurista”. Debes diseñar **la siguiente arquitectura defendible**.

## Material

```text
assets/enterprise_genai_assistant_v10_case.md
assets/v10_component_candidates.csv
templates/architecture_evolution_decision_pack.md
```

y los resultados de P01–P03.

Abre:

```text
notebooks/M09_P04_Capstone_v10.ipynb
```

## Parte A — Component decisions

Para cada componente decide `KEEP / ADOPT / TRIAL / WATCH / REJECT / RETIRE` e incluye evidencia y condición de revisión.

## Parte B — Target architecture

Debe contemplar, al menos:

```text
multimodal intake
identity / policy
adaptive router
edge / cloud
RAG
agent runtime
tools
human gates
evals
observability
cost / energy
```

No todos los componentes tienen que activarse.

## Parte C — Routing policy

Define decisiones para simple/private/offline, corporate knowledge, multimodal, complex reasoning y agentic tasks.

## Parte D — Agent autonomy

Clasifica capacidades:

```text
READ_ONLY
PROPOSE
APPROVAL_REQUIRED
WRITE_ALLOWED
```

Explica qué condiciones necesitarías antes de permitir `WRITE_ALLOWED`.

## Parte E — Personalization

Decide qué usarías entre role context, preferences, session memory y long-term memory, y qué NO almacenarías.

## Parte F — Migration roadmap

Define:

```text
KEEP NOW
TRIAL NEXT
WATCH LATER
```

con gates claros.

## Parte G — Exit strategy

Explica cómo cambiarías model provider, embedding model, agent framework y vector backend sin reconstruir todo el producto.

## Parte H — Final Decision Pack

Genera `Architecture_Evolution_Decision_Pack.md` con las decisiones, arquitectura, routing, multimodalidad, edge/cloud, autonomía, personalización, evaluación, coste/sostenibilidad, seguridad/regulación, colaboración humano-IA, roadmap y exit/rollback plan.

## Preguntas finales

1. ¿Qué parte de M01–M08 conservarías sin cambios?
2. ¿Qué tendencia aporta más valor inmediato?
3. ¿Qué tendencia mantendrías en WATCH?
4. ¿Qué componente constituye el principal lock-in?
5. ¿Qué activo del curso hace más fácil adoptar futuros modelos?
6. ¿Qué significa para ti una arquitectura preparada para cambiar?
