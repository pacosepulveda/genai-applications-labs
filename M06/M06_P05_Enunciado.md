# M06.P05 — Tools y create_agent

**Modalidad:** individual o parejas  
**Entregable:** dos tools read-only probadas y un agente que las combina

## Objetivo

Construirás un agente **después** de probar sus funciones de forma determinista.

## Tareas

Abre:

```text
notebooks/M06_P05_Tools_Agent_Memory.ipynb
```

### Parte A — Dos funciones

Implementa:

```text
get_incident
calculate_duration_minutes
```

Ambas son read-only.

### Parte B — Prueba directa

Antes de crear el agente:

1. recupera `INC-2048`;
2. calcula su duración.

Comprueba el resultado manualmente.

### Parte C — Tool

Convierte ambas funciones en tools con:

- nombre claro;
- type hints;
- docstring preciso.

### Parte D — Agent

Crea GPT-5.6 Luna con `ChatBedrockConverse` y utiliza:

```python
create_agent(...)
```

Pregunta:

```text
Consulta INC-2048 y dime cuánto duró el incidente.
```

Inspecciona qué tools utiliza.

## Ampliación guiada

Si queda tiempo:

- añade `search_knowledge_base`;
- añade `InMemorySaver`;
- demuestra `thread-a` frente a `thread-b`.

## Preguntas

1. ¿Quién ejecuta realmente la tool?
2. ¿Por qué probarla antes de entregársela al agent?
3. ¿Cuándo preferirías un workflow determinista?
4. ¿Por qué las tools del laboratorio son read-only?
