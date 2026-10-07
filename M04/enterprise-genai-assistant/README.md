# Enterprise GenAI Assistant — M04

La aplicación está completa para que la práctica se centre en ejecución, pruebas y arquitectura.

## Ruta esencial

```bash
python -m pytest -q
uvicorn src.main:app --reload --port 8080
```

Abre `/docs` y prueba `POST /v1/images`.

Por defecto:

```text
VISUAL_PROVIDER=mock
```

El mock permite validar sin servicios externos:

```text
request -> visual policy -> provider -> ArtifactStore -> PNG + metadata
```

## Bedrock

También existe `BedrockVisualProvider`.

La llamada real requiere que el entorno tenga permisos y acceso al modelo visual configurado. No es necesaria para completar la ruta esencial.

## Continuidad

La aplicación conserva componentes de módulos anteriores, pero el endpoint visual usa carga independiente y no necesita artefactos del router para probarse.
