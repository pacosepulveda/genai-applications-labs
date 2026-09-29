# Enterprise GenAI Assistant — M01

Primera vertical funcional del proyecto transversal. En M01 no incorpora RAG ni herramientas.

## Entorno

La aplicación está preparada para ejecutarse en el **entorno web de laboratorio** facilitado para el curso. No es necesario instalar Python, Git, Docker ni un IDE en el equipo del alumno.

Desde el terminal integrado:

```bash
uvicorn src.main:app --reload --port 8080
```

Abre la vista web del puerto 8080 y accede a `/docs`.

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
