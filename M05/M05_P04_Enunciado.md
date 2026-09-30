# M05.P04 — Logits, decoding y sampling

**Modalidad:** individual o parejas  
**Entregable:** comparación reproducible de estrategias de decoding

## Objetivo

Comprobarás que cambiar parámetros de generación modifica cómo seleccionamos tokens, no los pesos del modelo.

Utilizarás el modelo decoder causal de M05.P03.

## Tareas

Abre:

```text
notebooks/M05_P04_Decoding_Sampling.ipynb
```

### Parte A — Próximo token

Dado un prompt:

1. ejecuta un forward;
2. toma los logits de la última posición;
3. aplica softmax;
4. muestra los diez tokens más probables.

### Parte B — Greedy decoding

Genera con:

```text
do_sample=False
```

Repite y comprueba su comportamiento.

### Parte C — Temperature

Compara varias temperaturas con sampling activado.

No describas `temperature` como “inteligencia” o “creatividad”. Analiza cómo cambia la distribución.

### Parte D — Top-k

Genera utilizando un conjunto limitado de candidatos.

### Parte E — Top-p

Genera mediante nucleus sampling.

### Parte F — Reproducibilidad práctica

Fija una seed antes de dos generaciones equivalentes.

Comprueba si el entorno produce la misma salida y documenta el resultado.

### Parte G — Presupuesto de salida

Compara:

```text
max_new_tokens=20
max_new_tokens=80
```

Identifica cuándo una salida termina por límite y cuándo por EOS si puedes observarlo.

## Preguntas

1. ¿Qué diferencia existe entre logits y probabilidades?
2. ¿Qué cambia `temperature`?
3. ¿Qué diferencia hay entre top-k y top-p?
4. ¿Por qué decoding determinista no implica factualidad?
5. ¿Por qué `max_new_tokens` forma parte del control operacional?
