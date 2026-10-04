# M07.P05 — Risk register y plan de fallo seguro

**Modalidad:** equipos pequeños  
**Entregable:** registro de riesgos con controles, riesgo residual y plan de resiliencia

## Objetivo

Convertirás escenarios de fallo en decisiones controlables.

## Material

```text
assets/risk_scenarios.jsonl
notebooks/M07_P05_Risk_Resilience.ipynb
```

## Parte A — Riesgo inherente

Revisa:

```text
likelihood 1..5
impact 1..5
inherent_score = likelihood * impact
```

La puntuación ayuda a comparar; no expresa precisión científica.

## Parte B — Controles

Para cada riesgo propone controles concretos.

Ejemplo:

```text
riesgo:
fuente obsoleta

control:
status=CURRENT antes de construir contexto
```

## Parte C — Riesgo residual

Tras aplicar controles estima de nuevo:

```text
residual_likelihood
residual_impact
residual_score
risk_owner
```

## Parte D — Human oversight

Decide un patrón para distintas capacidades:

```text
NO_HUMAN_GATE
REVIEW_BEFORE_USE
APPROVAL_BEFORE_ACTION
OUT_OF_SCOPE
```

La revisión humana debe especificar qué información recibe la persona y si puede bloquear.

## Parte E — Resilience

Para los riesgos prioritarios define:

```text
OBSERVE
DEGRADE
STOP
RECOVER
```

Incluye al menos un kill switch o revocación de capacidad.

## Parte F — Constraints

Marca los escenarios que requieren revisión especializada de seguridad,
privacidad, legal o proveedor. No realices una clasificación jurídica definitiva.

## Preguntas

1. ¿Qué diferencia existe entre riesgo inherente y residual?
2. ¿Por qué autorización no debe delegarse al LLM?
3. ¿Qué riesgo aumenta al pasar de recomendación a ejecución?
4. ¿Cuándo utilizarías degradación en lugar de apagar todo el servicio?
