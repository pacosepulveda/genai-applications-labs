# M06.P03 — Retrieval evaluation: medir antes de generar

**Modalidad:** individual o parejas  
**Entregable:** benchmark del retriever y decisión de configuración

## Objetivo

Evaluarás el sistema de retrieval **sin utilizar todavía un LLM**.

El dataset de evaluación está en:

```text
assets/retrieval_eval.jsonl
```

## Tareas

Abre:

```text
notebooks/M06_P03_Retrieval_Evaluation.ipynb
```

### Parte A — Eval set

Carga cada caso:

```text
question
expected_source_ids
expected_status
```

### Parte B — Hit Rate@k

Implementa:

```python
hit_rate_at_k(...)
```

Un caso es hit cuando al menos una fuente esperada aparece en top-k.

Los casos `NO_EVIDENCE` deben evaluarse aparte.

### Parte C — MRR

Implementa Mean Reciprocal Rank usando la posición de la primera fuente relevante.

### Parte D — Configuraciones

Compara al menos:

```text
k = 1
k = 2
k = 4
```

y dos estrategias:

```text
similarity
MMR
```

### Parte E — Vigencia

Repite la evaluación:

1. sin filtrar documentos obsoletos;
2. excluyendo `status=OBSOLETE`.

Comprueba el efecto sobre `PROC-017`.

### Parte F — Exact IDs

Analiza el caso:

```text
/api/v2/status
```

y explica por qué un sistema híbrido lexical + semantic podría resultar útil.

### Parte G — Selección

Elige una configuración para P04 y justifica usando:

- Hit Rate@k;
- MRR;
- coste de contexto;
- ruido recuperado.

## Preguntas

1. ¿Por qué evaluar solo la respuesta final oculta fallos del retriever?
2. ¿Qué mide MRR que no muestra Hit Rate?
3. ¿Por qué `k` alto no es siempre mejor?
4. ¿Cuándo añadirías búsqueda lexical o reranking?
