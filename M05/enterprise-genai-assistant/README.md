# Enterprise GenAI Assistant — M05

La versión M05 añade un subsistema de NLP desacoplado del proveedor.

## Providers

```text
mock
local_seq2seq
local_chat
```

## Endpoints

```text
POST /v1/text
POST /v1/chat
```

## Principios

- policy fuera del modelo;
- límites de input/output;
- chat template propio del tokenizer/modelo;
- historial de laboratorio en memoria;
- metadatos de tokens;
- salida validada con Pydantic.

## Ejecución

```bash
pytest -q
uvicorn src.main:app --reload --port 8080
```

Los providers locales descargan los checkpoints desde el entorno de laboratorio la primera vez si no han sido precargados.
