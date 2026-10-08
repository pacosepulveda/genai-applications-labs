# M07.P02 — Tabletop · Evidence & Readiness Committee

**Modalidad:** equipos pequeños  
**Entregable:** scorecard de evidencia, decisión de datos y arquitectura propuesta

## Situación

El comité acepta estudiar el caso del Enterprise GenAI Assistant, pero no autoriza todavía un piloto.

La PoC técnica de M06 funciona. Ahora hay que demostrar que existe un problema medible, que los datos están preparados y que la estrategia técnica encaja con cada necesidad.

## Material

```text
assets/enterprise_genai_assistant_case.md
assets/baseline_procedure_search.csv
assets/prioritization_candidates.csv
assets/data_inventory.csv
templates/M07_P02_Evidence_Readiness.md
```

Los CSV son evidencia para inspeccionar, no datasets que haya que procesar con Python.

---

## Ronda 1 — Baseline antes de prometer valor

Utiliza como baseline del caso transversal:

```text
11 min   mediana de búsqueda del procedimiento
6%       uso de documento incorrecto
18%      escalado a experto
```

Define:

1. una **North Star** del piloto;
2. al menos una métrica `MODEL`;
3. al menos una métrica `SYSTEM`;
4. al menos una métrica `USER`;
5. al menos una métrica `BUSINESS`;
6. tres counter-metrics que impidan declarar éxito a costa de calidad, seguridad o retrabajo.

El objetivo inicial del sponsor es:

```text
reducir >= 30% el tiempo mediano de búsqueda
```

Decide qué condiciones adicionales deben cumplirse para que esa reducción pueda considerarse éxito.

## Ronda 2 — Priorizar no es ordenar una hoja de cálculo

Revisa `prioritization_candidates.csv`.

Debes asignar una de estas decisiones de portfolio:

```text
QUICK_WIN
STRATEGIC_BET
NOT_YET
NO_GO
```

No conviertas el score en una decisión automática.

Para cada decisión explica qué pesa más entre:

```text
business value
technical feasibility
data readiness
risk
time-to-value
```

Selecciona al menos un caso cuyo valor parezca alto pero que **no deba ser prioritario todavía**.

## Ronda 3 — Data readiness

Revisa `data_inventory.csv` desde la perspectiva de un piloto **read-only** del Enterprise GenAI Assistant.

Clasifica cada fuente que consideres relevante como:

```text
REQUIRED
OPTIONAL
OUT_OF_SCOPE
```

Para las fuentes `REQUIRED`, responde:

- ¿el owner está claro?;
- ¿la calidad es suficiente?;
- ¿los permisos están definidos?;
- ¿la freshness encaja con la tarea?;
- ¿la fuente es trazable?;
- ¿puede operarse de forma repetible?;

Asigna finalmente:

```text
READY
NEEDS_WORK
```

Para cada `NEEDS_WORK`, define:

```text
gap
action
owner
evidence_of_completion
```

## Ronda 4 — Nueva evidencia

Antes de cerrar la decisión, el comité confirma lo siguiente:

> La colección de procedimientos operativos contiene versiones duplicadas y metadata incompleta en parte del corpus. El histórico de procedimientos retirados debe conservarse para auditoría, pero no debe entrar por defecto en el contexto operativo. El chat interno contiene PII y secretos ocasionales y no tiene una política de retención suficientemente definida.

Revisa tu selección de datos.

Debes indicar qué fuentes:

```text
entran en el piloto
entran después de remediación
quedan fuera
```

## Ronda 5 — Elegir la estrategia técnica

Decide la opción principal para cada necesidad:

```text
PROMPTING
RAG
FINE_TUNING
DETERMINISTIC
TOOL_API
```

Casos a decidir:

1. conocimiento de procedimientos que cambia con el tiempo;
2. estilo de redacción corporativo;
3. estado actual de un incidente;
4. comprobación de permisos;
5. resumen de tickets largos.

La justificación debe explicar **qué queremos cambiar o recuperar**, no qué tecnología parece más sofisticada.

## Gate de la práctica

Con la evidencia disponible, decide para el caso principal:

```text
READY_FOR_PILOT_DESIGN
NOT_YET
NO_GO
```

Si eliges `NOT_YET`, enumera exactamente qué evidencias faltan.

## Resultado esperado

El comité debe poder reconstruir esta cadena:

```text
baseline
→ target
→ métricas
→ datos necesarios
→ readiness
→ estrategia técnica
→ decisión
```

La decisión no debe depender de haber ejecutado código, sino de la calidad de la evidencia y de los supuestos declarados.
