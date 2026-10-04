# M04.P06 — Enterprise GenAI Assistant v0.4: Visual Generation Service

**Modalidad:** individual o parejas  
**Entregable:** API visual multi-provider, almacenamiento de artefactos y tests

## Objetivo

Añadirás una capacidad visual a **Enterprise GenAI Assistant v0.3** sin eliminar las capacidades anteriores y sin acoplar la aplicación a un proveedor concreto.

La arquitectura de laboratorio será:

```text
POST /v1/images
      ↓
visual policy
      ↓
VisualProvider
      ├── mock
      ├── local_gan
      └── bedrock
      ↓
ArtifactStore
      ↓
metadata
```

El laboratorio utiliza un flujo síncrono para mantener la implementación observable. Las colas y jobs asíncronos vistos en las slides son un patrón de producción, no un requisito de esta práctica.

## Parte 0 — Conserva v0.3

Parte de tu implementación completada en M03.

La v0.4 debe seguir conservando:

- `POST /v1/draft`;
- router clásico/neural;
- políticas deterministas de M03;
- tests de regresión de esas políticas.

Si utilizas el scaffold de M04, traslada tu implementación resuelta de v0.3 y sus artefactos en lugar de reimplementar el módulo anterior.

## Parte A — Contrato de generación

La petición incluirá:

```json
{
  "prompt": "a minimal blue robot on a white background",
  "provider": "mock",
  "seed": 42
}
```

El campo `prompt` forma parte del contrato común:

- `mock` lo acepta para mantener la interfaz;
- `local_gan` no lo interpreta porque la GAN de P03 es incondicional;
- `bedrock` lo utiliza como condición de generación.

## Parte B — VisualProvider

Completa:

```text
src/visual_provider.py
```

Mantén una interfaz común para:

- `MockVisualProvider`;
- `LocalGANProvider`;
- `BedrockVisualProvider`.

### LocalGANProvider

Debe cargar:

```text
artifacts/generator.pt
artifacts/gan_config.json
```

y ejecutar inferencia en CPU.

### BedrockVisualProvider

Utiliza `boto3` y `bedrock-runtime`.

La configuración del modelo y de la región debe salir de settings/env, no quedar repartida por el código:

```text
BEDROCK_IMAGE_REGION
BEDROCK_IMAGE_MODEL_ID
```

El scaffold deja preparada la forma de la petición. Completa la invocación, decodifica la imagen devuelta y conviértela a `PIL.Image`.

No guardes credenciales en el repositorio. El código utiliza las credenciales temporales/rol disponibles en el entorno AWS.

## Parte C — Artifact storage

Cada generación debe producir:

```text
generated/<artifact_id>.png
generated/<artifact_id>.json
```

Los metadatos deben incluir como mínimo:

```text
artifact_id
provider
model_version
seed
width
height
created_at
```

Para un provider gestionado registra también el identificador de modelo utilizado por la aplicación.

No guardes secretos ni credenciales.

## Parte D — API

Completa:

```text
POST /v1/images
GET  /v1/images/{artifact_id}
```

El primer endpoint genera el artefacto.

El segundo devuelve metadatos.

La carpeta `generated/` se expone como contenido estático para visualizar las imágenes desde el navegador.

## Parte E — Política

La política debe ejecutarse **antes** de seleccionar/invocar el provider.

Esta versión debe rechazar:

- prompts vacíos;
- providers desconocidos;
- las siguientes categorías simplificadas del laboratorio:
  - solicitud explícita de suplantar a una persona real;
  - generación de credenciales de acceso;
  - creación de un documento oficial falso.

No estamos construyendo un moderador de producción. Estas reglas demuestran que la política debe existir fuera del modelo y que cambiar de backend no puede saltársela.

## Parte F — Tests

Ejecuta:

```bash
pytest -q
```

Añade pruebas para:

1. provider mock;
2. provider inexistente;
3. reproducibilidad básica con seed donde aplique;
4. creación de metadata;
5. rechazo por política;
6. que los tests de política/routing heredados de v0.3 siguen pasando.

Los tests normales **no deben realizar una llamada real a Bedrock**. Mockea esa frontera y reserva la llamada real para una prueba manual de integración.

## Preguntas finales

1. ¿Por qué el GAN local no debería interpretar el prompt?
2. ¿Qué diferencia arquitectónica existe entre ejecutar `local_gan` y llamar a `bedrock`?
3. ¿Por qué devolvemos `artifact_id` en lugar de insertar la imagen como base64 en JSON?
4. ¿Por qué una v0.4 no debería perder los controles de v0.3?
5. ¿Qué partes de esta arquitectura seguirían siendo válidas si mañana cambiamos de modelo visual o proveedor cloud?
