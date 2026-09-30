# Módulo 4 — Visión Artificial Generativa

## Objetivos

Estas prácticas recorren las ideas fundamentales de la generación visual desde los píxeles hasta un servicio visual integrable en una aplicación empresarial.

La progresión es:

```text
imagen como tensor
      ↓
preprocessing y augmentation
      ↓
autoencoder / VAE
      ↓
espacio latente
      ↓
GAN
      ↓
diagnóstico y evaluación
      ↓
diffusion
      ↓
VisualProvider en Enterprise GenAI Assistant
```

## Entorno

Todos los laboratorios están diseñados para realizarse desde el entorno web facilitado por el instructor. No es necesario instalar herramientas en el ordenador del alumno.

Las prácticas base funcionan sobre CPU con imágenes pequeñas. Si el entorno dispone de GPU, PyTorch puede utilizarla automáticamente en los ejercicios de entrenamiento.

## Orden recomendado

```text
M04.P01 -> M04.P02 -> M04.P03 -> M04.P04 -> M04.P05 -> M04.P06
```

P03 y P04 trabajan sobre la misma GAN. P06 reutiliza el generador entrenado en P03 si está disponible, pero dispone también de un provider mock.

## Material

- `M04_P01_Enunciado.md`
- `M04_P02_Enunciado.md`
- `M04_P03_Enunciado.md`
- `M04_P04_Enunciado.md`
- `M04_P05_Enunciado.md`
- `M04_P06_Enunciado.md`
- `notebooks/`
- `enterprise-genai-assistant/`
