# M04.P01 — Imágenes como tensores y augmentations

**Modalidad:** individual o parejas  
**Entregable:** observaciones y respuestas sobre el notebook

## Objetivo

Observar qué recibe realmente una red visual:

```text
imagen -> tensor -> canal -> batch -> rango numérico
```

## Trabajo

Abre `notebooks/M04_P01_Image_Tensors.ipynb`.

El código está completo. Ejecuta todas las celdas y:

1. identifica los shapes `8×8`, `1×8×8` y `32×1×8×8`;
2. compara los rangos `[0,1]` y `[-1,1]`;
3. observa ruido, desplazamiento e intensidad;
4. cambia `sigma` de `0.08` a `0.20`;
5. decide si la transformación sigue conservando razonablemente la clase.

## Preguntas

1. ¿Qué representa la dimensión de canal?
2. ¿Por qué el batch añade otra dimensión?
3. ¿Por qué una augmentation válida depende de la tarea?
4. ¿Qué problema tendría alimentar un modelo con un rango distinto del esperado?
