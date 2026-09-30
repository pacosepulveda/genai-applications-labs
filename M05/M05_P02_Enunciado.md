# M05.P02 — Embeddings estáticos vs contextuales

**Modalidad:** individual o parejas  
**Entregable:** notebook que demuestre experimentalmente el efecto del contexto

## Objetivo

Demostrarás que el embedding de entrada asociado a un token es fijo, mientras que la representación que sale del Transformer depende del contexto.

Utilizarás un BERT miniatura para reducir consumo de recursos.

## Tareas

Abre:

```text
notebooks/M05_P02_Contextual_Embeddings.ipynb
```

### Parte A — Token y embedding de entrada

Utiliza estas frases:

```text
The bank approved the loan.
The engineer sat on the bank of the river.
```

Localiza el token `bank`.

Obtén su vector directamente desde la matriz de embeddings del modelo en ambos casos.

Comprueba:

```text
cosine similarity ≈ 1
```

porque el token ID es el mismo.

### Parte B — Representación contextual

Ejecuta las dos frases a través de BERT.

Extrae `last_hidden_state` para `bank`.

Calcula cosine similarity.

Explica por qué ya no tienen que coincidir.

### Parte C — Shapes

Inspecciona:

```text
input_ids
attention_mask
last_hidden_state
```

y explica cada dimensión.

### Parte D — Sentence representation

Calcula una representación de frase mediante mean pooling respetando `attention_mask`.

Compara:

- dos frases relacionadas;
- una frase claramente distinta.

No interpretes el resultado como un sistema semántico de producción: el modelo utilizado es deliberadamente pequeño.

### Parte E — Padding

Comprueba que hacer mean pooling sin respetar `attention_mask` altera la representación cuando hay padding.

## Preguntas

1. ¿Qué diferencia existe entre embedding lookup y contextual embedding?
2. ¿Por qué la polisemia es difícil para embeddings estáticos?
3. ¿Por qué no debemos promediar posiciones PAD como si fueran palabras?
