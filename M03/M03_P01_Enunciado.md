# M03.P01 — Dentro de una red: forward, loss y backpropagation

**Modalidad:** individual o parejas  
**Entregable:** notebook completado y explicación de una actualización de pesos

## Objetivo

Observar directamente el ciclo mínimo de aprendizaje de una red:

```text
entrada
-> forward
-> predicción
-> loss
-> backward
-> gradientes
-> actualización
```

La práctica se centra en comparar un cálculo manual con el que realiza `autograd`.

## Ruta esencial

Abre `notebooks/M03_P01_Forward_Backprop.ipynb`.

### Parte A — Una neurona sin framework de alto nivel

Implementa manualmente:

```text
z = w*x + b
L = (y_hat - y)^2
```

Calcula:

- predicción;
- loss;
- gradiente respecto a `w`;
- gradiente respecto a `b`;
- una actualización con el learning rate indicado.

### Parte B — El mismo cálculo con autograd

Repite el ejemplo con PyTorch:

```python
loss.backward()
```

Compara los gradientes manuales con:

```python
w_t.grad
b_t.grad
```

Deben coincidir salvo pequeñas diferencias de representación numérica.

## Preguntas

1. ¿Qué contiene `parameter.grad` después de `backward()`?
2. ¿Qué parte del proceso automatiza `autograd`?
3. ¿Qué elementos sigue definiendo el desarrollador: datos, arquitectura, loss u objetivo?

## Ampliación

El notebook conserva una sección opcional para repetir varias actualizaciones y observar cómo cambian peso, bias, predicción y loss. Si modificas parámetros manualmente, utiliza `torch.no_grad()` y limpia los gradientes antes de la siguiente iteración.
