# M03.P04 — CNN: de píxeles a feature maps · ampliación

**Modalidad:** individual o parejas  
**Entregable:** comparación MLP/CNN y observación de feature maps

## Objetivo

Observar qué cambia cuando una red explota estructura espacial.

El notebook ya contiene MLP, CNN, entrenamiento y visualización.

## Tareas

Abre `notebooks/M03_P04_CNN_Feature_Maps.ipynb`.

1. Ejecuta la comparación.
2. Registra accuracy y número de parámetros.
3. Observa los ocho feature maps de la primera convolución.
4. Selecciona otra imagen de test y vuelve a visualizar los mapas.
5. Explica qué ha cambiado y qué permanece igual.

## Preguntas

1. ¿Qué shape espera `Conv2d`?
2. ¿Por qué un kernel puede reutilizarse en distintas posiciones?
3. ¿Qué representa un feature map?
4. ¿Debe una CNN pequeña superar necesariamente a la MLP en este dataset?
