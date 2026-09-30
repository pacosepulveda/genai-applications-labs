# M05.P01 — Tokenización, vocabulario y presupuesto de contexto

**Modalidad:** individual o parejas  
**Entregable:** notebook con comparación de tokenizers y análisis de contexto

## Objetivo

Comprobarás que un modelo de lenguaje no recibe palabras: recibe tokens e IDs.

Compararás tres estrategias:

```text
WordPiece
Byte-level BPE
SentencePiece
```

## Tareas

Abre:

```text
notebooks/M05_P01_Tokenization_Context.ipynb
```

### Parte A — Tres tokenizers

Carga:

- `google-bert/bert-base-multilingual-cased`;
- `HuggingFaceTB/SmolLM2-135M-Instruct`;
- `google/flan-t5-small`.

Tokeniza las mismas frases en español.

Para cada tokenizer muestra:

- tokens;
- IDs;
- número de tokens;
- special tokens añadidos.

### Parte B — Texto técnico

Tokeniza:

```text
CVE-2026-1234
customer_id
/api/v2/status
192.168.10.25
OpenTelemetry
Kubernetes
🔐
```

Analiza qué identificadores se fragmentan más.

### Parte C — Padding y attention mask

Crea un batch con frases de longitudes distintas.

Muestra:

```text
input_ids
attention_mask
```

Identifica qué posiciones corresponden a padding.

### Parte D — Truncation

Crea un texto mayor que el límite configurado del tokenizer.

Aplica truncation y comprueba qué información desaparece.

### Parte E — Token budget

Implementa:

```python
estimate_budget(...)
```

que reciba:

- system text;
- history;
- user input;
- output reserve.

Debe indicar si la petición cabe en una context window configurada.

## Preguntas

1. ¿Por qué token no equivale a palabra?
2. ¿Qué ventaja aporta subword tokenization?
3. ¿Por qué un identificador técnico puede consumir muchos tokens?
4. ¿Qué diferencia existe entre padding y truncation?
5. ¿Por qué la context window debe reservar espacio para la salida?
