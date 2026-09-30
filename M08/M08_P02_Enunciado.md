# M08.P02 — Skill Gaps: upskill, reskill, hire o partner

**Modalidad:** individual o equipos pequeños  
**Entregable:** skill gap plan por persona y plan de capacidad del equipo

## Objetivo

Convertir una skill matrix en decisiones de desarrollo de talento.

## Material

```text
assets/team_profiles.csv
assets/role_requirements.csv
assets/learning_catalog.csv
```

## Tareas

Abre:

```text
notebooks/M08_P02_Skill_Gaps.ipynb
```

### Parte A — Matching

Para cada persona calcula su distancia frente a distintos target roles.

Una métrica didáctica:

```text
gap =
sum(max(required - current, 0))
```

### Parte B — Transiciones plausibles

Evalúa:

```text
Ana     -> AI Engineer
Bruno   -> Data/Knowledge Engineer
Diego   -> Platform Engineer
Elena   -> Security Partner
Fátima  -> Product Owner
Gonzalo -> Domain SME
```

No asumas que menor gap numérico significa automáticamente mejor decisión.

### Parte C — Desarrollo

Para cada gap decide:

```text
UPSKILL
RESKILL
HIRE
PARTNER
```

### Parte D — Learning Plan

Utiliza `learning_catalog.csv` para construir un plan de aprendizaje.

Debe ligar:

```text
skill gap
-> learning action
-> práctica real
-> evidence
```

### Parte E — Bus factor

Identifica skills críticas donde:

```text
solo una persona
```

puede operar o revisar.

Propón mitigación.

## Preguntas

1. ¿Cuándo preferirías talento interno frente a contratar?
2. ¿Qué diferencia existe entre upskill y reskill?
3. ¿Qué gaps no deberían cubrirse solo con formación?
4. ¿Cómo demostrarías que una persona ha adquirido la competencia?
