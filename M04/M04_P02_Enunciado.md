# M04.P02 — VAE: reconstruir, muestrear e interpolar

**Modalidad:** individual o parejas  
**Entregable:** interpretación de reconstrucciones, sampling y latent

## Objetivo

Observar el comportamiento de un VAE sin dedicar tiempo a escribir su implementación.

## Trabajo

Abre `notebooks/M04_P02_VAE_Latent_Space.ipynb`.

El notebook ya contiene encoder, `mu`, `log_var`, reparameterization, decoder, reconstruction loss + KL, entrenamiento, sampling e interpolación.

Ejecuta el flujo completo y analiza sus salidas.

Después cambia `latent_dim=2` por `latent_dim=4` y explica qué cambia, especialmente respecto a la visualización directa del espacio latente.

## Preguntas

1. ¿Por qué el encoder no devuelve solo un punto?
2. ¿Qué intenta conservar reconstruction loss?
3. ¿Qué papel tiene KL?
4. ¿Por qué sampling permite generar sin partir de una imagen original?
