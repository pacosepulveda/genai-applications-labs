# M04.P05 — Tiny Diffusion: del ruido al sampling

**Modalidad:** individual o parejas  
**Entregable:** interpretación del forward process y reverse sampling

## Objetivo

Observar la mecánica esencial de diffusion con un modelo pequeño que se ejecuta en CPU.

## Trabajo

Abre `notebooks/M04_P05_Tiny_Diffusion.ipynb`.

El código está completo e incluye schedule de ruido, `q_sample`, denoiser condicionado por timestep, entrenamiento para predecir `epsilon` y reverse sampling.

Ejecuta el notebook y observa los snapshots del proceso.

Después cambia `T=40` por `T=20` y compara el recorrido.

## Preguntas

1. ¿Qué representa `t`?
2. ¿Qué predice el denoiser?
3. ¿Por qué la generación necesita varios pasos?
4. ¿Qué diferencia conceptual ves frente al Generator de una GAN?
