# M03.P05 — Self-attention y causal mask

**Modalidad:** individual o parejas  
**Entregable:** cálculo de scaled dot-product attention y explicación de una causal mask

## Objetivo

Comprender el mecanismo esencial de atención antes de introducir NLP generativo en M05.

Trabajaremos con tensores pequeños y no con texto.

## Ruta esencial

Abre `notebooks/M03_P05_Attention_Transformer.ipynb`.

### Parte A — Scaled dot-product attention

Completa:

```text
Attention(Q, K, V) = softmax((QK^T) / sqrt(d_k)) V
```

Inspecciona:

- matriz de scores;
- pesos de atención;
- suma de cada fila;
- salida final.

Comprueba que cada fila de los pesos suma aproximadamente `1`.

### Parte B — Causal mask

Construye una máscara triangular que bloquee las posiciones futuras.

Aplica la máscara **antes del softmax** y vuelve a calcular los pesos.

Comprueba que una posición:

- puede atender a sí misma;
- puede atender al pasado;
- no puede atender al futuro.

## Preguntas

1. ¿Qué papel tienen Q, K y V?
2. ¿Por qué se divide por `sqrt(d_k)`?
3. ¿Qué impide exactamente la causal mask?
4. ¿Por qué un decoder autoregresivo necesita esta restricción?

## Ampliación

El notebook conserva una sección opcional con `nn.MultiheadAttention` para inspeccionar las formas de entrada y salida. El entrenamiento de un Transformer completo queda fuera de la ruta esencial.
