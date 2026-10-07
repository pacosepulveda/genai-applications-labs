# M03.P02 — MLP frente al baseline clásico

**Modalidad:** individual o parejas  
**Entregable:** benchmark ejecutado y decisión técnica

## Objetivo

Comparar el router clásico con una MLP sin dedicar tiempo a escribir boilerplate de PyTorch.

El notebook incluye completos el split `train / validation / test`, el preprocesamiento, el baseline clásico, la MLP, el entrenamiento, la evaluación y la exportación de los archivos usados posteriormente por P06.

## Ruta esencial

Abre `notebooks/M03_P02_MLP_vs_Classic.ipynb`.

### Parte A — Ejecuta el benchmark

Ejecuta el notebook completo y registra macro F1, accuracy, latencia y número de parámetros de la MLP.

### Parte B — Modifica una decisión de arquitectura

Cambia `hidden_dim = 128` por `hidden_dim = 32`, vuelve a ejecutar y compara.

### Parte C — Decide

Elige una opción:

```text
KEEP_CLASSIC
USE_NEURAL
CONTINUE_EXPERIMENT
```

Justifica la decisión considerando calidad, latencia, complejidad y operación.

## Regla

No se considera éxito que la MLP “gane”. El objetivo es decidir si su ventaja compensa el coste adicional.

## Archivos para P06

El notebook exporta automáticamente los archivos necesarios para probar P06.
