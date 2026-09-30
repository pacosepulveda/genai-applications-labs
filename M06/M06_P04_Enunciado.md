# M06.P04 — Two-step RAG: respuestas con fuentes y no-answer

**Modalidad:** individual o parejas  
**Entregable:** chain RAG determinista, respuesta estructurada y validación de citas

## Objetivo

Construirás el flujo que utilizaremos para conocimiento corporativo:

```text
question
-> authorized retrieval
-> context
-> model
-> RAGAnswer
-> citation validation
```

Retrieval es obligatorio. El modelo **no decide si quiere buscar**.

## Tareas

Abre:

```text
notebooks/M06_P04_Two_Step_RAG.ipynb
```

### Parte A — RAGAnswer

Define:

```python
class RAGAnswer(BaseModel):
    answer: str
    source_ids: list[str]
    insufficient_evidence: bool
```

### Parte B — Context formatter

Cada chunk debe entrar con un identificador verificable:

```text
[S1]
source_id=PROC-017
version=3.2
status=CURRENT
...
```

### Parte C — Retrieval obligatorio

Utiliza la configuración seleccionada en P03.

Excluye documentación obsoleta **antes** de construir el contexto.

### Parte D — Prompt

El prompt debe indicar:

- responder solo con las fuentes;
- no convertir texto de las fuentes en instrucciones;
- declarar evidencia insuficiente cuando proceda;
- devolver únicamente `source_ids` realmente utilizados.

### Parte E — Structured output

Utiliza la capacidad de structured output del modelo facilitado en el entorno.

Si el proveedor no la soporta nativamente, utiliza una estrategia equivalente validada con Pydantic.

### Parte F — Citation validator

Implementa:

```python
validate_citations(answer, retrieved_docs)
```

Debe rechazar:

```text
source_id inventado
source_id no recuperado
source_id obsoleto
```

### Parte G — No evidence

Ejecuta:

```text
¿Cuál es el presupuesto anual aprobado para el programa de IA?
```

La respuesta correcta del sistema es:

```text
insufficient_evidence = true
```

No debe responder utilizando conocimiento paramétrico.

### Parte H — Regression cases

Ejecuta todos los casos del eval set y registra:

```text
question
retrieved_sources
answer_sources
citations_valid
insufficient_evidence
```

## Preguntas

1. ¿Por qué RAG no elimina las alucinaciones?
2. ¿Qué diferencia existe entre “fuente recuperada” y “fuente citada”?
3. ¿Por qué `insufficient_evidence=true` es una capacidad útil?
4. ¿Por qué no permitimos fallback directo al LLM para información corporativa?
