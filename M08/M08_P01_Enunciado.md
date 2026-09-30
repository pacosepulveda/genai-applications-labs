# M08.P01 — Capability Map: ¿qué equipo necesitamos realmente?

**Modalidad:** individual o equipos pequeños  
**Entregable:** capability map y propuesta de equipo inicial

## Objetivo

No empezarás asignando títulos.

Empezarás preguntando:

```text
¿Qué capacidades necesita el producto?
```

## Material

```text
assets/team_profiles.csv
assets/role_requirements.csv
```

Abre:

```text
notebooks/M08_P01_Capability_Map.ipynb
```

## Parte A — Mapa actual

Calcula para cada skill:

- media del equipo;
- máximo disponible;
- número de personas con nivel >= 3.

## Parte B — Capacidades críticas

Para Enterprise GenAI Assistant marca cada skill:

```text
CRITICAL
IMPORTANT
SUPPORTING
```

Justifica.

## Parte C — Coverage

Define una regla de cobertura.

Ejemplo:

```text
covered =
al menos una persona >= required_level
```

Después identifica:

```text
single_point_of_failure
```

si solo una persona cubre una skill crítica.

## Parte D — Equipo mínimo

Propón un squad con capacidades para:

- Product;
- AI Engineering;
- Data/Knowledge Engineering;
- Software Engineering;
- Domain;
- Security/Platform support.

No necesitas asignar un FTE completo a cada función.

## Parte E — Roles que NO crearías

Decide si crearías específicamente:

```text
Prompt Engineer
AI Researcher
MLOps Engineer
```

como puestos dedicados para este piloto.

Justifica.

## Preguntas

1. ¿Qué diferencia hay entre capability y job title?
2. ¿Qué skill tiene mayor bus-factor risk?
3. ¿Qué persona podría evolucionar hacia AI Engineer?
4. ¿Qué responsabilidades no debería absorber el equipo técnico?
