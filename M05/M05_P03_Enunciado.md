# M05.P03 — Familias Transformer

**Ampliación**

## Objetivo

Compararás encoder-only, decoder-only y encoder-decoder a través de sus contratos y tareas.

Abre:

```text
notebooks/M05_P03_Transformer_Families.ipynb
```

## Trabajo

1. Ejecuta la tabla de configuración de los tres modelos.
2. Observa el `last_hidden_state` del encoder-only.
3. Inspecciona el `chat_template` del decoder causal y su respuesta.
4. Ejecuta la tarea text-to-text con T5.
5. Cambia el mensaje del chat model y la instrucción de T5.
6. Revisa la tabla final y justifica qué familia elegirías para clasificación, chatbot y traducción.

## Preguntas

1. ¿Por qué no existe una jerarquía simple BERT < T5 < GPT?
2. ¿Qué aporta un chat template?
3. ¿Qué tareas encajan naturalmente con encoder-only?
