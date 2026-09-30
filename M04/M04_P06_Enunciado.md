# M04.P06 — Enterprise GenAI Assistant v0.4: Visual Generation Service

**Modalidad:** individual o parejas  
**Entregable:** API visual con provider desacoplado, almacenamiento de artefactos y tests

## Objetivo

Añadirás una capacidad visual a la aplicación transversal sin acoplarla a un proveedor concreto.

La arquitectura será:

```text
POST /v1/images
      ↓
visual policy
      ↓
VisualProvider
      ├── mock
      └── local_gan
      ↓
artifact storage
      ↓
metadata
```

## Parte A — Contrato de generación

La petición incluirá:

```json
{
  "prompt": "synthetic digit",
  "provider": "mock",
  "seed": 42
}
```

En esta versión el GAN local no entiende lenguaje. El campo `prompt` se conserva porque forma parte del contrato futuro del servicio.

## Parte B — VisualProvider

Completa:

```text
src/visual_provider.py
```

Implementa una interfaz común para:

- `MockVisualProvider`;
- `LocalGANProvider`.

`LocalGANProvider` debe cargar:

```text
artifacts/generator.pt
artifacts/gan_config.json
```

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

No guardes secretos ni credenciales.

## Parte D — API

Completa:

```text
POST /v1/images
GET  /v1/images/{artifact_id}
```

El primer endpoint genera el artefacto.

El segundo devuelve metadatos.

La carpeta `generated/` se expondrá como contenido estático para visualizar las imágenes desde el navegador.

## Parte E — Política

Esta versión debe rechazar:

- prompts vacíos;
- providers desconocidos;
- las siguientes categorías simplificadas del laboratorio:
  - solicitud explícita de **suplantar a una persona real**;
  - generación de **credenciales de acceso**;
  - creación de un **documento oficial falso**.

No estamos construyendo un moderador de producción. Estas reglas sirven para demostrar que la política debe existir fuera del modelo y ejecutarse antes de invocarlo.

## Parte F — Tests

Ejecuta:

```bash
pytest -q
```

Añade pruebas para:

1. provider mock;
2. provider inexistente;
3. reproducibilidad básica con seed;
4. creación de metadata;
5. rechazo por política.

## Preguntas finales

1. ¿Por qué el GAN local no debería interpretar el prompt?
2. ¿Qué tendría que cambiar para soportar text-to-image?
3. ¿Por qué devolvemos `artifact_id` en lugar de insertar la imagen como base64 en JSON?
4. ¿Qué información añadirías para auditoría empresarial?
5. ¿Qué partes de esta arquitectura seguirían siendo válidas si mañana cambiamos a un servicio gestionado?
