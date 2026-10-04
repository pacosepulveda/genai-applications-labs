# M06.P05 — Tools, create_agent y estado por thread

**Modalidad:** individual o parejas  
**Entregable:** tools probadas de forma independiente, agente read-only y demostración de short-term memory

## Objetivo

Construirás un agente solo después de disponer de tools deterministas y probadas: `search_knowledge_base`, `get_incident` y `calculate_duration_minutes`. Todas son read-only.

## Tareas

Abre `notebooks/M06_P05_Tools_Agent_Memory.ipynb`.

### Parte A — Tools

Implementa las tres funciones con `@tool`, type hints y docstrings precisos.

### Parte B — Test manual

Ejecuta cada tool directamente antes del agente. Comprueba `INC-2048` y calcula su duración.

### Parte C — create_agent + Luna

Crea el modelo con `ChatBedrockConverse` usando `us.openai.gpt-5.6-luna` en `us-east-1`, y después utiliza `create_agent(...)` con las tres tools.

### Parte D — Pregunta multi-tool

Analiza `INC-2048`, calcula su duración y consulta qué requisitos de comunicación P1 son aplicables. Inspecciona las tool calls.

### Parte E — Short-term memory

Añade `InMemorySaver()` y utiliza `thread_id="thread-a"`. Primero indica `Estamos analizando INC-2048.` y después pregunta `¿Cuánto duró?`.

### Parte F — Aislamiento

Repite la segunda pregunta con `thread_id="thread-b"` y comprueba que no comparte estado.

### Parte G — Límites

Discute límites de iteraciones, timeout, autorización y aprobación humana. No añadas tools destructivas.

## Preguntas

1. ¿Quién ejecuta realmente una tool?
2. ¿Por qué probar la tool antes de dársela al agente?
3. ¿Cuándo sería mejor un workflow determinista?
4. ¿Qué persiste `InMemorySaver` al reiniciar el proceso?
5. ¿Por qué short-term memory no es RAG?
