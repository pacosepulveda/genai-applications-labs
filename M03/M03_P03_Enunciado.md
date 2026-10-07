# M03.P03 — Provocar overfitting y corregirlo · ampliación

**Modalidad:** individual o parejas  
**Entregable:** curvas interpretadas y comparación base/regularizada

## Objetivo

Observar overfitting sin dedicar tiempo a implementar desde cero una red sobredimensionada.

## Tareas

Abre `notebooks/M03_P03_Overfitting_Regularization.ipynb`.

El código ya incluye reducción deliberada de train, una MLP sobredimensionada, curvas train/validation, Dropout, weight decay, early stopping y gradient clipping.

### Experimento

1. Ejecuta la red base.
2. Identifica dónde validation deja de mejorar.
3. Ejecuta la red regularizada.
4. Cambia `patience=6` por `patience=3`.
5. Explica qué cambia.

## Preguntas

1. ¿Cómo distingues overfitting de underfitting?
2. ¿Por qué la última época no tiene por qué ser la mejor?
3. ¿Por qué `Dropout` cambia entre `train()` y `eval()`?
4. ¿Qué limita gradient clipping?
