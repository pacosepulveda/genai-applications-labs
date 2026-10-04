# M06.P01 — LangChain moderno: Runnables, prompts y structured output

**Modalidad:** individual o parejas  
**Entregable:** notebook con pipeline compuesto, batch y salida validada

## Objetivo

Comprenderás la unidad de composición actual de LangChain: `Runnable`.

Primero construirás la chain sin depender del modelo remoto para inspeccionar cada contrato. Después sustituirás el mock por **GPT-5.6 Luna en Amazon Bedrock**.

## Tareas

Abre:

```text
notebooks/M06_P01_Runnables_Structured_Output.ipynb
```

### Parte A — Prompt template

Construye un `ChatPromptTemplate` para analizar un incidente con `incident_id`, `service` y `summary`. Inspecciona el objeto que produce `prompt.invoke(...)`.

### Parte B — RunnableLambda

Crea un componente determinista que reciba el prompt y produzca un JSON de demostración:

```text
input -> prompt -> runnable -> parser
```

### Parte C — PydanticOutputParser

Define `IncidentAnalysis` con `incident_id`, `category` y `requires_review`. Construye `prompt | mock_model | parser` y ejecuta `invoke()`.

### Parte D — Batch

Ejecuta la chain sobre varios incidentes mediante `batch()`.

### Parte E — RunnableParallel

Con el mismo input calcula en paralelo longitud del resumen, presencia de `balanceador` y análisis estructurado.

### Parte F — GPT-5.6 Luna

Crea el chat model con `ChatBedrockConverse`:

```text
region: us-east-1
model: us.openai.gpt-5.6-luna
```

Utiliza `with_structured_output(IncidentAnalysis)`. El resultado consumido por la lógica posterior debe seguir siendo un `IncidentAnalysis`.

## Preguntas

1. ¿Qué ventaja tiene que los componentes compartan la interfaz `Runnable`?
2. ¿Por qué `prompt | model | parser` describe contratos entre tipos?
3. ¿Qué diferencia hay entre schema validation y validación de negocio?
4. ¿Cuándo utilizarías `batch()` y cuándo `ainvoke()`?
