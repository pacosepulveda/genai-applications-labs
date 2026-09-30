# M04.P04 — Diagnóstico y evaluación de una GAN

**Modalidad:** individual o parejas  
**Entregable:** informe de diagnóstico con evidencia cuantitativa y visual

## Objetivo

Una GAN puede producir algunas imágenes convincentes y seguir siendo un mal generador.

En esta práctica evaluarás:

```text
calidad
diversidad
cobertura
estabilidad
```

## Tareas

Abre:

```text
notebooks/M04_P04_GAN_Evaluation.ipynb
```

y carga el generador de P03.

### Parte A — Muestreo

Genera al menos 500 muestras.

### Parte B — Diversidad simple

Calcula:

- desviación estándar media por píxel;
- distancia media entre pares de muestras de una submuestra;
- número de imágenes casi idénticas según un umbral razonado.

Estas métricas son didácticas; no son estándares universales.

### Parte C — Clasificador auxiliar

Entrena un pequeño clasificador sobre los dígitos reales.

Utilízalo **solo como instrumento de evaluación** de las imágenes generadas.

Obtén la distribución de clases predichas sobre las muestras de la GAN.

Pregunta:

> ¿La GAN cubre varias clases o se concentra en unas pocas?

### Parte D — Mode collapse

Define una regla práctica para marcar una ejecución como sospechosa de mode collapse.

La regla puede combinar:

- baja diversidad;
- concentración en pocas clases;
- inspección visual.

### Parte E — Comparación de checkpoints

Si conservaste muestras de diferentes épocas, compáralas.

No elijas el “mejor” modelo únicamente porque la última epoch sea la más reciente.

### Parte F — FID

Explica por qué **no calculamos FID estándar** sobre este pequeño dataset 8×8 con Inception:

- el extractor Inception está pensado para otro dominio;
- el tamaño de muestra es pequeño;
- la métrica resultaría poco informativa.

Describe qué necesitarías para utilizar FID correctamente en un proyecto real.

## Preguntas

1. ¿Puede una GAN tener imágenes individualmente buenas pero mala cobertura?
2. ¿Qué diferencia hay entre fidelidad y diversidad?
3. ¿Por qué una única métrica no es suficiente?
4. ¿Qué evaluarías si las imágenes se utilizaran como data augmentation?
