# M03.P06 — Enterprise GenAI Assistant v0.3: router intercambiable y gate de calidad

**Modalidad:** individual o parejas  
**Entregable:** API capaz de utilizar router clásico o neuronal y decisión de despliegue documentada

## Objetivo

Integrarás el router neuronal de P02 sin asumir que debe sustituir automáticamente al modelo clásico.

La aplicación soportará dos backends:

```text
classic
neural
```

seleccionados mediante configuración.

## Arquitectura

```text
request
  -> deterministic policy
  -> selected intent router
       ├── classic
       └── neural
  -> confidence policy
  -> routing policy
  -> generation / review / controlled flow / block
```

## Parte A — Artefactos

Comprueba que existen:

```text
artifacts/
├── classic_router.joblib
├── neural_preprocessor.joblib
├── neural_label_encoder.joblib
├── neural_router.pt
└── neural_router_config.json
```

## Parte B — Routers

Completa:

```text
src/routers.py
```

Debe proporcionar una interfaz común:

```python
predict(...) -> intent, confidence
```

para ambos modelos.

## Parte C — Configuración

La variable:

```text
ROUTER_BACKEND=classic
```

o:

```text
ROUTER_BACKEND=neural
```

debe seleccionar el modelo sin modificar la lógica de negocio.

## Parte D — Gate de calidad

Antes de elegir el router neuronal, utiliza el benchmark de P02.

Define criterios explícitos, por ejemplo:

- macro F1 mínimo;
- latencia máxima;
- degradación permitida por clase;
- coste operacional.

Documenta tu decisión:

```text
KEEP_CLASSIC
USE_NEURAL
CONTINUE_EXPERIMENT
```

## Parte E — Seguridad

Se mantienen las reglas de M01/M02:

- `CONFIDENTIAL` y `RESTRICTED` se bloquean antes del router;
- los patrones educativos de prompt injection directa siguen bloqueados;
- el material que parece contener secretos o credenciales sigue bloqueado;
- un modelo no puede anular un bloqueo determinista;
- `requires_authoritative_sources=true` -> `CONTROLLED_KNOWLEDGE_FLOW`;
- baja confianza -> `REVIEW`;
- `CORPORATE_KNOWLEDGE` -> `CONTROLLED_KNOWLEDGE_FLOW`;
- `UNSUPPORTED` -> `BLOCK`.

Cambiar `ROUTER_BACKEND` solo cambia el componente aprendido. Las políticas deterministas deben producir el mismo resultado con ambos backends.

## Parte F — Tests

Ejecuta:

```bash
pytest -q
```

Añade pruebas que confirmen que:

1. ambos backends cumplen la misma interfaz;
2. cambiar backend no cambia las políticas;
3. una petición confidencial se bloquea antes de cualquier decisión aprendida.

## Preguntas finales

1. ¿Qué ganaríamos sustituyendo el modelo clásico?
2. ¿Qué coste introduce la red?
3. ¿Cómo versionarías preprocesador, pesos y arquitectura?
4. ¿Qué ocurriría si desplegásemos pesos de una arquitectura distinta?
5. ¿Por qué un gate de calidad es preferible a desplegar “el modelo más moderno”?
