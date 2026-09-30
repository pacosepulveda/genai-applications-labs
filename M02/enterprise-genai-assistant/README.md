# Enterprise GenAI Assistant — M02

Esta versión añade un **intent router de Machine Learning** al proyecto transversal.

## Flujo

```text
request
-> deterministic policy
-> ML intent router
-> confidence policy
-> route
-> provider / controlled flow / review
```

## Artefacto esperado

El notebook M02.P02 debe crear:

```text
artifacts/intent_router.joblib
```

## Ejecución

Desde el terminal integrado del entorno web:

```bash
pytest -q
uvicorn src.main:app --reload --port 8080
```

Abre `/docs` utilizando el mecanismo de vista web/puerto facilitado por el entorno de laboratorio.
