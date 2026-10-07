# M06.P06 — Enterprise GenAI Assistant v0.6

**Ruta de clase** · aplicación completamente implementada

## Objetivo

Inspeccionar y validar una arquitectura con tres modos explícitos:

```text
request
  ↓
policy / routing
  ├── DIRECT
  ├── RAG
  └── AGENT
```

No tienes que implementar módulos ni copiar código. Trabajarás sobre `enterprise-genai-assistant/` ya funcional.

## Parte A — Tests

Desde el directorio de la aplicación ejecuta:

```bash
python -m pytest -q
```

Identifica qué tests comprueban routing, citas, documentos obsoletos y tools.

## Parte B — Routing

Inspecciona `choose_mode()` y comprueba:

```text
requires_authoritative_sources=true -> RAG
CORPORATE_KNOWLEDGE               -> RAG
resto                              -> DIRECT
```

Cambia una petición DIRECT para exigir fuentes autoritativas y observa el cambio de ruta.

## Parte C — RAG

Prueba `/v1/ask` con una pregunta sobre `PROC-017` y verifica que utiliza la versión vigente de **8 horas**, no la obsoleta de 24.

Fuerza una cita inventada en un test y comprueba que se rechaza.

## Parte D — NO_EVIDENCE

Pregunta por información no presente en el corpus. La aplicación debe responder sin evidencia suficiente y **no** hacer fallback a DIRECT.

## Parte E — AGENT

Prueba `/v1/operations` con `INC-2048` y observa el uso de tools read-only.

## Preguntas finales

- ¿Qué responsabilidad pertenece a policy y cuál al modelo?
- ¿Qué cambiaría al sustituir el vector store?
- ¿Qué cambiaría al sustituir Luna?
- ¿Por qué DIRECT, RAG y AGENT no deberían ocultarse detrás de un único flujo opaco?
