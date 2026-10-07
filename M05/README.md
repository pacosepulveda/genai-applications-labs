# Módulo 5 — NLP Generativo

## Objetivos

El módulo conecta el funcionamiento básico de un modelo de lenguaje con su uso dentro de una aplicación:

```text
texto -> tokens + contexto -> Transformer -> logits -> decoding -> texto -> aplicación
```

## Ruta esencial de clase

```text
M05.P01 -> M05.P04 -> M05.P06
```

- **M05.P01** — tokens, identificadores técnicos, truncation y presupuesto de contexto.
- **M05.P04** — logits, greedy, temperature, top-p y `max_new_tokens`.
- **M05.P06** — policy, provider abstraction, Bedrock Luna y respuesta estructurada.

## Ampliación

- `M05.P02` — embeddings contextuales.
- `M05.P03` — encoder-only, decoder-only y encoder-decoder.
- `M05.P05` — tareas NLP y evaluación más extensa.
- ampliaciones de P06 — conversación y providers locales.

## Entorno

```text
SageMaker Space
ml.t3.large
CPU
sin GPU
```

Los modelos locales pequeños se utilizan para comprender mecanismos. P06 utiliza también un provider gestionado real mediante Amazon Bedrock y el SageMaker Execution Role, sin almacenar API keys en el repositorio.

## Material

- `M05_P01_Enunciado.md` — esencial
- `M05_P02_Enunciado.md` — ampliación
- `M05_P03_Enunciado.md` — ampliación
- `M05_P04_Enunciado.md` — esencial
- `M05_P05_Enunciado.md` — ampliación
- `M05_P06_Enunciado.md` — esencial
- `notebooks/`
- `assets/`
- `enterprise-genai-assistant/`
