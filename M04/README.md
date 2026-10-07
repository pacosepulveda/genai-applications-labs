# Módulo 4 — Visión Artificial Generativa

## Objetivos

El módulo introduce las ideas fundamentales de generación visual y termina llevando esa capacidad a una aplicación.

La ruta conceptual es:

```text
imagen como tensor
      ↓
modelar una distribución
      ↓
espacio latente / VAE
      ↓
GAN
      ↓
diffusion y conditioning
      ↓
evaluación, riesgo y procedencia
      ↓
VisualProvider + ArtifactStore
```

## Entorno de laboratorio

Cada alumno trabaja desde un **SageMaker Space** con una instancia **`ml.t3.large`**, sin GPU.

Los notebooks locales utilizan modelos y datasets pequeños para que puedan ejecutarse en CPU. Los modelos visuales grandes se consumen mediante un servicio gestionado, por lo que el cálculo pesado no se ejecuta dentro del Space.

## Ruta de trabajo recomendada

La práctica principal del módulo es:

```text
M04.P06 — Enterprise GenAI Assistant v0.4
```

En ella se construye el flujo:

```text
POST /v1/images
      ↓
visual policy
      ↓
VisualProvider
      ├── mock
      └── bedrock
      ↓
ArtifactStore
      ↓
PNG + metadata
```

Los laboratorios **M04.P01–M04.P05** permanecen disponibles como ampliación técnica para profundizar en:

- representación de imágenes;
- VAE y espacio latente;
- entrenamiento adversarial;
- evaluación de GAN;
- tiny diffusion.

No son una dependencia de M04.P06.

## Continuidad del proyecto transversal

M04.P06 añade generación visual a **Enterprise GenAI Assistant**. La práctica visual puede realizarse de forma independiente de los artefactos de entrenamiento de P01–P05.

El scaffold conserva también los componentes textuales de módulos anteriores. Para la práctica M04 no es necesario reimplementar el router neuronal ni completar tareas pendientes del módulo 3.

## Material

- `M04_P01_Enunciado.md` — ampliación
- `M04_P02_Enunciado.md` — ampliación
- `M04_P03_Enunciado.md` — ampliación
- `M04_P04_Enunciado.md` — ampliación
- `M04_P05_Enunciado.md` — ampliación
- `M04_P06_Enunciado.md` — práctica principal
- `notebooks/`
- `enterprise-genai-assistant/`
