# Módulo 8 — Delivery y Operación de Aplicaciones de IA

## Objetivo

M08 cambia el foco desde la construcción técnica hacia la capacidad de entregar, cambiar y operar una aplicación GenAI de forma controlada.

```text
M01–M06:
construir capacidades técnicas

M07:
decidir qué merece la pena llevar a piloto

M08:
definir quién responde, cómo se promueven cambios
y cómo se opera el servicio cuando algo falla
```

## Documentación

La [documentación técnica completa del módulo](documentacion/README.md) está disponible en la carpeta `documentacion/`.

## Enfoque práctico

M08 no fuerza el uso de notebooks. Las prácticas son **tabletops y workshops de decisión** apoyados en evidence packs ficticios incluidos en `assets/`.

El patrón es:

```text
situación
→ evidencia
→ decisión
→ inyecto
→ revisión de la decisión
→ artefacto operativo
→ debrief
```

Las prácticas no dependen de que el alumno haya ejecutado laboratorios de M07. El estado inicial necesario está incluido dentro de M08.

## Ruta práctica

```text
M08.P01  Operating Model & Decision Rights
M08.P02  Release Gate & Platform Decisions
M08.P03  Production Day & Readiness Review
```

### M08.P01 — Operating Model & Decision Rights

Convierte capabilities en owners, decision rights e interfaces operativas.

**Momento recomendado:** después de la slide 7 del deck reducido.

### M08.P02 — Release Gate & Platform Decisions

Decide qué artefactos se promueven, qué gates son obligatorios, qué capacidades deben ser compartidas y cómo limitar el blast radius.

**Momento recomendado:** después de la slide 22.

### M08.P03 — Production Day & Readiness Review

Responde a degradaciones de disponibilidad, calidad, seguridad y coste, y termina con una decisión `READY / READY_WITH_CONDITIONS / NOT_READY`.

**Momento recomendado:** después de la slide 27.

## Material

- `M08_P01_Enunciado.md`
- `M08_P02_Enunciado.md`
- `M08_P03_Enunciado.md`
- `assets/` — evidence packs e inyectos
- `templates/` — plantillas editables
- `work/` — espacio local recomendado para las respuestas del alumno

## Forma de trabajo

Duplica la plantilla de cada práctica dentro de `work/` y completa allí las decisiones.

`work/` está ignorado por Git para que el trabajo del alumno no provoque conflictos al actualizar el repositorio.

## Regla de diseño

No hay una única respuesta correcta para todas las decisiones. Se evalúa la calidad de la postura:

- qué evidencia se utilizó;
- qué riesgo se acepta;
- quién tiene autoridad para decidir;
- qué condiciones producirían un rollback, degradación o parada;
- qué información haría cambiar la decisión.
