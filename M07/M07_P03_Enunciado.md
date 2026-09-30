# M07.P03 — Data Readiness y gobernanza de datos

**Modalidad:** individual o equipos pequeños  
**Entregable:** inventario enriquecido, nivel de readiness y plan de preparación

## Objetivo

Determinarás si los datos están realmente preparados para soportar un caso de IA.

## Dataset

```text
assets/data_inventory.csv
```

## Tareas

Abre:

```text
notebooks/M07_P03_Data_Readiness.ipynb
```

### Parte A — Inventario

Revisa para cada dataset:

```text
owner
classification
intended_use
freshness
quality
issues
```

### Parte B — Readiness D0–D5

Utiliza:

```text
D0 unknown
D1 inventoried
D2 accessible
D3 curated/metadata
D4 evaluated for use case
D5 operationalized/monitored
```

Revisa críticamente el valor inicial del fichero y modifícalo si procede.

### Parte C — Requirements

Para Enterprise GenAI Assistant, clasifica cada dataset como:

```text
REQUIRED
OPTIONAL
OUT_OF_SCOPE
```

### Parte D — Gap analysis

Para cada dataset `REQUIRED` que no esté en D4 o D5, define:

```text
gap
action
owner
evidence_of_completion
```

### Parte E — RAG vs fine-tuning

Para los siguientes problemas decide:

```text
PROMPTING
RAG
FINE_TUNING
DETERMINISTIC
TOOL/API
```

Casos:

- conocimiento de procedimientos que cambia;
- estilo de redacción corporativo;
- consulta de estado actual de un incidente;
- comprobación de permisos;
- resumen de tickets.

### Parte F — Minimización

Identifica datos que **no deberían incorporarse por defecto** al sistema.

## Preguntas

1. ¿Por qué un dataset grande puede estar en D1?
2. ¿Qué diferencia hay entre estar accesible y estar preparado?
3. ¿Por qué los chats históricos requieren especial cuidado?
4. ¿Qué datos deben venir de una tool en tiempo real y no del RAG?
