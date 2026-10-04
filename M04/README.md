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
diagnóstico de diversidad y cobertura
      ↓
tiny diffusion
      ↓
VisualProvider en Enterprise GenAI Assistant
      ↓
modelo visual real mediante Amazon Bedrock
```

## Entorno de laboratorio

Cada alumno trabaja desde un **SageMaker Space** con una instancia **`ml.t3.large`**, sin GPU.

Por ese motivo las prácticas locales están diseñadas para CPU:

- dataset `sklearn.datasets.load_digits`, disponible localmente;
- imágenes de 8×8;
- VAE, GAN y denoiser deliberadamente pequeños;
- sin descarga de datasets grandes;
- sin Stable Diffusion ni otros modelos grandes ejecutándose dentro del Space.

El objetivo de P01–P05 es comprender mecanismos y poder observar el entrenamiento. En P06 se añade un provider visual real mediante **Amazon Bedrock**: el cálculo pesado ocurre en el servicio gestionado y el Space actúa como cliente de la API.

## Orden recomendado

```text
M04.P01 -> M04.P02 -> M04.P03 -> M04.P04 -> M04.P05 -> M04.P06
```

P03 y P04 trabajan sobre la misma GAN. P06 reutiliza el generador entrenado en P03 si está disponible y mantiene también un provider mock para probar arquitectura y tests sin depender de un modelo externo.

## Continuidad del proyecto transversal

M04.P06 construye **Enterprise GenAI Assistant v0.4** como evolución de v0.3. La capacidad visual no debe eliminar el endpoint de borradores, el router ni los controles deterministas construidos en módulos anteriores.

## Material

- `M04_P01_Enunciado.md`
- `M04_P02_Enunciado.md`
- `M04_P03_Enunciado.md`
- `M04_P04_Enunciado.md`
- `M04_P05_Enunciado.md`
- `M04_P06_Enunciado.md`
- `notebooks/`
- `enterprise-genai-assistant/`
