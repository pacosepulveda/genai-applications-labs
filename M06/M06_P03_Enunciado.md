# M06.P03 — Retrieval evaluation

**Ruta de clase** · notebook completamente implementado

## Objetivo

Medir retrieval antes de añadir generación.

Abre `notebooks/M06_P03_Retrieval_Evaluation.ipynb` y ejecuta el benchmark.

## Experimentos

1. Compara `Hit Rate@2` y `Hit Rate@4`.
2. Localiza qué `source_id` se esperaba para cada caso positivo.
3. Analiza `R09`, marcado como `NO_EVIDENCE`.
4. Explica por qué devolver el documento más parecido en `R09` no significa que exista evidencia.
5. Elige `k=2` o `k=4` para P04 y justifica la elección considerando cobertura, ruido y contexto.

## Preguntas

- ¿Por qué separar retrieval eval de generation eval?
- ¿Por qué aumentar `k` puede empeorar el sistema aunque aumente cobertura?
- ¿Cómo debería medirse un caso donde la respuesta correcta es no recuperar evidencia suficiente?

## Ampliación

Implementa MRR o compara MMR con similarity search.
