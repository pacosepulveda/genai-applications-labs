# M08.P03 — Operating Model, Team Topology y RACI

**Modalidad:** equipos pequeños  
**Entregable:** modelo organizativo, RACI validada y decision-rights map

## Objetivo

Diseñar una organización que pueda entregar sin convertir Platform, Security o Governance en bottlenecks.

## Material

```text
assets/operating_activities.csv
assets/organization_scenarios.json
```

## Tareas

Abre:

```text
notebooks/M08_P03_Operating_Model_RACI.ipynb
```

### Parte A — Topology

Para cada escenario organizativo selecciona:

```text
CENTRALIZED
FEDERATED
HUB_AND_SPOKE
```

Justifica.

### Parte B — Enterprise GenAI Assistant

Diseña:

```text
Product Squad
AI Platform
Governance/Risk/Enablement
```

y asigna responsabilidades.

### Parte C — RACI

Para cada actividad A01–A15 asigna:

```text
R
A
C
I
```

Roles disponibles:

```text
Product
AI Engineering
Data/Knowledge
AI Platform
Security
Risk/Legal
Domain SME
Service Owner
```

### Parte D — Validación automática

Implementa reglas:

1. exactamente un `A`;
2. al menos un `R`;
3. no más de tres `R`;
4. `A` no puede estar vacío.

Genera una lista de violaciones.

### Parte E — Decision rights

Para actividades críticas especifica además:

```text
can_approve
can_block
can_rollback
```

## Preguntas

1. ¿Por qué un RACI con cinco Accountable no sirve?
2. ¿Qué debería centralizar AI Platform?
3. ¿Qué debe permanecer en el product squad?
4. ¿Qué tipos de cambios necesitan Risk/Security y cuáles pueden ir por fast lane?
