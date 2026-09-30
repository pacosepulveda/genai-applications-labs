# M05.P06 — Enterprise GenAI Assistant v0.5: TextModelProvider y conversación

**Modalidad:** individual o parejas  
**Entregable:** API textual, provider desacoplado, conversación y tests

## Objetivo

Añadirás una capa NLP real a la aplicación transversal.

La lógica será:

```text
request
  ↓
text policy
  ↓
task
  ↓
TextModelProvider
      ├── mock
      ├── local_seq2seq
      └── local_chat
  ↓
output validation
  ↓
response
```

## Parte A — TextModelProvider

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

## Parte B — API de texto

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

La respuesta debe incluir metadatos:

```text
provider
model
task
input_tokens
output_tokens
finish_reason
```

## Parte C — Chat

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

El servidor mantendrá un historial **en memoria** exclusivamente para el laboratorio.

No lo presentes como un mecanismo de memoria empresarial.

## Parte D — Chat template

`local_chat` debe construir la conversación mediante:

```python
tokenizer.apply_chat_template(...)
```

No concatenes manualmente marcas de roles.

## Parte E — Context policy

Define un máximo de mensajes.

Si se supera:

```text
conservar system + últimos turnos
```

y registrar que hubo truncation.

## Parte F — Salida estructurada

La API debe devolver un objeto Pydantic validado, no el texto crudo del modelo.

## Parte G — Políticas

Mantén fuera del LLM al menos:

- tamaño máximo de entrada;
- clasificación de datos simplificada;
- providers permitidos;
- límite de output.

## Parte H — Tests

Añade pruebas para:

1. provider mock;
2. provider desconocido;
3. límite de input;
4. historial de conversación;
5. truncation de historial;
6. metadatos de tokens.

## Preguntas finales

1. ¿Qué diferencia hay entre historial y memoria externa?
2. ¿Qué parte de la aplicación depende del proveedor?
3. ¿Por qué el chat template pertenece al tokenizer/modelo?
4. ¿Qué cambiaría al sustituir el provider local por Bedrock?
5. ¿Qué falta todavía para contestar preguntas basadas en documentos corporativos autorizados?

La respuesta a la última pregunta conduce directamente a M06: **retrieval y RAG**.
