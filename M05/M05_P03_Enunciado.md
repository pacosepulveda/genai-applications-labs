# M05.P03 — BERT, decoder causal y T5: tres familias Transformer

**Modalidad:** individual o parejas  
**Entregable:** notebook comparativo de arquitectura, máscaras y comportamiento

## Objetivo

Relacionarás tres familias Transformer con sus objetivos naturales:

```text
BERT -> encoder-only
SmolLM2 -> decoder-only causal
FLAN-T5 -> encoder-decoder
```

## Tareas

Abre:

```text
notebooks/M05_P03_Transformer_Families.ipynb
```

### Parte A — Configuración

Carga `AutoConfig` de los tres modelos.

Construye una tabla con:

- `model_type`;
- hidden size / model dimension;
- número de capas;
- attention heads;
- tamaño de vocabulario;
- encoder-decoder sí/no;
- context/position limit cuando esté disponible.

### Parte B — Encoder

Con BERT:

1. tokeniza una frase;
2. ejecuta el encoder;
3. inspecciona `last_hidden_state`;
4. explica por qué obtenemos una representación por token y no texto generado.

### Parte C — Decoder causal

Con SmolLM2:

1. aplica el chat template del tokenizer;
2. inspecciona el texto resultante;
3. tokeniza;
4. genera una continuación corta.

La calidad lingüística no es el objetivo del ejercicio.

### Parte D — Encoder-decoder

Con FLAN-T5:

1. formula una instrucción de resumen;
2. tokeniza el input;
3. ejecuta `generate`;
4. decodifica el resultado.

### Parte E — Elección de arquitectura

Para cada caso, selecciona una familia y justifica:

- clasificación de tickets;
- completado;
- traducción;
- resumen;
- extracción de entidades;
- chatbot generativo.

## Preguntas

1. ¿Por qué BERT no es un generador autoregresivo natural?
2. ¿Qué obliga al decoder causal a no mirar tokens futuros?
3. ¿Qué ventaja tiene encoder-decoder para transformaciones input→output?
4. ¿Por qué arquitectura y objetivo de pretraining están relacionados?
