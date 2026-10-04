# M04.P05 — Tiny Diffusion: ruido, timestep y denoising

**Modalidad:** individual o parejas  
**Entregable:** notebook con forward diffusion, denoiser entrenado y sampling iterativo

## Objetivo

Comprenderás diffusion entrenando un modelo pequeño sobre imágenes 8×8.

No utilizaremos un modelo text-to-image grande dentro del Space. La práctica aísla el mecanismo fundamental:

```text
imagen
-> añadir ruido
-> predecir ruido
-> retirar ruido
-> repetir
```

Todo se ejecuta en CPU.

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

Para esta práctica utiliza una representación sencilla y guiada del timestep, por ejemplo un escalar normalizado `t/(T-1)`.

El objetivo no es diseñar embeddings temporales sofisticados, sino comprobar que el denoiser necesita conocer el nivel de ruido.

### Parte C — Denoiser

Construye una red pequeña con entrada equivalente a:

```text
64 valores de x_t + timestep
```

y salida:

```text
64 valores de epsilon_pred
```

Una MLP `65 -> 128 -> 128 -> 64` es suficiente.

### Parte D — Training objective

Entrena con:

```text
MSE(predicted_noise, true_noise)
```

Mantén `T=40` y aproximadamente 15–20 épocas como referencia. No buscamos optimizar calidad visual, sino observar que el modelo aprende una señal de denoising.

### Parte E — Reverse sampling

Comienza con ruido gaussiano y aplica iterativamente el denoiser.

El notebook proporciona la ecuación simplificada del paso inverso que necesitas implementar. No se espera que derives DDPM desde cero.

Guarda varios estados intermedios para visualizar la evolución.

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
5. ¿Por qué tiene sentido estudiar el mecanismo localmente y utilizar un modelo visual grande mediante API en P06?
