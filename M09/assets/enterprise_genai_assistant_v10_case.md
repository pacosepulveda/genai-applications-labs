# Enterprise GenAI Assistant v1.0 — Capstone Case

## Estado heredado

La solución ha evolucionado durante M01–M08 hasta disponer de:

```text
API controlada
ML / neural routing
NLP / embeddings
RAG con citas
tools read-only
agentes limitados
evaluation
risk / governance
operating model
```

## Peticiones de evolución

La organización quiere estudiar:

1. entrada multimodal para screenshots y documentos;
2. routing entre modelos rápidos, reasoning y edge;
3. soporte offline para algunas tareas;
4. agentes duraderos para investigaciones;
5. personalización por rol;
6. mayor trazabilidad regulatoria;
7. reducción de coste y consumo;
8. posible write access futuro.

## Restricciones

- Conocimiento corporativo autorizado sigue requiriendo fuentes.
- Permisos no los decide el LLM.
- No se permite write access en producción sin un gate separado.
- Cualquier cambio de modelo debe pasar la misma suite de evaluación.
- Personalización no puede romper tenant/user boundaries.
- El sistema debe poder degradarse si el proveedor cloud no está disponible.
- Debe existir un plan para retirar modelos y tecnologías.

## Objetivo

Diseñar una versión 1.0 que clasifique cada capability como:

```text
KEEP
ADOPT
TRIAL
WATCH
REJECT
RETIRE
```

y justifique la evolución mediante evidencia, no por novedad.
