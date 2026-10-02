# M03.P04 — CNN: de píxeles a feature maps

**Modalidad:** individual o parejas  
**Entregable:** CNN entrenada, visualización de feature maps y comparación con una MLP

## Objetivo

Comprender experimentalmente qué cambia cuando una red explota estructura espacial.

Utilizarás `sklearn.datasets.load_digits`, un dataset de imágenes de dígitos de 8×8 incluido en scikit-learn.

## Tareas

Abre `notebooks/M03_P04_CNN_Feature_Maps.ipynb`.

1. Carga `load_digits`.
2. Visualiza varias imágenes y sus etiquetas.
3. Comprueba el shape original.
4. Divide train/test de forma estratificada.
5. Construye una MLP sencilla sobre los 64 píxeles.
6. Construye una CNN pequeña con:
   - una o dos capas `Conv2d`;
   - ReLU;
   - pooling;
   - capa final.
7. Entrena ambas con el mismo criterio de evaluación y un máximo orientativo de 15 épocas.
8. Compara:
   - precisión;
   - número de parámetros;
   - tiempo aproximado.
9. Selecciona una imagen.
10. Captura la salida de la primera convolución.
11. Visualiza varios **feature maps**.

## Preguntas

1. ¿Qué dimensión espera `Conv2d`?
2. ¿Qué significa cada canal de salida de la convolución?
3. ¿Por qué un kernel puede reutilizarse en diferentes posiciones?
4. ¿Por qué una CNN no necesita una conexión independiente entre cada píxel y cada detector local?
5. ¿Una CNN pequeña debe superar necesariamente a la MLP en este dataset?
