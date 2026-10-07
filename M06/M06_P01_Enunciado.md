# M06.P01 — Runnables, prompt y structured output

**Modalidad:** individual o parejas  
**Entregable:** notebook con un pipeline compuesto y una salida Pydantic

## Objetivo

Comprobarás que podemos cambiar el componente generativo sin cambiar el contrato que recibe el backend.

## Tareas

Abre:

```text
notebooks/M06_P01_Runnables_Structured_Output.ipynb
```

### Parte A — Prompt

Inspecciona el `ChatPromptTemplate` preparado para un incidente con:

```text
incident_id
service
summary
```

Ejecuta `prompt.invoke(...)` y observa el tipo y el contenido producido.

### Parte B — Runnable determinista

Completa `deterministic_demo(...)` para devolver un JSON compatible con:

```python
class IncidentAnalysis(BaseModel):
    incident_id: str
    category: str
    requires_review: bool
```

Compón:

```text
prompt -> RunnableLambda -> PydanticOutputParser
```

y ejecuta `invoke()`.

### Parte C — GPT-5.6 Luna

Crea `ChatBedrockConverse` con:

```text
model: us.openai.gpt-5.6-luna
region: us-east-1
```

Utiliza:

```python
model.with_structured_output(IncidentAnalysis)
```

El resultado final debe seguir siendo un `IncidentAnalysis`.

## Ampliación

Si dispones de tiempo:

- `batch()`;
- `RunnableParallel`;
- `ainvoke()`.

## Preguntas

1. ¿Qué ventaja tiene mantener un contrato Pydantic estable?
2. ¿Qué responsabilidad resuelve el parser/schema y cuál no?
3. ¿Qué ha cambiado al sustituir el mock por Luna?
