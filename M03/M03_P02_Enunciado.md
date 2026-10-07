# M03.P02 — Entrenar una MLP y compararla con el baseline clásico

**Modalidad:** individual o parejas  
**Entregable:** benchmark reproducible y conclusión técnica

## Objetivo

En M02 construiste un router basado en TF-IDF + Logistic Regression.

Ahora entrenarás una **MLP compacta sobre una representación equivalente** y responderás a una pregunta de ingeniería:

> ¿La red neuronal mejora suficientemente el sistema como para justificar su complejidad?

## Dataset

Utiliza:

```text
assets/intent_requests.csv
```

`final_route` no se utiliza como feature porque introduciría fuga de información.

## Ruta esencial

Abre `notebooks/M03_P02_MLP_vs_Classic.ipynb`.

El notebook deja preparado el split reproducible y gran parte del preprocesamiento para concentrarnos en el ciclo de entrenamiento.

1. Comprueba las particiones `train`, `validation` y `test`.
2. Ejecuta el baseline `TF-IDF + OneHotEncoder + LogisticRegression`.
3. Prepara la representación para la red utilizando el preprocesador proporcionado.
4. Instancia `NeuralIntentMLP` con una capa oculta principal de 128 unidades.
5. Configura:
   - `CrossEntropyLoss`;
   - `AdamW`;
   - mini-batches;
   - 8 épocas como recorrido base.
6. Completa el ciclo:
   - `zero_grad`;
   - forward;
   - loss;
   - `backward`;
   - `step`.
7. Evalúa una sola vez sobre `test`.
8. Compara al menos:
   - macro F1;
   - accuracy.
9. Decide entre:
   - mantener el modelo clásico;
   - usar el neuronal;
   - continuar experimentando.

## Regla

No se considera éxito que la red “gane”.

Se considera éxito que puedas explicar por qué una diferencia de calidad sí o no compensa mayor complejidad, latencia y operación.

## Ampliación

El notebook incluye una sección opcional para exportar los artefactos que utiliza `M03.P06`. No es necesaria para completar la ruta esencial.
