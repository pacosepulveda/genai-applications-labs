# M07.P06 — Enterprise GenAI Assistant v0.7: Stage Gate y roadmap

**Modalidad:** equipos pequeños  
**Entregable:** Decision Pack y defensa de la decisión

## Objetivo

Cerrarás M07 tomando una decisión sobre el proyecto transversal.

No debes responder:

```text
"es una buena idea"
```

Debes elegir:

```text
GO
NO-GO
NOT YET
```

para cada alcance.

## Material

```text
assets/enterprise_genai_assistant_case.md
assets/baseline_procedure_search.csv
assets/data_inventory.csv
assets/risk_scenarios.jsonl
```

Abre:

```text
notebooks/M07_P06_Stage_Gate_Roadmap.ipynb
```

## Parte A — Gate actual

Supón que M06 ha demostrado viabilidad técnica.

Estás en:

```text
Gate 2:
PoC -> Pilot
```

Evalúa:

- valor;
- baseline;
- datos;
- riesgo;
- operación;
- ownership.

### Parte B — Decisiones separadas

Toma una decisión distinta para:

1. **RAG read-only con citas**.
2. **Consulta read-only de incidentes**.
3. **Agente que propone acciones**.
4. **Agente que ejecuta cambios en producción**.
5. **Aprobación automática de accesos privilegiados**.

Una única decisión global no es suficiente.

### Parte C — Pilot hypothesis

Redacta:

```text
We believe...
for...
will improve...
measured by...
```

### Parte D — Pilot scorecard

Define:

- baseline;
- targets;
- counter-metrics;
- guardrails;
- stop criteria.

### Parte E — Pilot scope

Especifica:

```text
usuarios
fuentes
funciones
exclusiones
soporte
rollback
```

### Parte F — Roadmap

Construye:

```text
Discovery
Feasibility
PoC
Pilot
Production
Scale
```

Para cada fase añade:

```text
learning_goal
deliverable
gate
owner
```

### Parte G — Decision record

Genera:

```text
M07_Decision_Pack.md
```

con:

```text
Executive summary
Decision
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

1. ¿Qué evidencias permiten pasar a piloto?
2. ¿Qué capacidades quedan en `NOT YET`?
3. ¿Qué condición produciría un `NO-GO` inmediato?
4. ¿Qué debería demostrar el piloto antes de producción?
5. ¿Qué temas de ownership y organización debemos resolver en M08?
