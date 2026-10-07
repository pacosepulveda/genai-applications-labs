# M03.P01 — Dentro de una red: forward, loss y backpropagation

**Modalidad:** individual o parejas  
**Entregable:** resultados ejecutados y explicación de una actualización

## Objetivo

Observar directamente:

```text
entrada -> forward -> predicción -> loss -> backward -> gradientes -> actualización
```

El notebook ya contiene el código completo para evitar perder tiempo en errores de sintaxis.

## Ruta esencial

Abre:

```text
notebooks/M03_P01_Forward_Backprop.ipynb
```

### Parte A — Ejecuta y verifica

Ejecuta el cálculo manual y la versión con `autograd`.

Comprueba que:

```text
dL/dw manual == w_t.grad
dL/db manual == b_t.grad
```

### Parte B — Predice antes de modificar

Antes de ejecutar de nuevo, elige **un solo cambio**:

```text
x
y
lr
```

Escribe qué esperas que ocurra con:

- gradiente;
- actualización;
- loss.

Después modifica únicamente ese valor y comprueba tu predicción.

### Parte C — Interpreta

Explica:

1. qué contiene `.grad`;
2. qué automatiza `autograd`;
3. qué sigue decidiendo el desarrollador.

## Ampliación

Ejecuta la sección de varias iteraciones y observa cómo cambian peso, bias, predicción y loss.
