# Módulo 5 — NLP Generativo

## Objetivo

M05 conecta el funcionamiento de un modelo de lenguaje con su integración en una aplicación:

```text
texto -> tokens/contexto -> Transformer -> logits -> decoding -> aplicación
```

## Formato de los laboratorios

Los notebooks y scripts están **completamente implementados**. No es necesario copiar código ni rellenar `TODOs`.

El trabajo práctico sigue este patrón:

```text
ejecutar -> inspeccionar -> modificar -> comparar -> explicar
```

## Ruta esencial de clase

```text
M05.P01 -> M05.P04 -> M05.P06
```

- **P01** — tokenización, truncation y presupuesto de contexto.
- **P04** — logits, greedy, temperature, top-p y `max_new_tokens`.
- **P06** — policy, provider abstraction, Bedrock Luna y contrato de aplicación.

## Ampliación

- **P02** — embeddings contextuales.
- **P03** — familias Transformer.
- **P05** — tareas NLP y evaluación.
- `/v1/chat` y providers locales de P06.

## Entorno

```text
SageMaker Space
ml.t3.large
CPU
```

Los modelos locales pequeños se utilizan para observar mecanismos. P06 puede utilizar Amazon Bedrock mediante el rol del SageMaker Space, sin guardar claves en el repositorio.

## Material

- `M05_P01_Enunciado.md` … `M05_P06_Enunciado.md`
- `notebooks/` — notebooks ejecutables
- `scripts/` — equivalentes `.py` ejecutables
- `assets/`
- `enterprise-genai-assistant/` — aplicación v0.5 completa
