# M03.P01 — Dentro de una red: forward, loss y backpropagation

**Modalidad:** individual o parejas  
**Entregable:** notebook completado y explicación de una actualización de pesos

## Objetivo

Observarás directamente los pasos que normalmente ocultan los frameworks:

```text
entrada
-> forward
-> predicción
-> loss
-> backward
-> gradientes
-> actualización
```

## Tareas

Abre `notebooks/M03_P01_Forward_Backprop.ipynb`.

### Parte A — Una neurona sin framework de alto nivel

Implementa manualmente:

[
z = wx + b
]

y una función de pérdida cuadrática:

[
L=(hat y-y)^2
]

Calcula el gradiente respecto a `w` y `b` para un único ejemplo.

Realiza una actualización utilizando un learning rate pequeño.

### Parte B — Autograd

Repite el mismo cálculo con PyTorch y:

```python
loss.backward()
```

Compara:

- gradiente manual;
- gradiente producido por `autograd`.

### Parte C — Varias iteraciones

Entrena la neurona durante varias actualizaciones y registra:

- peso;
- bias;
- predicción;
- loss.

### Parte D — MLP

Construye una red:

```text
2 inputs
-> Linear(2, 8)
-> ReLU
-> Linear(8, 2)
```

Inspecciona:

- shapes;
- logits;
- número de parámetros.

## Preguntas

1. ¿Qué contiene `parameter.grad` después de `backward()`?
2. ¿Por qué se limpian los gradientes antes de la siguiente actualización?
3. ¿Qué ocurriría si todas las capas fuesen lineales y no hubiese activaciones?
4. ¿Cuál es la diferencia entre un logit y una probabilidad?
