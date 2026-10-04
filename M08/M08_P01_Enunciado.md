# M08.P01 — Capabilities, ownership y decision rights

**Modalidad:** individual o equipos pequeños  
**Entregable:** ownership map y decision-rights map

## Objetivo

Convertirás el equipo conceptual del módulo en responsabilidades operables para
Enterprise GenAI Assistant.

No empezarás por títulos. Empezarás por:

```text
capability
owner
decision
```

## Material

```text
assets/ownership_activities.csv
notebooks/M08_P01_Capabilities_Ownership.ipynb
```

## Parte A — Capabilities

Para cada actividad identifica la capability principal:

```text
PRODUCT
AI_SOFTWARE
DATA_KNOWLEDGE
DOMAIN_SME
PLATFORM
SECURITY_RISK
SERVICE_OPERATIONS
```

## Parte B — Ownership

Asigna un owner concreto.

Evita:

```text
AI Team
IT
The business
```

como propietarios genéricos.

## Parte C — Decision rights

Para cada actividad decide quién puede:

```text
APPROVE
BLOCK
ROLLBACK
```

No todas las actividades necesitan las tres decisiones.

## Parte D — Interfaces

Identifica qué actividades requieren colaboración entre:

```text
Product Squad
AI Platform
Security/Risk
Operations
```

## Parte E — Validación

Comprueba automáticamente que:

1. toda actividad tiene un owner;
2. todo cambio productivo tiene `APPROVE`;
3. toda actividad que puede romper producción tiene `ROLLBACK`;
4. la aceptación de riesgo no queda en AI/Software.

## Preguntas

1. ¿Qué diferencia hay entre capability y job title?
2. ¿Por qué ownership compartido no debe convertirse en ownership difuso?
3. ¿Quién debería poder bloquear un cambio de alto riesgo?
4. ¿Quién debería poder ordenar un rollback durante un incidente?
