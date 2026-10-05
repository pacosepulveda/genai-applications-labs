# Enterprise GenAI Assistant v1.0 — Architecture Evolution Case

## Estado heredado

M08 dejó un servicio operable con:

```text
RAG read-only con citas
consulta read-only de incidentes
release manifest
quality gates
observability
rollback / kill switch
cost ownership
```

## Objetivo de M09

No reconstruir el producto.

Decidir qué capabilities nuevas merecen modificar la arquitectura.

## Presiones

- parte del conocimiento llega en documentos con diagramas e imágenes;
- algunas tareas simples podrían ejecutarse localmente;
- el coste debe medirse por tarea completada;
- las acciones de alto impacto deben conservar accountability humana;
- modelos y proveedores seguirán cambiando;
- regulación, auditoría y evidencia pueden endurecerse.

## Principios

```text
least agency
minimum useful context
smallest adequate model
eval-first migration
portable assets
explicit lifecycle
```

## Resultado esperado

Una arquitectura adaptativa en la que cada request utiliza la capability
suficiente y cada cambio tecnológico compite contra la misma evidencia.
