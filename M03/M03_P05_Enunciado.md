# M03.P05 — Self-attention y causal mask

**Modalidad:** individual o parejas  
**Entregable:** matrices inspeccionadas y explicación de la causal mask

## Objetivo

Comprender el mecanismo esencial de attention antes de M05.

El notebook contiene el cálculo completo para que el trabajo se centre en interpretar las matrices.

## Ruta esencial

Abre `notebooks/M03_P05_Attention_Transformer.ipynb`.

### Parte A — Scaled dot-product attention

Ejecuta:

```text
scores = QK^T / sqrt(d_k)
weights = softmax(scores)
output = weights V
```

Comprueba scores, pesos, suma por fila y salida.

### Parte B — Causal mask

Ejecuta la versión con máscara triangular y compara `weights` con `causal_weights`.

Localiza las posiciones futuras y comprueba que su peso queda en cero tras softmax.

### Parte C — Modifica y predice

Cambia un único vector de Q. Antes de ejecutar, predice qué fila de la matriz de atención cambiará más.

## Preguntas

1. ¿Qué papel tienen Q, K y V?
2. ¿Por qué se divide por `sqrt(d_k)`?
3. ¿Qué impide exactamente la causal mask?
4. ¿Por qué un decoder autoregresivo necesita esta restricción?

## Ampliación

El notebook incluye `MultiheadAttention` y un mini Transformer ya implementados.
