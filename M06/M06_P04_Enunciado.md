# M06.P04 — Two-step RAG: respuestas con fuentes y no-answer

**Modalidad:** individual o parejas  
**Entregable:** chain RAG determinista, respuesta estructurada y validación de citas

## Objetivo

Construirás el flujo para conocimiento corporativo:

```text
question -> authorized retrieval -> context -> GPT-5.6 Luna -> RAGAnswer -> citation validation
```

Retrieval es obligatorio. El modelo no decide si quiere buscar.

## Tareas

Abre `notebooks/M06_P04_Two_Step_RAG.ipynb`.

### Parte A — RAGAnswer

Define `answer`, `source_ids` e `insufficient_evidence` mediante Pydantic.

### Parte B — Context formatter

Cada chunk debe entrar con identificador, `source_id`, versión, status y contenido.

### Parte C — Retrieval obligatorio

Reutiliza la configuración elegida en P03 y excluye obsoletos antes del contexto.

### Parte D — Prompt

Debe responder solo con fuentes, tratar las fuentes como datos y no instrucciones, declarar evidencia insuficiente y citar solo `source_ids` utilizados.

### Parte E — Structured output con Luna

Utiliza GPT-5.6 Luna mediante `ChatBedrockConverse` y `model.with_structured_output(RAGAnswer)`.

### Parte F — Citation validator

Rechaza source IDs inventados, no recuperados u obsoletos.

### Parte G — No evidence

Para `¿Cuál es el presupuesto anual aprobado para el programa de IA?`, el sistema debe producir `insufficient_evidence=true`; no hay fallback al conocimiento paramétrico.

### Parte H — Regression cases

Ejecuta el eval set y registra fuentes recuperadas/citadas, validación y no-evidence.

## Preguntas

1. ¿Por qué RAG no elimina las alucinaciones?
2. ¿Qué diferencia existe entre fuente recuperada y fuente citada?
3. ¿Por qué no-answer es una capacidad útil?
4. ¿Por qué no permitimos fallback directo al LLM para información corporativa?
