# M05.P06 — Enterprise GenAI Assistant v0.5: servicio NLP

**Modalidad:** individual o parejas  
**Entregable:** endpoint textual, provider abstraction y tests

## Objetivo

Convertirás la capacidad de generación de texto en un servicio de aplicación con un contrato estable.

La ruta principal será:

```text
POST /v1/text
      ↓
text policy
      ↓
task prompt
      ↓
TextModelProvider
      ├── mock
      └── bedrock_luna
      ↓
TextResponse
```

No necesitas entrenar un modelo ni cargar modelos locales para completar la ruta principal.

## Parte A — Contrato de entrada

El endpoint recibe una petición como:

```json
{
  "task": "SUMMARIZE",
  "text": "...",
  "provider": "mock",
  "max_new_tokens": 120
}
```

Las tareas soportadas son:

```text
GENERATE
SUMMARIZE
TRANSLATE
```

Para `TRANSLATE` debes recibir también `target_language`.

## Parte B — Policy antes del modelo

Antes de seleccionar o invocar el provider utiliza:

```text
src/text_policy.py
```

La aplicación debe rechazar, como mínimo:

- entrada vacía;
- input que supere el límite configurado;
- material marcado como `CONFIDENTIAL:` o `RESTRICTED:`;
- patrones deterministas de prompt injection definidos en el scaffold;
- material con apariencia de secreto según las reglas del laboratorio.

El provider nunca debe poder saltarse estos controles.

## Parte C — TextModelProvider

Completa:

```text
src/text_provider.py
```

La ruta principal utiliza dos providers.

### `mock`

Ya está implementado y permite comprobar la aplicación sin inferencia ni coste.

### `bedrock_luna`

Completa `BedrockLunaProvider.generate(...)` utilizando Amazon Bedrock Runtime y la API Converse.

Configuración:

```text
BEDROCK_TEXT_REGION=us-east-1
BEDROCK_TEXT_MODEL_ID=us.openai.gpt-5.6-luna
```

La llamada debe enviar:

- un mensaje `user`;
- `maxTokens` dentro de `inferenceConfig`.

Convierte la respuesta de Bedrock al contrato común `GenerationResult`:

```text
text
provider
model
input_tokens
output_tokens
finish_reason
```

No guardes credenciales en el repositorio.

## Parte D — Selección del provider

Completa `build_text_provider(...)` para soportar:

```text
mock
bedrock_luna
```

Un nombre desconocido debe producir `ValueError`.

## Parte E — Construcción de la tarea

Completa:

```text
POST /v1/text
```

Construye una instrucción distinta según la tarea:

- `GENERATE`: utiliza el texto como instrucción;
- `SUMMARIZE`: pide un resumen fiel y conciso;
- `TRANSLATE`: pide traducir al idioma indicado y conservar identificadores técnicos.

No necesitas implementar prompt engineering avanzado. Queremos una separación clara entre **tarea de aplicación** y **provider**.

## Parte F — Límite de salida

El cliente puede solicitar `max_new_tokens`, pero la aplicación debe imponer su máximo configurado.

Utiliza:

```python
min(req.max_new_tokens, settings.max_new_tokens)
```

Esto demuestra que un parámetro de generación también es un control operacional.

## Parte G — Respuesta estructurada

Devuelve un `TextResponse` validado por Pydantic con:

```text
output
provider
model
task
input_tokens
output_tokens
finish_reason
request_id
latency_ms
```

El objetivo es no tratar la salida del modelo como un string sin contexto operativo.

## Parte H — Tests

Ejecuta:

```bash
python -m pytest -q
```

Comprueba al menos:

1. provider `mock`;
2. provider desconocido;
3. input demasiado grande;
4. construcción del endpoint con `mock`;
5. metadatos de la respuesta;
6. límite de `max_new_tokens`;
7. `bedrock_luna` mediante un stub/mock del cliente, sin llamada real.

Los tests automatizados **no deben realizar llamadas reales a Bedrock**.

## Prueba manual de integración

Cuando los tests funcionen, cambia el provider a:

```text
bedrock_luna
```

y realiza una petición corta desde `/docs`.

Comprueba que recibes contenido y metadatos de uso.

## Ampliación

El scaffold conserva componentes para continuar experimentando con conversación y modelos locales.

Como ampliación puedes implementar:

- `/v1/chat`;
- historial en memoria;
- `local_seq2seq` con FLAN-T5-small;
- `local_chat` con SmolLM2 y `chat_template`.

Estas extensiones no son necesarias para completar la ruta principal del módulo.

## Preguntas finales

1. ¿Qué parte cambia al pasar de `mock` a `bedrock_luna`?
2. ¿Qué partes de la aplicación permanecen iguales aunque cambie el provider?
3. ¿Por qué la policy debe ejecutarse antes de llamar al modelo?
4. ¿Por qué `max_new_tokens` no es solo una preferencia estética?
5. ¿Por qué conviene devolver tokens, modelo, `request_id` y latencia junto al texto?
6. ¿Qué falta para contestar preguntas utilizando documentación corporativa autorizada y trazable?

La última pregunta conduce directamente a M06: **retrieval y RAG**.
