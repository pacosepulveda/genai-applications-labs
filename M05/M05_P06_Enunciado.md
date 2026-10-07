# M05.P06 — Enterprise GenAI Assistant v0.5

**Ruta esencial**

## Objetivo

Analizarás una aplicación textual completa con policy, provider abstraction, límites y metadatos. El código ya está implementado: la práctica consiste en ejecutarlo, cambiar configuración y comprobar que el contrato permanece estable.

Trabaja en:

```text
M05/enterprise-genai-assistant/
```

## Parte A — Validación

Ejecuta:

```bash
pip install -r requirements.txt
python -m pytest -q
```

Todos los tests normales utilizan `mock` o stubs; no hacen una llamada real a Bedrock.

## Parte B — API con mock

Arranca:

```bash
uvicorn src.main:app --reload --port 8080
```

Desde `/docs`, ejecuta `POST /v1/text` con:

```json
{
  "task": "SUMMARIZE",
  "text": "El servicio estuvo degradado durante veinte minutos. No hubo pérdida de datos.",
  "provider": "mock",
  "max_new_tokens": 80
}
```

Inspecciona:

```text
provider
model
input_tokens
output_tokens
finish_reason
request_id
latency_ms
```

## Parte C — Límites y policy

1. Reduce `max_new_tokens`.
2. Prueba un input vacío o demasiado grande.
3. Prueba un texto con un patrón que la policy bloquee.
4. Comprueba que el modelo no decide por sí mismo estas reglas.

## Parte D — Cambio de provider

Si el entorno tiene acceso a Bedrock, repite una petición con:

```text
provider=bedrock_luna
```

El endpoint y el modelo de respuesta no cambian. Solo cambia la implementación del provider.

## Parte E — Conversación

Como ampliación, prueba `/v1/chat` con el mismo `conversation_id` en dos mensajes y observa el historial/truncation.

## Preguntas

1. ¿Qué cambia al pasar de `mock` a `bedrock_luna`?
2. ¿Qué permanece estable?
3. ¿Por qué policy se ejecuta antes de inferencia?
4. ¿Por qué `max_new_tokens` debe estar limitado por la aplicación?
5. ¿Qué falta para responder con documentación corporativa autoritativa?
