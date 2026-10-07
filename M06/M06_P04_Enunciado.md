# M06.P04 — Two-step RAG: fuentes, citas y no-answer

**Ruta de clase** · notebook completamente implementado

## Objetivo

Observar un RAG determinista:

```text
question -> retrieval obligatorio -> context -> Luna -> RAGAnswer -> citation validation
```

Abre `notebooks/M06_P04_Two_Step_RAG.ipynb`.

## Experimentos

1. Ejecuta una pregunta con evidencia sobre acceso privilegiado.
2. Inspecciona el contexto enviado al modelo: `source_id`, versión, estado y contenido.
3. Comprueba que las citas pertenecen a documentos realmente recuperados y `CURRENT`.
4. Fuerza una cita ficticia como `PROC-999` y comprueba que `validate_citations()` la rechaza.
5. Ejecuta la pregunta sobre el presupuesto anual del programa de IA y verifica `insufficient_evidence=True`.
6. Comprueba que no existe fallback silencioso a una respuesta paramétrica del modelo.

## Preguntas

- ¿Por qué structured output no garantiza que una cita sea verdadera?
- ¿En qué capa debe rechazarse una cita inventada?
- ¿Por qué `NO_EVIDENCE` es un resultado correcto?
