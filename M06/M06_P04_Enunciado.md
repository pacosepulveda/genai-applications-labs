# M06.P04 — Two-step RAG: fuentes, citas y no-answer

**Modalidad:** individual o parejas  
**Entregable:** flujo RAG determinista con validación de citas

## Objetivo

Construirás:

```text
question -> retrieval obligatorio -> context -> Luna -> RAGAnswer -> validation
```

## Tareas

Abre:

```text
notebooks/M06_P04_Two_Step_RAG.ipynb
```

### Parte A — RAGAnswer

Utiliza:

```python
class RAGAnswer(BaseModel):
    answer: str
    source_ids: list[str]
    insufficient_evidence: bool
```

### Parte B — Context

Implementa `format_documents(...)`.

Cada fragmento debe incluir:

```text
source_id
version
status
contenido
```

### Parte C — Retrieval obligatorio

Reutiliza el retriever de P02 con el `k` elegido en P03.

Excluye `OBSOLETE` **antes** de construir el contexto.

### Parte D — Structured output

Utiliza GPT-5.6 Luna mediante `ChatBedrockConverse` y `with_structured_output(RAGAnswer)`.

### Parte E — Citation validator

Una cita solo es válida si:

```text
source_id citado ∈ source_ids recuperados y CURRENT
```

### Parte F — Dos casos

Prueba:

```text
¿Cuánto dura un acceso privilegiado?
```

y:

```text
¿Cuál es el presupuesto anual aprobado para el programa de IA?
```

En el segundo caso debe quedar explícito que no hay evidencia suficiente. No hay fallback a una respuesta "de memoria".

## Ampliación

Ejecuta todo `retrieval_eval.jsonl` como suite de regresión.

## Preguntas

1. ¿Por qué structured output no valida una cita por sí solo?
2. ¿Por qué retrieval es obligatorio cuando se exigen fuentes autoritativas?
3. ¿Por qué no-answer es comportamiento correcto?
