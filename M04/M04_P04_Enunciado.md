# M04.P04 — Diagnosticar una GAN

**Modalidad:** individual o parejas  
**Entregable:** diagnóstico razonado de diversidad y cobertura

## Requisito

Ejecuta antes `M04.P03`; genera `generator.pt` y `gan_config.json` automáticamente.

## Objetivo

Comprobar que “la GAN genera imágenes” no implica que tenga buena diversidad o cobertura.

## Trabajo

Abre `notebooks/M04_P04_GAN_Evaluation.ipynb`.

El notebook ya calcula variación media por píxel, distancia entre muestras, pares casi duplicados, distribución aproximada de clases mediante una sonda y una regla heurística de `suspected_collapse`.

Ejecuta el diagnóstico y después cambia un único umbral de la regla. Observa si la conclusión cambia.

## Preguntas

1. ¿Por qué una sonda de clases no es ground truth para imágenes sintéticas?
2. ¿Por qué debemos combinar varias señales?
3. ¿Qué diferencia existe entre calidad visual y diversidad?
4. ¿Por qué los umbrales del laboratorio son heurísticos?
