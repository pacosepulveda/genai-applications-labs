# Módulo 3 — Redes Neuronales y Deep Learning

## Objetivo

El módulo mantiene la progresión:

```text
forward + loss + autograd
        ↓
MLP y comparación con ML clásico
        ↓
overfitting y regularización
        ↓
CNN
        ↓
self-attention y Transformer
        ↓
Enterprise GenAI Assistant v0.3
```

## Formato de los laboratorios

Los notebooks y scripts contienen **código completo y ejecutable**.

La actividad de clase cambia de:

```text
escribir código -> depurar sintaxis -> ejecutar
```

a:

```text
ejecutar -> inspeccionar -> modificar un parámetro -> comparar -> explicar
```

El objetivo es dedicar el tiempo a comprender el comportamiento del modelo y la arquitectura, no a copiar boilerplate.

## Ruta esencial de clase

```text
M03.P01 — Forward, loss y autograd
        ↓
M03.P02 — MLP vs baseline clásico
        ↓
M03.P05 — Self-attention y causal mask
```

## Ampliación

- `M03.P03` — overfitting, regularización y gradient clipping.
- `M03.P04` — CNN y feature maps.
- `M03.P06` — router clásico/neural e integración v0.3.

P02 genera automáticamente los artefactos que puede reutilizar P06.

## Entorno

Todo se ejecuta en el entorno web del curso, en CPU.

## Material

- enunciados `M03_P01_Enunciado.md` … `M03_P06_Enunciado.md`;
- `notebooks/` — código completo organizado para clase;
- `scripts/` — equivalentes `.py` ejecutables;
- `assets/`;
- `enterprise-genai-assistant/` — implementación completa de P06.
