# M02.P03 — Métricas, confianza y abstención

**Modalidad:** individual o parejas  
**Entregable:** política de confianza justificada y evaluación sobre test

## Objetivo

Un sistema empresarial no debería convertir necesariamente cada predicción en una acción.

En esta práctica utilizarás las probabilidades del clasificador para introducir una tercera posibilidad:

```text
predecir
o
abstenerse y pedir revisión
```

## Concepto operativo

En esta práctica llamaremos **coverage** al porcentaje de solicitudes que el sistema resuelve automáticamente en lugar de enviarlas a `REVIEW`. Al aumentar el threshold suele reducirse la cobertura, porque exigimos más confianza para automatizar.

## Tareas

Abre `notebooks/M02_P03_Thresholds_Abstention.ipynb`.

1. Entrena o carga el pipeline de P02.
2. Obtén `predict_proba` sobre test.
3. Para cada solicitud calcula:
   - clase predicha;
   - probabilidad máxima;
   - si la predicción es correcta.
4. Evalúa varios thresholds de confianza.
5. Para cada threshold calcula:
   - `coverage`: porcentaje de solicitudes resueltas automáticamente;
   - accuracy sobre las solicitudes aceptadas;
   - porcentaje enviado a `REVIEW`.
6. Elige un threshold y justifícalo.
7. Analiza específicamente los errores relacionados con `CORPORATE_KNOWLEDGE`.
8. Diseña una regla adicional para que las solicitudes que requieren fuentes corporativas no puedan ser enrutadas a generación libre aunque el clasificador tenga alta confianza.

## Resultado esperado

La salida conceptual debe ser similar a:

```text
prediction = CORPORATE_KNOWLEDGE
confidence = 0.87
route = CONTROLLED_KNOWLEDGE_FLOW
```

o:

```text
prediction = QUESTION
confidence = 0.54
route = REVIEW
```

## Reflexión

Explica por qué aumentar el threshold puede mejorar la precisión de los casos aceptados, pero reducir la cobertura del sistema.
