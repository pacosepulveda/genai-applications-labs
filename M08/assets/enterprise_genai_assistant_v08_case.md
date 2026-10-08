# Enterprise GenAI Assistant v0.8 — Production Readiness Case

## Punto de partida

Este caso es autocontenido. No depende de que el alumno haya realizado ejercicios de M07.

Se parte de un piloto ya aprobado con alcance limitado:

```text
20 técnicos
1 departamento: Operations
5 procedimientos aprobados
8 semanas
modo read-only
```

Capacidades incluidas:

```text
RAG read-only con citas
consulta read-only de incidentes
cálculo determinista de duración
```

Capacidades fuera de alcance:

```text
write tools
cambios automáticos de producción
aprobación automática de accesos privilegiados
comunicaciones externas automáticas
```

## Evidencia previa

El piloto ha demostrado utilidad suficiente para plantear operación productiva, pero pasar a producción exige ahora demostrar que el sistema puede entregarse, observarse, recuperarse y gobernarse.

## Objetivo de M08

Convertir el piloto en un servicio operable sin ampliar su autonomía.

## Requisitos de readiness

Antes de producción deben existir:

```text
owners explícitos
release manifest inmutable
quality gates
staging representativo
rollback
observability
SLO + alerts
runbooks
kill switch
incident process
cost ownership
```

## Restricciones de arquitectura y operación

- El corpus pertenece a Operations/Security, no a AI Engineering.
- Las ACL se aplican antes de construir contexto.
- La plataforma puede compartir infraestructura RAG, pero no asume ownership del contenido ni del outcome.
- Las trazas no deben almacenar secretos ni prompts completos indiscriminadamente.
- Model access puede centralizarse, pero el gateway se convierte en servicio crítico.
- El fallback debe haber sido evaluado antes de necesitarlo.
- Una regresión de calidad puede ser un incidente aunque HTTP sea 200.
- El coste se optimiza como `cost/task`, no como tokens aislados.
- Promover a producción requiere que la combinación evaluada sea la misma combinación desplegada.

## Grupos implicados

```text
Product Squad
AI Platform
Security / Risk
Service Operations
Data / Knowledge owners
```

## Decisión final de M08

El equipo debe clasificar v0.8 como:

```text
READY
READY_WITH_CONDITIONS
NOT_READY
```

y justificar la decisión con evidencia operativa.
