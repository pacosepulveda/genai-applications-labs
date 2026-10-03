# Enterprise GenAI Assistant — M01

Primera vertical funcional del proyecto transversal. En M01 no incorpora RAG ni herramientas.

## Entorno

La aplicación está preparada para ejecutarse en el **entorno web de laboratorio** facilitado para el curso. No es necesario instalar Python, Git, Docker ni un IDE en el equipo del alumno.

Desde el terminal integrado:

```bash
uvicorn src.main:app \
  --reload \
  --host 0.0.0.0 \
  --port 8080 \
  --root-path /jupyterlab/default/proxy/8080
```

En SageMaker Studio, abre Swagger UI mediante el proxy de JupyterLab:

```text
/jupyterlab/default/proxy/8080/docs
```

Si estás visualizando este README desde JupyterLab, puedes usar directamente:

[Abrir Swagger UI](/jupyterlab/default/proxy/8080/docs)

Mantén el terminal con Uvicorn en ejecución mientras utilizas la API.

## Modo mock

`GENAI_PROVIDER=mock` permite ejecutar y probar la arquitectura sin credenciales ni llamadas externas.

## Provider compatible con Responses API

Cuando el entorno incluya acceso a un modelo real, la configuración puede utilizar:

```text
GENAI_PROVIDER=openai
OPENAI_API_KEY=...
OPENAI_MODEL=...
OPENAI_BASE_URL=...
```

Estas variables permiten utilizar un endpoint compatible con la Responses API sin acoplar la aplicación a un único proveedor.

Las credenciales deben inyectarse desde el entorno de laboratorio y nunca guardarse en el repositorio.
