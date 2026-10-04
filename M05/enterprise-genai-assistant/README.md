# Enterprise GenAI Assistant — M05

M05 convierte la aplicación en **v0.5**. Esta versión amplía v0.4 y no elimina capacidades anteriores.

## Capacidades heredadas

```text
POST /v1/draft
POST /v1/images
```

Se conservan routing, políticas deterministas, `VisualProvider` y almacenamiento visual.

## Nuevas capacidades NLP

```text
POST /v1/text
POST /v1/chat
```

## Text providers

```text
mock
local_seq2seq
local_chat
bedrock_luna
```

`bedrock_luna` usa Amazon Bedrock Runtime con:

```text
BEDROCK_TEXT_REGION=us-east-1
BEDROCK_TEXT_MODEL_ID=us.openai.gpt-5.6-luna
```

Las credenciales proceden del SageMaker Execution Role. No se guardan claves en `.env`.

## Principios

- policy fuera del modelo;
- límites de input/output;
- chat template propio del tokenizer/modelo local;
- historial de laboratorio en memoria;
- metadatos de tokens, latencia y stop reason;
- salida validada con Pydantic;
- regresión: una capacidad nueva no elimina controles anteriores.

## Entorno

```text
SageMaker Space
ml.t3.large
CPU
sin GPU
```

Se recomienda precargar antes de la sesión los checkpoints/tokenizers locales utilizados por P01–P06.

## Ejecución

```bash
python -m pytest -q
uvicorn src.main:app --reload --port 8080
```

Los providers locales pueden descargar checkpoints la primera vez si no han sido precargados. Los tests no deben realizar llamadas reales a Bedrock.
