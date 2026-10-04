# M07.P04 — Data readiness y estrategia técnica

**Modalidad:** individual o equipos pequeños  
**Entregable:** inventario evaluado, gaps y decisiones de arquitectura

## Objetivo

Determinarás si las fuentes necesarias son utilizables, trazables y operables.

## Material

```text
assets/data_inventory.csv
notebooks/M07_P04_Data_Readiness.ipynb
```

## Parte A — Necesidad

Clasifica cada fuente como:

```text
REQUIRED
OPTIONAL
OUT_OF_SCOPE
```

para el piloto read-only de Enterprise GenAI Assistant.

## Parte B — Readiness

Para cada fuente `REQUIRED`, evalúa:

```text
owner_known
quality_acceptable
permissions_defined
freshness_fit
traceable
operable
```

Después asigna:

```text
READY
NEEDS_WORK
```

## Parte C — Gap plan

Para cada `NEEDS_WORK` define:

```text
gap
action
owner
evidence_of_completion
```

## Parte D — Estrategia técnica

Decide entre:

```text
PROMPTING
RAG
FINE_TUNING
DETERMINISTIC
TOOL_API
```

para:

- conocimiento de procedimientos que cambia;
- estilo de redacción corporativo;
- estado actual de un incidente;
- comprobación de permisos;
- resumen de tickets.

## Parte E — Minimización

Identifica qué datos no deben incorporarse por defecto y por qué.

## Preguntas

1. ¿Qué diferencia existe entre `accessible` y `ready`?
2. ¿Por qué un corpus enorme puede ser peor que uno pequeño y curado?
3. ¿Qué información exige una tool/API en tiempo real?
4. ¿Por qué los secretos deben quedar fuera del contexto del modelo?
