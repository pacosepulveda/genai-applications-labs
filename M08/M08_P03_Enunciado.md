# M08.P03 — Plataforma mínima y observabilidad

**Modalidad:** individual o equipos pequeños  
**Entregable:** capability split y contrato de observabilidad seguro

## Objetivo

Decidirás qué capacidades conviene compartir entre productos y qué ownership
debe permanecer cerca del caso de uso.

## Material

```text
assets/platform_capabilities.csv
assets/trace_samples.jsonl
notebooks/M08_P03_Platform_Observability.ipynb
```

## Parte A — Shared vs product-owned

Clasifica cada capacidad como:

```text
SHARED_PLATFORM
PRODUCT_OWNED
SHARED_WITH_PRODUCT_OWNER
```

Considera:

- repetición entre equipos;
- necesidad de estandarización;
- sensibilidad al dominio;
- riesgo de convertir Platform en bottleneck.

## Parte B — Golden path

Selecciona las capacidades mínimas que formarían un golden path:

```text
model access
CI/CD
eval tooling
observability
secrets
```

No diseñes una plataforma completa imaginaria.

## Parte C — Model gateway

Define qué debería centralizar:

```text
auth
routing
logging
cost attribution
approved models
```

y qué responsabilidades operativas introduce.

## Parte D — Trace contract

A partir de las trazas de ejemplo decide qué conservar, redactar o eliminar.

Como mínimo considera:

```text
trace_id
model_id
prompt_version
source_ids
tool_calls
tokens
latency
outcome
```

## Parte E — Privacy by design

Marca campos sensibles y define:

```text
redaction
retention
access_control
```

## Preguntas

1. ¿Por qué compartir RAG no transfiere el ownership del corpus?
2. ¿Qué convierte al model gateway en una dependencia crítica?
3. ¿Qué dato de una traza ayuda a depurar sin necesidad de almacenar el prompt completo?
4. ¿Qué capacidades deben seguir cerca del product squad?
