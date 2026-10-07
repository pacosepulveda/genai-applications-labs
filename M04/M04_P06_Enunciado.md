# M04.P06 — Enterprise GenAI Assistant v0.4: servicio visual multi-provider

**Modalidad:** individual o parejas  
**Entregable:** ejecución, pruebas y análisis de una API visual

## Objetivo

Integrar generación de imágenes detrás de un contrato de aplicación:

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

En esta práctica el código está **completo**. El trabajo consiste en ejecutarlo, inspeccionarlo, modificar configuración y comprobar los controles.

## Parte A — Tests

```bash
cd M04/enterprise-genai-assistant
python -m pytest -q
```

Revisa especialmente los tests de visual policy, provider, almacenamiento y endpoint visual.

## Parte B — Arrancar la API

```bash
uvicorn src.main:app --reload --port 8080
```

Abre `/docs`.

## Parte C — Provider mock

Ejecuta `POST /v1/images` con:

```json
{
  "prompt": "a minimal blue robot on a white background",
  "provider": "mock",
  "seed": 42
}
```

Comprueba `artifact_id`, provider, model version, seed, dimensiones, URL de imagen y URL de metadata.

Repite con otra seed y compara el artefacto.

## Parte D — Policy

Prueba una solicitud permitida y otra que active una regla del laboratorio.

Localiza dónde se bloquea la petición y confirma que el provider no es quien decide la política de negocio.

## Parte E — Provider abstraction

Inspecciona `src/visual_provider.py`.

Explica por qué el endpoint no tiene que cambiar al sustituir `mock` por otro backend.

## Parte F — Bedrock

La integración `bedrock` está implementada.

Si el entorno dispone de acceso al modelo visual configurado, cambia `VISUAL_PROVIDER=bedrock` y realiza una prueba.

Si el modelo visual no está habilitado, la práctica esencial termina con `mock`: policy, provider abstraction, API, almacenamiento y metadata ya se han validado.

## Experimento

Modifica únicamente uno de estos elementos:

- seed;
- provider;
- prompt.

Antes de ejecutar, predice qué campos de la respuesta deberían cambiar y cuáles deberían permanecer estables.

## Preguntas finales

1. ¿Por qué la policy se ejecuta antes del provider?
2. ¿Qué ventaja aporta `VisualProvider`?
3. ¿Por qué guardar metadata junto al artefacto?
4. ¿Qué campos ayudan a reproducir o auditar una generación?
5. ¿Qué partes de la aplicación deberían permanecer estables al cambiar de modelo?
