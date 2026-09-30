# M07.P04 — Risk Register, AI RMF y human oversight

**Modalidad:** equipos pequeños  
**Entregable:** registro de riesgos con controles, riesgo residual y ownership

## Objetivo

Convertirás riesgos genéricos en decisiones controlables.

## Dataset

```text
assets/risk_scenarios.jsonl
```

## Tareas

Abre:

```text
notebooks/M07_P04_Risk_Governance.ipynb
```

### Parte A — Inherent risk

Para cada riesgo revisa:

```text
likelihood 1..5
impact 1..5
```

Calcula:

```text
inherent_score = likelihood * impact
```

No interpretes el número como precisión científica.

### Parte B — Controles

Propón controles concretos.

Ejemplo:

```text
riesgo:
documento obsoleto

control:
status=CURRENT before retrieval
```

Evita controles vagos como:

```text
"usar IA responsable"
```

### Parte C — Residual risk

Tras controles estima nuevamente:

```text
likelihood
impact
residual_score
```

y asigna:

```text
risk_owner
```

### Parte D — NIST AI RMF

Mapea las actividades principales a:

```text
GOVERN
MAP
MEASURE
MANAGE
```

Una acción puede contribuir a más de una función.

### Parte E — Human oversight

Para estas capacidades decide un patrón:

```text
NO_HUMAN_GATE
REVIEW_BEFORE_USE
APPROVAL_BEFORE_ACTION
OUT_OF_SCOPE
```

Capacidades:

- resumen interno;
- respuesta RAG con fuentes;
- recomendación de cambio;
- aplicar cambio en producción;
- aprobación de acceso privilegiado.

### Parte F — Regulatory / legal review

Identifica qué casos necesitan:

```text
legal_review_required = true
```

No intentes realizar por tu cuenta una clasificación jurídica definitiva.

## Preguntas

1. ¿Qué diferencia existe entre riesgo inherente y residual?
2. ¿Por qué el LLM no puede ser el control de autorización?
3. ¿Qué riesgo aumenta al pasar de recomendación a ejecución autónoma?
4. ¿Por qué human-in-the-loop mal diseñado puede convertirse en rubber-stamping?
