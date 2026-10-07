# Enterprise GenAI Assistant — M05

La ruta principal de M05 añade un servicio textual desacoplado del backend.

```text
POST /v1/text
      ↓
text policy
      ↓
TextModelProvider
      ├── mock
      └── bedrock_luna
      ↓
TextResponse
```

## Configuración

```text
TEXT_PROVIDER=mock
MAX_INPUT_CHARS=12000
MAX_NEW_TOKENS=256
BEDROCK_TEXT_REGION=us-east-1
BEDROCK_TEXT_MODEL_ID=us.openai.gpt-5.6-luna
```

No guardes claves de acceso en `.env`.

## Ejecución

```bash
python -m pytest -q
uvicorn src.main:app --reload --port 8080
```

El provider `mock` permite completar los tests sin llamadas externas. La llamada real a Bedrock se reserva para una prueba manual de integración.

`/v1/chat` y los providers locales se consideran ampliación.
