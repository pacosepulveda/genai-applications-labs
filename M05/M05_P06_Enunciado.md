# M05.P06 — Enterprise GenAI Assistant v0.5: TextModelProvider y conversación

**Modalidad:** individual o parejas  
**Entregable:** ampliación v0.5 de la API, provider textual desacoplado, conversación y tests

## Objetivo

Ampliarás la aplicación transversal. **v0.5 extiende v0.4; no la sustituye.**

Al terminar deben seguir existiendo las capacidades anteriores, incluyendo el routing y la generación visual, y se añaden:

```text
POST /v1/text
POST /v1/chat
```

La nueva rama textual será:

```text
request
  ↓
text policy
  ↓
task selection
  ↓
TextModelProvider
      ├── mock
      ├── local_seq2seq
      ├── local_chat
      └── bedrock_luna
  ↓
output validation
  ↓
response
```

## Parte A — Continuidad de v0.4

Conserva la implementación completada en los módulos anteriores.

No elimines ni debilites:

- `/v1/draft`;
- `/v1/images`;
- router clásico/neural;
- políticas de clasificación, prompt injection y material sensible;
- `VisualProvider`;
- almacenamiento y metadatos visuales.

El directorio `enterprise-genai-assistant/` de este módulo incluye el scaffold acumulativo. Los bloques marcados como heredados deben sustituirse por tu implementación completada de los módulos anteriores cuando corresponda.

## Parte B — TextModelProvider

Completa:

```text
src/text_provider.py
```

Implementa una interfaz común.

### `mock`

No utiliza ningún modelo.

### `local_seq2seq`

Utiliza:

```text
google/flan-t5-small
```

para:

- `SUMMARIZE`;
- `TRANSLATE`;
- instrucciones texto-a-texto.

### `local_chat`

Utiliza:

```text
HuggingFaceTB/SmolLM2-135M-Instruct
```

y el `chat_template` del tokenizer.

### `bedrock_luna`

Utiliza Amazon Bedrock Runtime desde el SageMaker Execution Role:

```text
region: us-east-1
model:  us.openai.gpt-5.6-luna
```

No guardes access keys, bearer tokens ni secretos en el repositorio.

El provider debe utilizar la API Converse de Bedrock y devolver el mismo `GenerationResult` que los providers locales.

## Parte C — API de texto

Completa:

```text
POST /v1/text
```

Petición conceptual:

```json
{
  "task": "SUMMARIZE",
  "text": "...",
  "provider": "local_seq2seq",
  "max_new_tokens": 120
}
```

La respuesta debe incluir:

```text
request_id
provider
model
task
input_tokens
output_tokens
finish_reason
latency_ms
```

## Parte D — Chat

Implementa:

```text
POST /v1/chat
```

con:

```text
conversation_id
message
provider
```

El servidor mantendrá historial **en memoria** exclusivamente para el laboratorio.

No lo presentes como memoria empresarial.

## Parte E — Chat template

`local_chat` debe construir la conversación mediante:

```python
tokenizer.apply_chat_template(...)
```

No concatenes manualmente marcas de roles.

`bedrock_luna` recibe los mensajes mediante el contrato de Converse; no necesita el chat template de SmolLM2.

## Parte F — Context policy

La conversación parte de un system message configurado por la aplicación.

Define un máximo de mensajes.

Si se supera:

```text
conservar system + últimos turnos
```

y devuelve:

```text
history_truncated=true
```

## Parte G — Salida estructurada

La API debe devolver objetos Pydantic validados, no el texto crudo del modelo.

## Parte H — Políticas

Mantén fuera del LLM al menos:

- tamaño máximo de input;
- clasificación de datos;
- controles deterministas heredados;
- providers permitidos;
- límite de output.

Cambiar de provider no puede saltarse una política.

## Parte I — Tests

Añade pruebas para:

1. provider mock;
2. provider desconocido;
3. límite de input;
4. historial de conversación;
5. truncation preservando system;
6. metadatos de tokens;
7. metadata `request_id` y `latency_ms`;
8. `bedrock_luna` mediante mock/stub del cliente: los tests no deben realizar llamadas reales ni generar coste;
9. regresión de controles heredados.

## Preguntas finales

1. ¿Qué diferencia hay entre historial y memoria externa?
2. ¿Qué parte de la aplicación depende del proveedor?
3. ¿Por qué el chat template pertenece al tokenizer/modelo local?
4. ¿Qué cambia al pasar del provider local a Luna en Bedrock?
5. ¿Qué permanece igual aunque cambie el provider?
6. ¿Qué falta todavía para contestar preguntas basadas en documentos corporativos autorizados?

La última pregunta conduce directamente a M06: **retrieval y RAG**.
