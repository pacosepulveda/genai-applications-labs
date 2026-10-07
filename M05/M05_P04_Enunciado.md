# M05.P04 — Logits, decoding y sampling

**Modalidad:** individual o parejas  
**Entregable:** notebook con comparación breve de estrategias de decoding

## Objetivo

Observarás cómo un decoder causal transforma logits en una secuencia generada y comprobarás que cambiar parámetros de decoding **no cambia los pesos ni añade conocimiento al modelo**.

## Tareas

Abre `notebooks/M05_P04_Decoding_Sampling.ipynb` y utiliza `HuggingFaceTB/SmolLM2-135M-Instruct`.

### Parte A — Próximo token

Con un prompt corto: ejecuta un `forward`, toma los logits de la última posición, aplica `softmax` y muestra los diez tokens más probables.

### Parte B — Greedy decoding

Genera dos veces con `do_sample=False` y observa el resultado.

### Parte C — Temperature

Con sampling activado compara `temperature=0.3` y `temperature=1.0`. Fija la misma seed antes de ambas ejecuciones.

Explica qué cambia en la distribución y evita describir `temperature` como “inteligencia”.

### Parte D — Top-p

Genera con:

```text
do_sample=True
temperature=0.8
top_p=0.9
```

Compara la salida con greedy.

### Parte E — Presupuesto de salida

Compara `max_new_tokens=20` y `max_new_tokens=80`.

## Ampliación

Si quieres profundizar, prueba `top_k`, más temperaturas, distintas seeds y combinaciones top-k/top-p.

## Preguntas

1. ¿Qué diferencia existe entre logits y probabilidades?
2. ¿Qué modifica `temperature`?
3. ¿Qué hace `top_p`?
4. ¿Por qué greedy determinista no implica factualidad?
5. ¿Por qué `max_new_tokens` es también un control operacional?
