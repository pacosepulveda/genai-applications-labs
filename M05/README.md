# Módulo 5 — NLP Generativo

## Objetivos

En este módulo seguimos el recorrido esencial de una aplicación de lenguaje generativo:

```text
texto
  ↓
tokens + contexto
  ↓
embeddings / Transformer
  ↓
decoder causal
  ↓
logits + decoding
  ↓
texto generado
  ↓
validación + políticas + metadatos
```

El objetivo principal es comprender **cómo pasa un texto a convertirse en una salida generada y cómo encapsular esa capacidad dentro de una aplicación**.

## Entorno

Todos los laboratorios están diseñados para ejecutarse desde el SageMaker Space facilitado por el instructor.

```text
ml.t3.large
CPU
sin GPU
```

No es necesario instalar herramientas en el ordenador del alumno.

## Ruta principal

La práctica principal del módulo es:

```text
M05.P06 — Enterprise GenAI Assistant v0.5
```

En ella se implementa un servicio textual con:

```text
POST /v1/text
      ↓
text policy
      ↓
TextModelProvider
      ├── mock
      └── bedrock_luna
      ↓
TextResponse validada
```

La práctica conecta directamente con los conceptos vistos en las slides: tarea, contexto, provider abstraction, límite de salida, tokens, latencia y validación.

## Prácticas de ampliación

Las siguientes prácticas permanecen disponibles para profundizar en los mecanismos internos:

- `M05.P01` — tokenización, vocabulario y presupuesto de contexto;
- `M05.P02` — embeddings estáticos/contextuales;
- `M05.P03` — familias Transformer;
- `M05.P04` — logits, decoding y sampling;
- `M05.P05` — resumen, traducción y evaluación.

Los modelos locales pequeños utilizados en esas prácticas tienen finalidad didáctica. Su calidad no representa la de modelos empresariales de mayor tamaño.

## Provider gestionado

La ruta principal utiliza, cuando se selecciona el provider real:

```text
Amazon Bedrock Runtime
región: us-east-1
modelo: us.openai.gpt-5.6-luna
```

El código utiliza las credenciales temporales o el rol disponibles en el entorno AWS. No almacenes API keys, bearer tokens ni secretos en el repositorio.

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
