# M04.P02 — VAE: reconstrucción, sampling y espacio latente

**Modalidad:** individual o parejas  
**Entregable:** VAE entrenado, reconstrucciones, muestras e interpolación latente

## Objetivo

Construirás un Variational Autoencoder pequeño para observar directamente:

```text
imagen
-> μ, log_var
-> sampling
-> z
-> decoder
-> reconstrucción
```

## Tareas

Abre:

```text
notebooks/M04_P02_VAE_Latent_Space.ipynb
```

### Parte A — Modelo

Implementa un VAE pequeño:

- entrada de 64 valores;
- encoder con una capa oculta de aproximadamente 32 unidades;
- `mu`;
- `log_var`;
- reparameterization;
- decoder simétrico;
- salida de 64 valores.

Utiliza un espacio latente de dimensión 2 para poder visualizarlo. Mantén el entrenamiento en torno a 25–30 épocas como máximo orientativo.

### Parte B — Loss

Combina:

```text
reconstruction loss
+
KL divergence
```

Registra ambos componentes por separado.

### Parte C — Entrenamiento

Entrena sobre `load_digits`.

Visualiza:

- train loss;
- reconstruction loss;
- KL loss.

### Parte D — Reconstrucción

Selecciona varias imágenes de test y muestra:

```text
original | reconstrucción
```

### Parte E — Sampling

Genera valores:

```python
z ~ N(0, I)
```

y decodifícalos.

Comprueba que el modelo genera imágenes nuevas sin recibir una imagen original.

### Parte F — Espacio latente

Proyecta los ejemplos de test usando `mu` y colorea por clase.

No esperamos que las diez clases queden perfectamente separadas.

### Parte G — Interpolación

Elige dos imágenes, obtén sus representaciones latentes e interpola entre ambas.

Visualiza la transición.

## Preguntas

1. ¿Por qué un VAE devuelve una distribución y no un único `z`?
2. ¿Qué papel cumple KL divergence?
3. ¿Qué ocurriría si eliminamos por completo el término KL?
4. ¿Por qué las reconstrucciones pueden ser más suaves que las imágenes originales?
