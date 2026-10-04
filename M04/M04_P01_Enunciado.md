# M04.P01 — Imágenes como tensores y augmentations

**Modalidad:** individual o parejas  
**Entregable:** notebook completado con análisis de representación y transformaciones

## Objetivo

Antes de generar imágenes debes comprender qué recibe realmente una red neuronal.

Utilizarás `sklearn.datasets.load_digits`, que contiene imágenes de dígitos de 8×8 y está disponible localmente. La práctica está diseñada para ejecutarse íntegramente en CPU dentro del SageMaker Space.

## Tareas

Abre:

```text
notebooks/M04_P01_Image_Tensors.ipynb
```

### Parte A — Representación

1. Carga el dataset.
2. Inspecciona:
   - número de imágenes;
   - resolución;
   - rango de píxeles;
   - tipo de dato;
   - clases.
3. Convierte una imagen a tensor PyTorch.
4. Añade explícitamente:
   - dimensión de canal;
   - dimensión de batch.
5. Explica los shapes:

```text
8 × 8
1 × 8 × 8
32 × 1 × 8 × 8
```

### Parte B — Normalización

Transforma el rango original:

```text
0 .. 16
```

a:

```text
0 .. 1
```

y después a:

```text
-1 .. 1
```

Comprueba los valores mínimo y máximo.

### Parte C — Augmentation

Aplica transformaciones pequeñas que puedan preservar razonablemente la clase:

- traslación;
- ruido;
- cambio pequeño de escala o intensidad.

Visualiza varias versiones.

Después crea deliberadamente una transformación problemática y explica por qué podría cambiar el significado.

### Parte D — Dataset para generación

El notebook ya importa `TensorDataset` y `DataLoader`. Utilízalos para entregar batches con shape:

```text
batch × 1 × 8 × 8
```

No es necesario explorar opciones avanzadas de `DataLoader`: aquí solo necesitamos agrupar tensores en mini-batches.

## Preguntas

1. ¿Por qué una CNN espera una dimensión de canal aunque la imagen sea en escala de grises?
2. ¿Por qué es importante que datos reales y salida del generador utilicen rangos compatibles?
3. ¿Por qué data augmentation no consiste simplemente en aplicar transformaciones aleatorias?
