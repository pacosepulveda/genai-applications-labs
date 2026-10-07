# M04.P03 — GAN: Generator vs Discriminator

**Modalidad:** individual o parejas  
**Entregable:** interpretación del entrenamiento adversarial

## Objetivo

Observar un training loop GAN completo y la evolución de un conjunto fijo de muestras.

## Trabajo

Abre `notebooks/M04_P03_GAN_Training.ipynb`.

El código ya implementa Generator, Discriminator, losses, optimizadores y training loop.

Ejecuta el notebook y analiza `d_loss`, `g_loss`, las imágenes producidas desde el mismo `fixed_noise` y los artefactos guardados para P04.

Después cambia solo `LATENT_DIM=32` por `16` y compara el comportamiento.

## Preguntas

1. ¿Por qué se usa `fake.detach()` al entrenar D?
2. ¿Por qué las losses no bastan para juzgar la calidad generativa?
3. ¿Para qué sirve `fixed_noise`?
4. ¿Qué señales podrían sugerir mode collapse?
