# M05.P05 — Tareas NLP y evaluación

**Ampliación**

## Objetivo

Ejecutarás una pequeña suite de regresión para resumen, traducción y generación controlada.

Abre:

```text
notebooks/M05_P05_NLP_Tasks_Evaluation.ipynb
```

## Trabajo

1. Ejecuta todos los casos de `assets/nlp_eval_cases.jsonl`.
2. Revisa `metric_rouge1_recall`, `constraints_ok` y `unsupported_claims`.
3. Inspecciona el CSV generado.
4. Añade un `protected span` a un caso de traducción y vuelve a ejecutar.
5. Compara greedy, beam search y sampling sobre el mismo resumen.

## Preguntas

1. ¿Por qué ROUGE no mide factualidad?
2. ¿Qué aporta un conjunto fijo de regresión?
3. ¿Por qué conviene separar restricciones verificables de valoración humana?
