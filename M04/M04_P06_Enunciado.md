# M04.P06 — Enterprise GenAI Assistant v0.4: Visual Generation Service

**Modalidad:** individual o parejas  
**Entregable:** endpoint de generación visual con provider abstraction, política, almacenamiento de artefactos y tests

## Objetivo

Añadirás una capacidad visual a **Enterprise GenAI Assistant** utilizando un contrato común para distintos backends.

La arquitectura será:

```text
POST /v1/images
      ↓
visual policy
      ↓
VisualProvider
      ├── mock
      └── bedrock
      ↓
ArtifactStore
      ↓
PNG + metadata
```

La práctica no depende de haber entrenado previamente un VAE, una GAN o un modelo de diffusion. El objetivo es llevar la generación visual al nivel de **aplicación**.

## Parte 0 — Preparación

Trabaja en:

```text
M04/enterprise-genai-assistant/
```

Instala las dependencias si el entorno todavía no las tiene:

```bash
pip install -r requirements.txt
```

La práctica se centra en los endpoints visuales. No necesitas completar tareas pendientes del endpoint `/v1/draft` para poder realizarla.

## Parte A — Contrato de generación

La petición utiliza:

```json
{
  "prompt": "a minimal blue robot on a white background",
  "provider": "mock",
  "seed": 42
}
```

El contrato debe ser el mismo con ambos providers.

- `mock` crea una imagen determinista y permite probar la aplicación sin una llamada externa;
- `bedrock` utiliza el prompt como condición para un modelo visual gestionado.

## Parte B — Política visual

Completa:

```text
src/visual_policy.py
```

La política se ejecuta **antes** de invocar un provider.

Mantén los controles ya preparados para:

- prompt vacío;
- provider desconocido.

Añade reglas educativas sencillas para bloquear solicitudes explícitas de:

- suplantar a una persona real;
- generar credenciales de acceso;
- crear un documento oficial falso.

No estamos construyendo un sistema de moderación de producción. El objetivo es demostrar que la política pertenece a la aplicación y no al modelo.

## Parte C — VisualProvider

Completa:

```text
src/visual_provider.py
```

La interfaz común es:

```python
generate(prompt, seed) -> VisualResult
```

### MockVisualProvider

Ya está implementado.

Utilízalo primero para comprobar el flujo completo sin depender de un modelo externo.

### BedrockVisualProvider

Completa la invocación al runtime:

```text
boto3
bedrock-runtime
```

La región y el identificador del modelo proceden de settings/env:

```text
BEDROCK_IMAGE_REGION
BEDROCK_IMAGE_MODEL_ID
```

No guardes access keys en el repositorio. El SDK debe utilizar las credenciales temporales o el rol disponibles en el entorno AWS.

Decodifica la imagen devuelta y conviértela a `PIL.Image`.

## Parte D — Selección del provider

Completa:

```python
build_visual_provider(...)
```

Debe aceptar:

```text
mock
bedrock
```

Un valor distinto debe producir `ValueError`.

## Parte E — API y ArtifactStore

Completa el flujo de:

```text
POST /v1/images
```

La secuencia debe ser:

1. determinar el provider;
2. evaluar la política;
3. construir el `VisualProvider`;
4. generar la imagen;
5. crear un `artifact_id`;
6. registrar metadata;
7. guardar PNG y JSON mediante `ArtifactStore`;
8. devolver `ImageGenerationResponse`.

Los metadatos deben incluir:

```text
artifact_id
provider
model_version
seed
width
height
created_at
```

La imagen queda disponible en:

```text
/generated/<artifact_id>.png
```

y los metadatos mediante:

```text
GET /v1/images/{artifact_id}
```

## Parte F — Validación con mock

Ejecuta:

```bash
pytest -q
uvicorn src.main:app --reload --port 8080
```

Desde `/docs`, genera una imagen con:

```json
{
  "prompt": "a minimal blue robot on a white background",
  "provider": "mock",
  "seed": 42
}
```

Comprueba:

- respuesta de la API;
- archivo PNG;
- archivo JSON;
- recuperación de metadatos.

Repite con la misma seed y observa qué parte del comportamiento es reproducible.

## Parte G — Provider gestionado

Si el entorno tiene acceso al modelo configurado, cambia el provider a:

```text
bedrock
```

y realiza una generación real.

Los tests normales no deben llamar a Bedrock. La invocación real se valida como prueba de integración desde el entorno del laboratorio.

## Preguntas finales

1. ¿Por qué el endpoint no debería cambiar cuando cambia el backend visual?
2. ¿Por qué la política se ejecuta antes de invocar el provider?
3. ¿Por qué guardamos una imagen como artefacto y devolvemos una URL en lugar de insertar base64 en toda la respuesta?
4. ¿Qué metadatos ayudan a reproducir o auditar una generación?
5. ¿Qué cambiaría en producción si una generación tardase muchos segundos y hubiera alta concurrencia?
