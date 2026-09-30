# Enterprise GenAI Assistant — M06

M06 añade:

```text
RAG obligatorio para conocimiento corporativo
structured output
validación de citas
tools read-only
agent
short-term state
```

## Modos

```text
DIRECT
RAG
AGENT
```

La aplicación mantiene estas rutas separadas deliberadamente.

## Regla de seguridad

Si la petición requiere fuentes autoritativas o es `CORPORATE_KNOWLEDGE`:

```text
RAG obligatorio
```

No se permite fallback directo al conocimiento paramétrico del modelo.

## Datos

La base documental de laboratorio se encuentra en:

```text
data/knowledge_base/
```

e incluye una versión obsoleta para comprobar filtrado de vigencia.

## Tests

```bash
pytest -q
```

Los tests deterministas no requieren invocar un modelo gestionado.

## Ejecución

Cuando completes los TODO:

```bash
uvicorn src.main:app --reload --port 8080
```

y abre `/docs` desde la vista web del entorno.
