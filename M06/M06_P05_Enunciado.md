# M06.P05 — Tools, create_agent y estado por thread

**Modalidad:** individual o parejas  
**Entregable:** tools probadas de forma independiente, agente read-only y demostración de short-term memory

## Objetivo

Construirás un agente solo después de disponer de tools deterministas y probadas.

Tools:

```text
search_knowledge_base
get_incident
calculate_duration_minutes
```

Todas son read-only.

## Tareas

Abre:

```text
notebooks/M06_P05_Tools_Agent_Memory.ipynb
```

### Parte A — Tools

Implementa con `@tool`:

```python
search_knowledge_base(query: str)
get_incident(incident_id: str)
calculate_duration_minutes(start_iso: str, end_iso: str)
```

Incluye type hints y docstrings precisos.

### Parte B — Test manual

Antes del agente, ejecuta cada tool directamente.

Comprueba:

```text
get_incident("INC-2048")
```

y calcula su duración.

### Parte C — create_agent

Crea un agente con:

```python
create_agent(...)
```

y las tres tools.

Utiliza el modelo tool-capable facilitado por el instructor.

### Parte D — Pregunta multi-tool

Pregunta conceptualmente:

```text
Analiza INC-2048, calcula cuánto duró y dime qué requisitos de comunicación P1 son aplicables según la base de conocimiento.
```

Inspecciona qué tools usa.

### Parte E — Short-term memory

Añade:

```python
InMemorySaver()
```

e invoca el agente con:

```text
thread_id = "thread-a"
```

Primera petición:

```text
Estamos analizando INC-2048.
```

Segunda:

```text
¿Cuánto duró?
```

### Parte F — Aislamiento

Repite la segunda pregunta con:

```text
thread_id = "thread-b"
```

Comprueba que no comparte el estado del thread A.

### Parte G — Límites

Discute cómo añadirías:

- límite de iteraciones;
- timeout;
- autorización;
- aprobación humana.

No añadas tools destructivas al laboratorio.

## Preguntas

1. ¿Quién ejecuta realmente una tool?
2. ¿Por qué debemos probar la tool antes de usarla con un agente?
3. ¿Cuándo sería mejor un workflow determinista?
4. ¿Qué persiste `InMemorySaver` y qué ocurre al reiniciar el proceso?
5. ¿Por qué short-term memory no es lo mismo que RAG?
