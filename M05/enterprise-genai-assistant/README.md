# Enterprise GenAI Assistant — M05

La aplicación está completamente implementada para utilizarla como laboratorio de ejecución, inspección y comparación.

## Providers

- `mock`
- `local_seq2seq`
- `local_chat`
- `bedrock_luna`

Los tests normales usan `mock` o stubs y no generan coste en Bedrock.

```bash
python -m pytest -q
uvicorn src.main:app --reload --port 8080
```
