# Módulo 5 — NLP Generativo

## Objetivos

En estas prácticas estudiarás el pipeline completo que transforma texto en una salida generada:

```text
texto
  ↓
tokenización
  ↓
token IDs + masks
  ↓
embeddings contextuales
  ↓
BERT / decoder causal / T5
  ↓
logits
  ↓
decoding
  ↓
texto
```

La secuencia es:

```text
M05.P01 -> M05.P02 -> M05.P03 -> M05.P04 -> M05.P05 -> M05.P06
```

## Entorno

Todos los laboratorios están diseñados para ejecutarse en el SageMaker Space facilitado por el instructor:

```text
ml.t3.large
CPU
sin GPU
```

No se requiere instalar software en el ordenador del alumno ni disponer de una cuenta personal en servicios de IA.

Los modelos locales son deliberadamente pequeños. Para evitar descargas simultáneas durante la clase, se recomienda precargar sus checkpoints/tokenizers en la caché del entorno antes de la sesión.

## Modelos utilizados

| Uso | Modelo |
|---|---|
| Tokenización multilingual / WordPiece | `google-bert/bert-base-multilingual-cased` |
| Embeddings BERT pequeños | `google/bert_uncased_L-2_H-128_A-2` |
| Decoder causal / chat template | `HuggingFaceTB/SmolLM2-135M-Instruct` |
| Encoder-decoder text-to-text | `google/flan-t5-small` |
| Provider gestionado real | `us.openai.gpt-5.6-luna` en Amazon Bedrock |

Los modelos locales pequeños se utilizan para comprender mecanismos. La calidad de sus respuestas no representa la calidad de modelos empresariales de mayor tamaño.

P06 añade Luna como provider gestionado real usando las credenciales del SageMaker Execution Role. No se almacenan API keys en el repositorio.

## Material

- `M05_P01_Enunciado.md`
- `M05_P02_Enunciado.md`
- `M05_P03_Enunciado.md`
- `M05_P04_Enunciado.md`
- `M05_P05_Enunciado.md`
- `M05_P06_Enunciado.md`
- `notebooks/`
- `assets/`
- `enterprise-genai-assistant/`
