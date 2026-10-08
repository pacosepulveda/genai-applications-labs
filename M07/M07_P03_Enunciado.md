# M07.P03 — Tabletop · Pilot Gate Under Pressure

**Modalidad:** equipos pequeños  
**Entregable:** Decision Pack y defensa del gate

## Situación

La PoC de M06 ha demostrado viabilidad técnica y el comité ha aceptado diseñar un piloto controlado.

Tu equipo actúa ahora como comité de gate. Debe decidir qué capacidades pasan al piloto, cuáles esperan y cuáles quedan fuera.

## Material

```text
assets/enterprise_genai_assistant_case.md
assets/risk_scenarios.jsonl
assets/data_inventory.csv
templates/M07_P03_Pilot_Gate.md
```

---

## Ronda 1 — Decidir por capacidad

Evalúa por separado:

1. RAG read-only con citas;
2. consulta read-only de incidentes;
3. agente que propone acciones pero no las ejecuta;
4. agente que ejecuta cambios en producción;
5. aprobación automática de accesos privilegiados.

Para cada capacidad decide:

```text
GO
NOT_YET
NO_GO
```

No existe obligación de dar la misma decisión a todas.

Documenta:

```text
value hypothesis
evidence available
main risk
required control
maximum autonomy
owner
decision
```

## Ronda 2 — Risk register

Revisa `risk_scenarios.jsonl`.

Selecciona los riesgos que consideres materiales para el alcance del piloto.

Para cada uno registra:

```text
inherent likelihood 1..5
inherent impact 1..5
controls
residual likelihood 1..5
residual impact 1..5
risk owner
```

La puntuación sirve para ordenar la conversación; no representa precisión científica.

Incluye para los riesgos prioritarios una respuesta de resiliencia:

```text
OBSERVE
DEGRADE
STOP
RECOVER
```

Debe existir al menos un mecanismo concreto de kill switch, revocación de tool o degradación a un modo más seguro.

## Ronda 3 — Piloto inicial

El alcance propuesto es:

```text
20 técnicos
1 departamento
5 procedimientos aprobados
8 semanas
read-only
```

Criterios de éxito mínimos:

```text
time_saved >= 30%
citation_validity >= 98%
satisfaction >= 4/5
```

Criterios de parada o replanteamiento:

```text
retrieval_miss > 15%
critical_hallucination
security_blocker
```

Decide si estos criterios son suficientes. Puedes añadir counter-metrics, pero no eliminar los controles esenciales sin justificarlo.

## Ronda 4 — Inyecto operacional

Durante una prueba previa al piloto aparecen estos resultados:

```text
time_saved              37%
citation_validity       99.1%
retrieval_miss          12%
satisfaction            4.3/5
critical_hallucinations 0
```

Pero el equipo de seguridad descubre que dos usuarios pudieron recuperar un procedimiento fuera de su ACL debido a un error en el filtrado del índice.

Decide inmediatamente una postura:

```text
CONTINUE
DEGRADE
STOP
```

Después define:

- qué capacidad deshabilitas o limitas;
- qué evidencia necesitas para recuperar el servicio completo;
- quién autoriza la recuperación;
- qué nuevo caso debe añadirse al eval set o a los tests.

## Ronda 5 — Presión de negocio

El sponsor responde:

> “Las métricas son buenas. Añadamos una tool de escritura para que el agente pueda corregir automáticamente cambios simples en producción durante el piloto.”

Decide:

```text
GO
NOT_YET
NO_GO
```

para esta ampliación concreta.

La respuesta debe distinguir entre:

- valor potencial;
- evidencia disponible;
- autonomía;
- blast radius;
- rollback;
- accountability.

## Ronda 6 — Stage Gate final

Construye el roadmap únicamente con estas fases:

```text
Discovery
Feasibility
PoC
Pilot
Production
```

Para cada fase registra:

```text
learning_goal
evidence
gate
owner
```

La decisión final debe ser una de:

```text
GO
NOT_YET
NO_GO
```

para el paso actual `PoC -> Pilot`.

## Decision Pack

Completa la plantilla con:

```text
Executive summary
Capabilities and decisions
Evidence
Metrics and counter-metrics
Data readiness
Top risks and residual risk
Pilot scope
Human oversight
Resilience / kill switch
Success criteria
Stop criteria
Roadmap
Open dependencies
Final gate decision
```

## Defensa final

El equipo debe poder responder:

1. ¿Qué evidencia justifica avanzar?
2. ¿Qué capacidad queda en `NOT_YET` y qué falta exactamente?
3. ¿Qué capacidad recibe `NO_GO` para este alcance?
4. ¿Qué condición obliga a degradar o detener el sistema?
5. ¿Quién acepta el riesgo residual?
6. ¿Qué debe demostrar el piloto antes de Production?

## Resultado esperado

Una buena respuesta no maximiza el número de capacidades aprobadas.

Maximiza la **calidad de la decisión**:

```text
valor demostrado
+ riesgo controlado
+ autonomía proporcional
+ ownership explícito
+ capacidad de parar y recuperar
```
