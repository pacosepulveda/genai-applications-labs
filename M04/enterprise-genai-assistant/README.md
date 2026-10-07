# Enterprise GenAI Assistant — M04

La versión M04 añade generación visual mediante un contrato de provider y almacenamiento de artefactos.

## Flujo visual

```text
/v1/images
  └── visual policy
      └── VisualProvider
          ├── mock
          └── bedrock
              ↓
          ArtifactStore
```

## Entorno

El código se ejecuta desde un SageMaker Space `ml.t3.large` sin GPU.

- `mock` permite probar API, política, seed y almacenamiento sin dependencia externa.
- `bedrock` llama a un modelo visual gestionado; el cálculo pesado no se ejecuta dentro del Space.

Los laboratorios locales de VAE, GAN y tiny diffusion son ampliaciones independientes y no son requisito para utilizar el servicio visual.

## Configuración

Copia `.env.example` a `.env` cuando necesites personalizar valores.

```text
VISUAL_PROVIDER=mock
BEDROCK_IMAGE_REGION=us-west-2
BEDROCK_IMAGE_MODEL_ID=stability.sd3-5-large-v1:0
```

No guardes access keys en `.env`. En AWS el SDK debe utilizar las credenciales o el rol proporcionados por el entorno.

## API visual

```text
POST /v1/images
GET  /v1/images/{artifact_id}
```

Las imágenes se sirven desde:

```text
/generated/<artifact_id>.png
```

## Componentes que debes completar

```text
src/visual_policy.py
src/visual_provider.py
src/main.py   # únicamente el endpoint visual
```

No es necesario completar tareas pendientes de `/v1/draft` para realizar M04.P06.

## Ejecución

```bash
pytest -q
uvicorn src.main:app --reload --port 8080
```

En SageMaker Studio utiliza la vista web/proxy disponible para abrir `/docs`.
