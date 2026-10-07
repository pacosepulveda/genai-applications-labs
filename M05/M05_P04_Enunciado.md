# M05.P04 — Logits, decoding y sampling

**Ruta esencial**

## Objetivo

Observarás cómo el mismo decoder produce comportamientos distintos al cambiar la estrategia de selección del siguiente token.

Abre:

```text
notebooks/M05_P04_Decoding_Sampling.ipynb
```

## Trabajo

1. Ejecuta el forward y observa los 10 tokens con mayor probabilidad.
2. Ejecuta greedy dos veces.
3. Compara `temperature=0.3` y `temperature=1.0` usando la misma seed.
4. Ejecuta `top_p=0.9` y después prueba `top_p=0.5`.
5. Compara `max_new_tokens=20` y `80`.
6. Cambia el prompt y repite al menos una comparación.

## Preguntas

1. ¿Qué diferencia existe entre logits y probabilidades?
2. ¿Qué modifica `temperature`?
3. ¿Qué hace `top_p`?
4. ¿Por qué greedy determinista no implica factualidad?
5. ¿Por qué `max_new_tokens` es un control operacional?
