# M03.P05 — Self-attention y Transformer sin NLP

**Modalidad:** individual o parejas  
**Entregable:** implementación de scaled dot-product attention y pequeño clasificador Transformer

## Objetivo

Comprender la arquitectura Transformer sin introducir todavía tokenización lingüística, BERT, GPT o tareas NLP del M05.

Trabajarás con **secuencias de enteros**, no con texto.

## Parte A — Scaled dot-product attention

Abre `notebooks/M03_P05_Attention_Transformer.ipynb`.

Implementa:

```text
Attention(Q, K, V) = softmax((QK^T) / sqrt(d_k)) V
```

Inspecciona:

- shape de `Q`;
- shape de `K`;
- matriz de scores;
- matriz de attention weights;
- salida.

Comprueba que cada fila de los pesos suma aproximadamente 1.

## Parte B — Causal mask

Construye una máscara que impida a una posición atender a posiciones futuras.

Visualiza la matriz.

Explica por qué esta restricción es necesaria en generación autoregresiva.

## Parte C — Multi-head attention

Utiliza `torch.nn.MultiheadAttention`.

Compara shapes con la implementación manual.

No se espera que los valores sean iguales: las proyecciones aprendidas son distintas.

## Antes de la Parte D — Embeddings

`nn.Embedding` funciona como una tabla aprendible: recibe un identificador entero y devuelve un vector. En esta práctica esos identificadores no son palabras, sino símbolos abstractos.

El **positional embedding** hace algo equivalente con la posición `0, 1, 2...`, permitiendo que el modelo distinga dónde aparece cada símbolo.

## Parte D — Mini Transformer

Genera un dataset sintético y balanceado de secuencias de enteros.

El objetivo será predecir si:

```text
primer símbolo == último símbolo
```

La clase depende de posiciones alejadas entre sí, por lo que el modelo debe combinar información de la secuencia.

Construye un Transformer deliberadamente pequeño:

```text
token ids
-> Embedding (d_model=32)
-> positional embedding
-> TransformerEncoder (1 layer, 4 heads, feed-forward=64)
-> representación de extremos
-> Linear
-> clase
```

Entrena y evalúa durante un máximo orientativo de 15 épocas.

## Preguntas

1. ¿Qué representan Q, K y V?
2. ¿Por qué se divide por `sqrt(d_k)`?
3. ¿Qué diferencia hay entre self-attention y una RNN?
4. ¿Dónde aparece una MLP dentro de un bloque Transformer?
5. ¿Por qué hace falta información posicional?
6. ¿Por qué este ejercicio todavía no constituye un modelo de lenguaje?
