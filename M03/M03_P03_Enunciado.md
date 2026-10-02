# M03.P03 — Provocar overfitting y corregirlo

**Modalidad:** individual o parejas  
**Entregable:** curvas de aprendizaje y comparación entre red base y red regularizada

## Objetivo

El overfitting se entiende mejor cuando se observa.

En esta práctica reducirás deliberadamente el conjunto de entrenamiento y aumentarás la capacidad de la red para provocar sobreajuste.

## Tareas

Abre `notebooks/M03_P03_Overfitting_Regularization.ipynb`.

1. Reutiliza el preprocesamiento del dataset de intenciones.
2. Utiliza un subconjunto pequeño de train.
3. Construye una red deliberadamente sobredimensionada **respecto al pequeño dataset**. Como referencia, utiliza capas ocultas de 512 y 256 unidades.
4. Entrena suficientes épocas para observar el fenómeno, con un máximo orientativo de 60 épocas:
   - train loss;
   - validation loss;
   - train accuracy/F1;
   - validation accuracy/F1.
5. Dibuja las curvas.
6. Identifica la época aproximada donde validation deja de mejorar.
7. Construye una segunda versión incorporando al menos:
   - Dropout;
   - weight decay;
   - early stopping.
8. Compara ambas.

## Parte adicional — gradientes

Registra la norma global aproximada de los gradientes durante algunas iteraciones.

Aplica `clip_grad_norm_` y explica:

- qué modifica;
- qué problema intenta limitar;
- por qué no es una solución universal al mal entrenamiento.

## Preguntas

1. ¿Cómo distingues overfitting de underfitting?
2. ¿Por qué la última época no tiene por qué ser el mejor modelo?
3. ¿Dropout se comporta igual en `train()` y `eval()`?
4. ¿Por qué early stopping necesita un validation set independiente?
