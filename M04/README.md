# Módulo 4 — Visión Artificial Generativa

## Enfoque práctico

Los laboratorios de M04 se entregan con el código completo.

El trabajo del alumno es:

```text
ejecutar -> inspeccionar -> modificar una variable -> comparar -> explicar
```

El objetivo es evitar que errores de sintaxis o boilerplate consuman el tiempo destinado a comprender los mecanismos y la arquitectura.

## Ruta de clase

La práctica principal es:

```text
M04.P06 — Enterprise GenAI Assistant v0.4
```

P06 no depende de haber entrenado previamente VAE, GAN o diffusion. El provider `mock` permite comprobar policy, provider abstraction, API, almacenamiento y metadata de principio a fin.

## Ampliaciones ejecutables

- `M04.P01` — tensores, rangos y augmentations.
- `M04.P02` — VAE, sampling e interpolación.
- `M04.P03` — training loop GAN.
- `M04.P04` — diversidad, cobertura y mode collapse.
- `M04.P05` — tiny diffusion.

P01-P05 también están completamente resueltas en los notebooks y en `scripts/`. P04 reutiliza los artefactos generados por P03.

## Entorno

Los ejemplos utilizan CPU y datasets pequeños. No es necesaria GPU.

## Material

- `M04_P01_Enunciado.md` … `M04_P06_Enunciado.md`
- `notebooks/`
- `scripts/`
- `enterprise-genai-assistant/`
