# M05.P01 — Tokenización y presupuesto de contexto

**Modalidad:** individual o parejas  
**Entregable:** notebook con observación de tokens, truncation y presupuesto de contexto

## Objetivo

Comprobarás dos ideas fundamentales para trabajar con LLMs:

```text
texto -> tokens -> IDs
```

y:

```text
input_tokens + output_reserve <= context_window
```

La práctica utiliza un único tokenizer generativo para centrarnos en el mecanismo y evitar trabajo repetitivo.

## Tareas

Abre `notebooks/M05_P01_Tokenization_Context.ipynb`.

### Parte A — Texto, tokens e IDs

Carga el tokenizer `HuggingFaceTB/SmolLM2-135M-Instruct`.

Tokeniza una frase corta en español y muestra tokens, IDs y número total de tokens. Comprueba que **token no equivale necesariamente a palabra**.

### Parte B — Identificadores técnicos

Tokeniza:

```text
CVE-2026-1234
customer_id
/api/v2/status
192.168.10.25
OpenTelemetry
Kubernetes
```

Muestra cuántos tokens consume cada elemento e identifica cuáles se fragmentan más.

### Parte C — Truncation

Construye un texto largo que termine con `INFORMACION_CRITICA_FINAL`.

Tokenízalo con `max_length=64` y `truncation=True`. Decodifica la entrada resultante y comprueba si la información crítica ha sobrevivido.

### Parte D — Token budget

Implementa:

```python
estimate_budget(...)
```

La función debe recibir system text, history, user input, output reserve y context limit. Debe devolver al menos `input_tokens`, `total_reserved`, `fits` y `remaining`.

Prueba un escenario que quepa y otro que no.

## Ampliación

Si quieres profundizar, compara el mismo texto con WordPiece y SentencePiece y explora padding + `attention_mask`.

## Preguntas

1. ¿Por qué token no equivale a palabra?
2. ¿Por qué un identificador técnico puede consumir varios tokens?
3. ¿Qué riesgo tiene truncar sin estrategia?
4. ¿Por qué debemos reservar espacio para la salida?
5. ¿Qué tendría que hacer una aplicación cuando la petición no cabe?
