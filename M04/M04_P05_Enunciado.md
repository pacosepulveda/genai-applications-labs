# M04.P05 — Diffusion paso a paso: ruido, timestep y denoising

**Modalidad:** individual o parejas  
**Entregable:** notebook con forward diffusion, denoiser entrenado y sampling iterativo

## Objetivo

Comprenderás diffusion entrenando un modelo pequeño sobre imágenes 8×8.

No utilizaremos un modelo text-to-image grande. La práctica aísla el mecanismo fundamental:

```text
imagen
-> añadir ruido
-> predecir ruido
-> retirar ruido
-> repetir
```

## Tareas

Abre:

```text
notebooks/M04_P05_Tiny_Diffusion.ipynb
```

### Parte A — Forward process

Implementa una función que, dados:

- imagen `x0`;
- timestep `t`;
- ruido `epsilon`;

construya una versión ruidosa `x_t`.

Visualiza la misma imagen en distintos timesteps.

### Parte B — Timestep encoding

Construye una representación sencilla del timestep.

El denoiser debe saber cuánto ruido contiene la entrada.

### Parte C — Denoiser

Construye una red pequeña que reciba:

```text
x_t + timestep
```

y prediga:

```text
epsilon
```

### Parte D — Training objective

Entrena con:

```text
MSE(predicted_noise, true_noise)
```

### Parte E — Reverse sampling

Comienza con ruido gaussiano y aplica iterativamente el denoiser.

Visualiza varias etapas del proceso.

### Parte F — Comparación con GAN

Compara:

- training objective;
- estabilidad;
- número de redes;
- coste de sampling;
- facilidad de conditioning.

## Preguntas

1. ¿Por qué el timestep debe formar parte de la entrada?
2. ¿Qué diferencia fundamental existe entre el entrenamiento de GAN y diffusion?
3. ¿Por qué diffusion suele necesitar varios pasos de inferencia?
4. ¿Qué ventaja aportaría realizar el proceso en un espacio latente?
