# M02.P05 — Enterprise GenAI Assistant v0.2: integrar el router ML

**Modalidad:** individual o parejas  
**Entregable:** API con routing ML, tests y metadatos de predicción

## Objetivo

Integrarás en la aplicación el pipeline entrenado en P02/P03.

La arquitectura pasa de:

```text
request -> policy -> provider
```

a:

```text
request
  -> validation
  -> intent router ML
  -> confidence policy
  -> deterministic policy
  -> provider / review / controlled flow
```

## Continuidad de controles

La v0.2 añade Machine Learning, pero no debe perder los controles deterministas ya trabajados. Se mantienen las restricciones de clasificación de datos y el bloqueo educativo de patrones evidentes de prompt injection y material que parece contener secretos o credenciales.

Además, una petición que marque `requires_authoritative_sources=true` **no puede terminar en generación libre**. En esta versión debe desviarse a un flujo controlado, aunque el clasificador proponga otra intención.

## Preparación

Trabaja en `enterprise-genai-assistant/`.

Comprueba que existe:

```text
artifacts/intent_router.joblib
```

Si no existe, vuelve a P02 y genera el artefacto.

## Parte A — Implementar `IntentRouter`

Completa los `TODO M02.P05` de:

```text
src/intent_router.py
```

Debe:

1. cargar el pipeline con `joblib`;
2. recibir los mismos campos utilizados durante entrenamiento;
3. ejecutar `predict_proba`;
4. devolver:
   - intención;
   - confianza.

## Parte B — Integración en FastAPI

Completa los `TODO M02.P05` de `src/main.py`.

La respuesta debe incluir:

```json
{
  "intent": "DRAFT",
  "confidence": 0.91,
  "route": "GENERATION"
}
```

## Parte C — Política de routing

Aplica estas reglas mínimas:

1. Si la política determinista de seguridad bloquea la petición, el ML no puede anular el bloqueo.
2. Si `requires_authoritative_sources=true`, utiliza `CONTROLLED_KNOWLEDGE_FLOW`.
3. Si `confidence < ROUTER_THRESHOLD`, utiliza `REVIEW`.
4. `CORPORATE_KNOWLEDGE` debe ir a `CONTROLLED_KNOWLEDGE_FLOW`.
5. `UNSUPPORTED` debe bloquearse.
6. Las demás clases pueden usar `GENERATION` en esta versión.

## Parte D — Pruebas

Ejecuta:

```bash
pytest -q
```

Añade al menos un test propio para comprobar un caso de baja confianza o una ruta controlada.

## Parte E — Observabilidad

Registra como metadatos, sin almacenar el texto completo:

```text
request_id
intent
confidence
route
model_version
latency_ms
```

## Preguntas finales

1. ¿Qué parte de la decisión es aprendida?
2. ¿Qué parte sigue siendo determinista?
3. ¿Por qué no debe el clasificador saltarse las políticas de seguridad?
4. ¿Qué necesitaríamos monitorizar para detectar degradación del router en producción?
5. ¿Cuándo sería necesario reentrenarlo?
