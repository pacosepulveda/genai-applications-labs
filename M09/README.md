# Módulo 9 — El Futuro de la IA Generativa en la Empresa

## Objetivo

M09 cierra el curso con una idea: no necesitamos predecir qué tecnología dominará, sino mantener nuestras aplicaciones preparadas para **evaluar, decidir y adaptarse con evidencia**.

```text
M01–M06:
construir capacidades técnicas

M07:
decidir qué merece la pena llevar a piloto

M08:
entregar y operar el servicio

M09:
adaptarlo cuando cambian capabilities, modelos,
hardware, regulación, coste y patrones de uso
```

## Documentación

La [documentación técnica completa del módulo](documentacion/README.md) está disponible en la carpeta `documentacion/`.

## Enfoque práctico

M09 no fuerza el uso de notebooks. Las prácticas son **tabletops y workshops de decisión** apoyados en evidence packs ficticios incluidos en `assets/`.

El patrón es:

```text
señal
→ evidencia
→ decisión inicial
→ inyecto
→ reevaluación
→ decisión de arquitectura/lifecycle
→ debrief
```

Las prácticas son autocontenidas. No es necesario haber ejecutado laboratorios de M07 o M08 para empezar M09.

## Ruta práctica

```text
M09.P01  Technology Radar & Adoption Board
M09.P02  Adaptive Architecture & Human Control
M09.P03  Future Scenario Stress Test & Lifecycle Board
```

### M09.P01 — Technology Radar & Adoption Board

Clasifica tecnologías como `NOW / NEXT / WATCH` y toma decisiones `ADOPT / TRIAL / WATCH / REJECT` utilizando capability, evidencia, riesgo, complejidad y switching cost.

**Momento recomendado:** después de la slide 5 del deck reducido.

### M09.P02 — Adaptive Architecture & Human Control

Diseña rutas por request utilizando la capability mínima suficiente, aplica `least agency`, `minimum useful context` y decide dónde es obligatorio mantener intervención humana.

**Momento recomendado:** después de la slide 23.

### M09.P03 — Future Scenario Stress Test & Lifecycle Board

Somete la arquitectura a cuatro futuros posibles, compara candidatos con la misma evidencia y decide qué mantener, probar, rechazar o retirar.

**Momento recomendado:** después de la slide 30.

## Material

- `M09_P01_Enunciado.md`
- `M09_P02_Enunciado.md`
- `M09_P03_Enunciado.md`
- `assets/` — evidence packs y escenarios
- `templates/` — plantillas editables
- `work/` — espacio local recomendado para las respuestas del alumno

## Forma de trabajo

Duplica la plantilla de cada práctica dentro de `work/` y completa allí las decisiones.

`work/` está ignorado por Git para que el trabajo del alumno no provoque conflictos al actualizar el repositorio.

## Regla de diseño

No hay una única respuesta correcta para todas las decisiones. Se evalúa la calidad de la postura:

- qué capability resuelve realmente el problema;
- qué evidencia justifica adoptar o esperar;
- qué riesgo y coste introduce la decisión;
- qué parte debe permanecer reversible;
- qué condición cambiaría la decisión;
- qué activos portables reducen el switching cost futuro.
