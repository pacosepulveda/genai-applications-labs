# Enterprise GenAI Assistant — M04

La versión v0.4 **extiende v0.3**: mantiene la capacidad textual y añade generación visual mediante un contrato multi-provider.

## Capacidades

```text
/v1/draft
  └── routing + políticas de M03

/v1/images
  └── visual policy
      └── VisualProvider
          ├── mock
          ├── local_gan
          └── bedrock
```

## Entorno de laboratorio

El código se ejecuta desde un SageMaker Space `ml.t3.large` sin GPU.

- `local_gan` utiliza el Generator 8×8 creado en M04.P03 y ejecuta inferencia en CPU.
- `bedrock` llama a un modelo visual gestionado. El modelo grande no se ejecuta dentro del Space.
- `mock` permite probar API, política y almacenamiento sin dependencia externa.

## Configuración

Copia `.env.example` a `.env` cuando necesites personalizar valores.

```text
VISUAL_PROVIDER=mock
BEDROCK_IMAGE_REGION=us-west-2
BEDROCK_IMAGE_MODEL_ID=stability.sd3-5-large-v1:0
```

No guardes access keys en `.env`. En AWS el SDK debe utilizar las credenciales/rol proporcionados por el entorno.

## Continuidad desde M03

Conserva tu implementación completada de v0.3 y sus artefactos. El scaffold de M04 incluye los contratos y ficheros necesarios para mantener la funcionalidad anterior, pero no pretende resolver de nuevo las tareas de M03.

## API visual

```text
POST /v1/images
GET  /v1/images/{artifact_id}
```

Las imágenes generadas se sirven desde:

```text
/generated/<artifact_id>.png
```

## Ejecución

```bash
pytest -q
uvicorn src.main:app --reload --port 8080
```

En SageMaker Studio utiliza la vista web/proxy disponible para abrir `/docs`; no dependas de exponer `localhost` directamente al navegador del equipo del alumno.
