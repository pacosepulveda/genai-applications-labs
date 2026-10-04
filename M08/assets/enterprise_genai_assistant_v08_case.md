# Enterprise GenAI Assistant v0.8 — Production Readiness Case

## Estado heredado de M07

M07 recomendó un piloto limitado:

```text
RAG read-only con citas
consulta read-only de incidentes
```

y dejó fuera:

```text
write tools
cambios automáticos de producción
aprobación automática de accesos
```

## Alcance candidato

```text
20 técnicos
Operations
5 procedimientos aprobados
8 semanas
read-only
```

## Objetivo de M08

Convertir ese piloto en un servicio operable, no ampliar su autonomía.

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

## Restricciones

- El corpus pertenece a Operations/Security, no a AI Engineering.
- Las ACL se aplican antes de construir contexto.
- Las trazas no almacenan secretos ni prompts completos indiscriminadamente.
- Model access puede centralizarse, pero el gateway se convierte en servicio crítico.
- El fallback debe haber sido evaluado antes de necesitarlo.
- Una regresión de calidad puede ser un incidente aunque HTTP sea 200.
- El coste se optimiza como `cost/task`, no como tokens aislados.

## Decisión final

El equipo debe clasificar v0.8 como:

```text
READY
READY_WITH_CONDITIONS
NOT_READY
```

y justificar la decisión con evidencia.
