# M07.P06 — Enterprise GenAI Assistant v0.7: Stage Gate y piloto

**Modalidad:** equipos pequeños  
**Entregable:** Decision Pack y defensa de la decisión

## Objetivo

Cerrarás M07 decidiendo si la PoC técnica de M06 debe pasar a un piloto controlado.

## Material

```text
assets/enterprise_genai_assistant_case.md
assets/baseline_procedure_search.csv
assets/data_inventory.csv
assets/risk_scenarios.jsonl
notebooks/M07_P06_Stage_Gate_Pilot.ipynb
```

## Parte A — Gate actual

Supón que M06 ha demostrado viabilidad técnica.

Estás en:

```text
PoC -> Pilot
```

Evalúa:

- valor;
- baseline y métricas;
- datos;
- riesgo;
- capacidad operativa;
- ownership.

## Parte B — Decisiones por capacidad

Toma una decisión distinta:

```text
GO
NOT_YET
NO_GO
```

para:

1. RAG read-only con citas;
2. consulta read-only de incidentes;
3. agente que propone acciones;
4. agente que ejecuta cambios;
5. aprobación automática de accesos privilegiados.

## Parte C — Piloto

El alcance candidato es:

```text
20 técnicos
1 departamento
5 procedimientos
read-only
8 semanas
```

## Parte D — Success y stop criteria

Incluye:

```text
time_saved >= 30%
citation_validity >= 98%
satisfaction >= 4/5
```

y detén/replantea si ocurre:

```text
retrieval_miss > 15%
critical_hallucination
security_blocker
```

## Parte E — Roadmap

Construye únicamente las fases explicadas en el deck:

```text
Discovery
Feasibility
PoC
Pilot
Production
```

Para cada una añade:

```text
learning_goal
evidence
gate
owner
```

## Parte F — Decision Pack

Genera:

```text
M07_Decision_Pack.md
```

con:

```text
Executive summary
Decisions
Evidence
Metrics
Data readiness
Top risks
Pilot scope
Stop criteria
Roadmap
Open dependencies
```

## Preguntas finales

1. ¿Qué evidencias justifican pasar a piloto?
2. ¿Qué capacidades quedan en `NOT_YET`?
3. ¿Qué condición produciría un `NO_GO` inmediato?
4. ¿Qué debe demostrar el piloto antes de producción?
5. ¿Qué ownership queda por resolver en M08?
