# Enterprise GenAI Assistant — M03

La versión M03 permite seleccionar un router clásico o neuronal mediante configuración:

```text
ROUTER_BACKEND=classic
```

o:

```text
ROUTER_BACKEND=neural
```

Los artefactos se generan en M03.P02.

## Principio de diseño

El backend de ML es intercambiable. Las políticas empresariales y de seguridad no dependen del modelo elegido.

## Ejecución

Desde el terminal integrado del entorno web:

```bash
pytest -q
uvicorn src.main:app --reload --port 8080
```

Utiliza la vista web del entorno para abrir `/docs`.
