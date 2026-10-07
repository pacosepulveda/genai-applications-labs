# M05.P02 — Embeddings contextuales

**Ampliación**

## Objetivo

Comprobarás que el mismo token puede partir del mismo embedding de entrada y terminar con una representación diferente según el contexto.

Abre:

```text
notebooks/M05_P02_Contextual_Embeddings.ipynb
```

## Trabajo

1. Ejecuta el notebook completo.
2. Compara el cosine similarity del embedding de entrada de `bank` con la representación contextual.
3. Cambia uno de los contextos y repite.
4. Compara el pooling con y sin `attention_mask`.
5. Sustituye una frase del batch por otra mucho más corta y observa el efecto del padding.

## Preguntas

1. ¿Dónde aparece el contexto: en la lookup table o después del Transformer?
2. ¿Por qué ignorar padding altera una representación de frase?
3. ¿Qué diferencia hay entre embedding de token y embedding de frase?
