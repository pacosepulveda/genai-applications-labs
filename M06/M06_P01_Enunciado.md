# M06.P01 — LangChain moderno: Runnables, prompts y structured output

**Modalidad:** individual o parejas  
**Entregable:** notebook con pipeline compuesto, batch y salida validada

## Objetivo

Comprenderás la unidad de composición actual de LangChain: `Runnable`.

Construirás primero una chain **sin depender de un LLM remoto** para poder inspeccionar cada tipo intermedio.

## Tareas

Abre:

```text
notebooks/M06_P01_Runnables_Structured_Output.ipynb
```

### Parte A — Prompt template

Construye un `ChatPromptTemplate` para analizar un incidente.

Variables:

```text
incident_id
service
summary
```

Inspecciona el objeto que produce `prompt.invoke(...)`.

### Parte B — RunnableLambda

Crea un componente determinista que reciba el prompt y produzca un JSON de demostración.

No pretende simular inteligencia.

Su objetivo es mostrar el contrato:

```text
input
-> prompt
-> runnable
-> parser
```

### Parte C — PydanticOutputParser

Define:

```python
class IncidentAnalysis(BaseModel):
    incident_id: str
    category: str
    requires_review: bool
```

Construye:

```text
prompt | mock_model | parser
```

y ejecuta `invoke()`.

### Parte D — Batch

Ejecuta la misma chain sobre varios incidentes con:

```python
chain.batch(...)
```

### Parte E — RunnableParallel

Con el mismo input calcula en paralelo:

- longitud del resumen;
- presencia de la palabra `balanceador`;
- análisis estructurado.

### Parte F — Modelo real

Si el entorno tiene configurado el modelo facilitado por el instructor, sustituye el `RunnableLambda` por el chat model y utiliza structured output.

La lógica posterior no debe cambiar.

## Preguntas

1. ¿Qué ventaja tiene que los componentes compartan la interfaz `Runnable`?
2. ¿Por qué `prompt | model | parser` no es simplemente sintaxis decorativa?
3. ¿Qué diferencia hay entre schema validation y validación de negocio?
4. ¿Cuándo utilizarías `batch()` y cuándo `ainvoke()`?
