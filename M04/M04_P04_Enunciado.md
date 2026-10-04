# M04.P04 — Diagnóstico y evaluación de una GAN

**Modalidad:** individual o parejas  
**Entregable:** informe de diagnóstico con evidencia cuantitativa y visual

## Objetivo

Una GAN puede producir algunas imágenes convincentes y seguir siendo un mal generador.

En esta práctica evaluarás:

```text
calidad
variación
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

Entrena una `LogisticRegression` sobre los dígitos reales y utilízala **solo como instrumento de evaluación** de las imágenes generadas.

Obtén la distribución de clases predichas sobre las muestras de la GAN.

Pregunta:

> ¿La GAN parece cubrir varias clases o se concentra en unas pocas?

La clase predicha por este clasificador **no es ground truth** de una imagen sintética. Es una señal de diagnóstico que debe combinarse con otras evidencias.

### Parte D — Mode collapse

Define una regla práctica para marcar una ejecución como sospechosa de mode collapse.

La regla puede combinar:

- baja diversidad;
- concentración en pocas clases predichas;
- inspección visual.

### Parte E — Comparación de checkpoints

Si conservaste muestras de diferentes épocas, compáralas.

No elijas el “mejor” modelo únicamente porque la última epoch sea la más reciente.

## Sobre FID

FID se estudia después en las slides, pero no lo calcularemos en esta práctica. Un FID estándar basado en Inception sobre imágenes 8×8, con pocas muestras y un dominio tan diferente, aportaría una cifra difícil de interpretar.

## Preguntas

1. ¿Puede una GAN tener imágenes individualmente buenas pero mala cobertura?
2. ¿Qué diferencia hay entre fidelidad y diversidad?
3. ¿Por qué una única métrica no es suficiente?
4. ¿Qué evaluarías si las imágenes se utilizaran como data augmentation?
