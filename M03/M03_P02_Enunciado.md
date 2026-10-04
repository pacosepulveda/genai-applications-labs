# M03.P02 — Entrenar una MLP y compararla con el baseline clásico

**Modalidad:** individual o parejas  
**Entregable:** benchmark reproducible, artefactos del router neuronal y conclusión técnica

## Objetivo

En M02 construiste un router de intenciones basado en TF-IDF + Logistic Regression.

Ahora construirás una **MLP** sobre una representación equivalente y responderás a una pregunta de ingeniería:

> ¿La red neuronal mejora realmente el sistema?

## Dataset

Utiliza:

```text
assets/intent_requests.csv
```

Mantén la misma exclusión de `final_route`: sigue siendo una fuga de información.

## Particiones

Trabajaremos con tres conjuntos distintos:

- **train**: ajusta preprocesamiento y parámetros;
- **validation**: permite seguir el entrenamiento sin consultar test;
- **test**: permanece reservado hasta la comparación final.

Mantén una división estratificada y reproducible con `random_state=42`. Una distribución válida para esta práctica es aproximadamente 64 % train, 16 % validation y 20 % test.

## Tareas

Abre `notebooks/M03_P02_MLP_vs_Classic.ipynb`.

1. Crea las particiones train, validation y test de forma estratificada con `random_state=42`.
2. Ajusta el preprocesador **solo con train**:
   - TF-IDF para texto;
   - one-hot encoding para variables categóricas.
3. Entrena como referencia una `LogisticRegression`.
4. Convierte las matrices de entrada a tensores.
5. Construye una MLP compacta:
   - TF-IDF limitado a aproximadamente 1.000 features;
   - input;
   - capa oculta de 128 unidades;
   - ReLU;
   - segunda capa oculta;
   - ReLU;
   - capa de salida.

En esta práctica **no utilizaremos todavía Dropout**. Primero queremos observar una red básica; la regularización se estudia y aplica explícitamente en P03.
6. Entrena utilizando:
   - `CrossEntropyLoss`;
   - AdamW;
   - mini-batches de 32 o 64;
   - un máximo orientativo de 25 épocas.
7. Registra por época:
   - train loss;
   - validation loss;
   - macro F1 de validation.
8. Evalúa ambos modelos sobre el mismo **test reservado**.
9. Compara:
   - macro F1;
   - accuracy;
   - número de parámetros;
   - latencia aproximada de inferencia.
10. Concluye si reemplazarías el modelo clásico.

## DataLoader

El notebook proporciona el esqueleto de `TensorDataset` y `DataLoader`. En esta práctica su función es agrupar ejemplos en mini-batches y entregarlos al training loop; no es necesario memorizar todavía toda la API.

## Artefactos

Guarda:

```text
enterprise-genai-assistant/artifacts/
├── neural_preprocessor.joblib
├── neural_label_encoder.joblib
├── neural_router.pt
└── neural_router_config.json
```

Guarda también el modelo clásico como:

```text
classic_router.joblib
```

para poder comparar ambos en P06.

## Regla

No se considera éxito que la red “gane”.

Se considera éxito que la comparación sea reproducible y la decisión esté sustentada por evidencia.
