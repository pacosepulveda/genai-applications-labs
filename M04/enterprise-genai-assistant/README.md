# Enterprise GenAI Assistant — M04

Esta versión añade un servicio de generación visual con provider desacoplado.

## Providers

```text
mock
local_gan
```

`local_gan` utiliza los artefactos creados en M04.P03.

## API

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

Abre `/docs` utilizando la vista web del entorno de laboratorio.
