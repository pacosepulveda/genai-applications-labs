# M01.P03 — Enterprise GenAI Assistant v0.1

**Duración:** 55 minutos  
**Modalidad:** individual o parejas  
**Entregable:** API funcionando + pruebas superadas

## Objetivo

Construirás la primera versión funcional del proyecto transversal del curso: **Enterprise GenAI Assistant**.

Esta versión **no tiene RAG, no consulta documentación corporativa y no ejecuta herramientas**. Eso es deliberado. El objetivo es comprender qué partes necesita una aplicación empresarial además del modelo.

La aplicación expondrá:

- `GET /health`
- `POST /v1/draft`
- documentación OpenAPI automática en `/docs`

Y aplicará el siguiente flujo:

```text
request
  -> validación de esquema
  -> política determinista
  -> prompt del sistema
  -> provider de modelo
  -> respuesta estructurada
  -> metadatos y logging
```

## Parte A — Preparar el entorno

Desde `M01/enterprise-genai-assistant`:

```bash
python -m venv .venv
```

Activa el entorno virtual y ejecuta:

```bash
pip install -r requirements.txt
```

Copia la configuración:

```bash
cp .env.example .env
```

En PowerShell:

```powershell
Copy-Item .env.example .env
```

La configuración inicial utiliza:

```text
GENAI_PROVIDER=mock
```

No necesitas ninguna API key.

## Parte B — Comprender la arquitectura

Revisa estos archivos:

```text
src/main.py
src/models.py
src/settings.py
src/policy.py
src/prompts.py
src/providers/
```

Identifica cuál corresponde a:

1. interfaz de aplicación;
2. contrato de datos;
3. configuración;
4. reglas deterministas;
5. instrucciones al modelo;
6. abstracción del proveedor de IA.

## Parte C — Completar los controles mínimos

Busca los bloques `TODO M01.P03` en:

- `src/policy.py`
- `src/prompts.py`

Implementa estas reglas:

1. `CONFIDENTIAL` y `RESTRICTED` deben bloquearse en esta versión formativa.
2. Si `requires_authoritative_sources=true`, la petición debe bloquearse porque v0.1 todavía no dispone de fuentes autorizadas ni RAG.
3. El prompt del sistema debe indicar que:
   - la salida es un borrador;
   - no debe inventar acceso a fuentes corporativas;
   - debe marcar supuestos o incertidumbre;
   - no debe afirmar que una decisión ha sido aprobada por una persona u organización si la entrada no lo demuestra.

## Parte D — Ejecutar pruebas

```bash
pytest -q
```

Antes de continuar, las pruebas de P03 deben pasar.

## Parte E — Ejecutar la API

```bash
uvicorn src.main:app --reload --port 8080
```

Abre:

```text
http://localhost:8080/docs
```

Prueba una petición válida:

```json
{
  "task": "Redacta un borrador de comunicado técnico sobre una ventana de mantenimiento.",
  "audience": "equipo técnico",
  "confidentiality": "INTERNAL",
  "requires_authoritative_sources": false
}
```

Después prueba:

```json
{
  "task": "Indica cuál es la política corporativa vigente de retención de logs.",
  "audience": "administradores",
  "confidentiality": "INTERNAL",
  "requires_authoritative_sources": true
}
```

Explica por qué la segunda petición debe bloquearse aunque un LLM pudiera producir una respuesta plausible.

## Parte F — Provider real opcional

Si el instructor proporciona acceso a un modelo compatible, configura:

```text
GENAI_PROVIDER=openai
OPENAI_API_KEY=...
OPENAI_MODEL=...
```

`OPENAI_BASE_URL` es opcional y puede utilizarse cuando exista un endpoint compatible aprobado para el laboratorio.

> Nunca subas `.env` ni claves al repositorio.

## Parte G — Docker opcional

```bash
docker build -t enterprise-genai-assistant:m01 .
docker run --rm -p 8080:8080 --env-file .env enterprise-genai-assistant:m01
```

Comprueba de nuevo `/health` y `/docs`.

## Preguntas finales

1. ¿Dónde está el modelo y dónde está la aplicación?
2. ¿Qué controles son deterministas?
3. ¿Qué parte es probabilística?
4. ¿Por qué no almacenamos por defecto el texto completo del prompt en los logs?
5. ¿Qué falta para poder responder de forma fiable sobre documentación interna?
