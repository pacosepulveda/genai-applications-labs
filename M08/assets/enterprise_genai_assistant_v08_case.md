# Enterprise GenAI Assistant v0.8 — Operating Model Case

## Estado heredado

M07 recomendó un piloto limitado de:

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

## Objetivo de M08

Diseñar el equipo y el operating model necesarios para pasar de PoC a un piloto operable.

## Restricciones

- Hay que mantener separación entre product ownership, service ownership, data ownership y risk ownership.
- El contenido de procedimientos pertenece a Operations/Security, no al equipo de IA.
- El acceso a modelos y proveedores debe centralizar controles comunes.
- Un cambio de prompt, modelo, índice o tool puede provocar regresiones.
- El piloto debe disponer de rollback y kill switch.
- Security y Risk no deben revisar manualmente cada cambio de bajo riesgo.
- El equipo debe poder operar el servicio aunque una persona clave no esté disponible.

## Entregables esperados

- Team topology.
- Skill gap plan.
- RACI.
- Ownership map.
- Git/LLMOps workflow.
- Operations readiness checklist.
- On-call/escalation model.
- Service catalog entry.
- Training/change-management plan.
