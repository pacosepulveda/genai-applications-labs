# Enterprise GenAI Assistant v1.0 — Architecture Evolution Case

## Estado inicial del caso

Enterprise GenAI Assistant es ya un servicio operable con:

```text
RAG read-only con citas
consulta read-only de incidentes
release manifest
quality gates
observability
rollback / kill switch
cost ownership
```

No es necesario haber realizado M08 para trabajar con este caso. Este es el baseline del que parte M09.

## Alcance actual

```text
usuarios internos
conocimiento corporativo autorizado
consultas read-only
rutas DIRECT / RAG / AGENT acotadas
operación con métricas y rollback
```

## Objetivo de M09

No reconstruir el producto.

Decidir qué capabilities nuevas merecen modificar la arquitectura y cuáles deben esperar.

## Presiones

- parte del conocimiento llega en documentos con diagramas e imágenes;
- algunas tareas simples podrían ejecutarse localmente;
- el coste debe medirse por tarea completada;
- las acciones de alto impacto deben conservar accountability humana;
- modelos y proveedores seguirán cambiando;
- regulación, auditoría y evidencia pueden endurecerse;
- nuevas capacidades no deben destruir la posibilidad de rollback o migración.

## Principios

```text
least agency
minimum useful context
smallest adequate model
eval-first migration
portable assets
explicit lifecycle
```

## Restricciones

- ninguna migración tecnológica se aprueba solo por benchmark externo;
- knowledge y authorization siguen siendo controles del producto, no del modelo;
- una tool de alto impacto requiere límites y accountability explícitos;
- los eval sets deben poder ejecutarse contra candidatos distintos;
- una abstracción solo se mantiene si reduce una dependencia estratégica real;
- todo componente adoptado debe tener trigger de revisión y exit plan cuando corresponda.

## Resultado esperado

Una arquitectura adaptativa en la que cada request utiliza la capability suficiente y cada cambio tecnológico compite contra la misma evidencia.
