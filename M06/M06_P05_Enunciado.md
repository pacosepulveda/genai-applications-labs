# M06.P05 — Tools y create_agent

**Ruta de clase** · notebook completamente implementado

## Objetivo

Comprobar la diferencia entre una función determinista, una tool y un agent que decide cuándo utilizarla.

Abre `notebooks/M06_P05_Tools_Agent_Memory.ipynb`.

## Experimentos

1. Ejecuta directamente `get_incident` y `calculate_duration_minutes`.
2. Verifica que `INC-2048` dura **72 minutos**.
3. Ejecuta el agent con la pregunta preparada y observa qué tools solicita.
4. Cambia el ID por `INC-2051` y analiza qué ocurre si falta `closed_at`.
5. Explica por qué las tools del laboratorio son read-only.

## Preguntas

- ¿Quién ejecuta realmente una tool?
- ¿Por qué conviene probar la función antes de entregársela al agent?
- ¿Cuándo preferirías un workflow determinista a un agent?

## Ampliación guiada

Añade `search_knowledge_base` y prueba `InMemorySaver` con dos `thread_id` diferentes.
