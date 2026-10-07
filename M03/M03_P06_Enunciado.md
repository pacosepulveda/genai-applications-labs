# M03.P06 — Enterprise GenAI Assistant v0.3 · ampliación

**Modalidad:** individual o parejas  
**Entregable:** ejecución de la API con router intercambiable y análisis del gate de calidad

## Objetivo

Observar cómo una aplicación puede cambiar entre `classic` y `neural` sin reescribir la política de negocio.

El código de `enterprise-genai-assistant/` está completo. No tienes que implementar `routers.py` ni `main.py`.

## Prerrequisito

Ejecuta P02 una vez para generar en `enterprise-genai-assistant/artifacts/` los archivos del router clásico y neuronal.

## Parte A — Tests

Desde `M03/enterprise-genai-assistant/` ejecuta:

```bash
pytest -q
```

## Parte B — Router clásico

Configura `ROUTER_BACKEND=classic`, arranca:

```bash
uvicorn src.main:app --reload --port 8080
```

y prueba `/health` y `/v1/draft`.

## Parte C — Router neuronal

Cambia únicamente a `ROUTER_BACKEND=neural`, reinicia la aplicación y repite los mismos casos.

## Parte D — Gate de calidad

Utiliza los resultados de P02 y decide entre:

```text
KEEP_CLASSIC
USE_NEURAL
CONTINUE_EXPERIMENT
```

## Comprobaciones

Verifica que cambiar backend no cambia estas reglas:

- `CONFIDENTIAL` y `RESTRICTED` se bloquean antes del router;
- baja confianza -> `REVIEW`;
- `requires_authoritative_sources=true` -> `CONTROLLED_KNOWLEDGE_FLOW`;
- `CORPORATE_KNOWLEDGE` -> `CONTROLLED_KNOWLEDGE_FLOW`;
- `UNSUPPORTED` -> `BLOCK`.

## Preguntas finales

1. ¿Qué componente cambia realmente con `ROUTER_BACKEND`?
2. ¿Por qué el modelo aprendido no puede anular una policy determinista?
3. ¿Qué archivos deben versionarse juntos?
4. ¿Por qué un gate de calidad es preferible a desplegar “el modelo más moderno”?
