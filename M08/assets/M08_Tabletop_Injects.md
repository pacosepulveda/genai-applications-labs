# M08 — Tabletop Injects

> Material para revelar secuencialmente durante las prácticas. Todos los datos son ficticios.

# P02 — Release Gate & Platform Decisions

## Inject P02.1 — La release parece buena, pero no toda la evidencia es equivalente

La release candidata contiene:

```text
CH02  system prompt RAG
CH04  reindexación del mismo corpus
CH06  tool read-only get_incident()
```

Resultados en staging:

```text
unit/schema tests: PASS
policy tests: PASS
prompt eval: mejora 93% -> 96%
retrieval eval: 37/40 casos correctos
security eval: PASS
p95 latency: +12%
cost/task: +8%
```

Tres fallos del retrieval afectan a preguntas poco frecuentes pero dos de ellos recuperan una versión documental incorrecta.

### Decisión

Elige:

```text
PROMOTE
PROMOTE_WITH_CONDITIONS
HOLD
REJECT
```

Debes indicar si separarías alguno de los cambios de la release y qué evidencia falta.

---

## Inject P02.2 — Cambio de última hora

El sponsor pide incorporar también:

```text
CH07 — tool que modifica configuración productiva
```

Argumento del sponsor:

> La tool ya funciona en DEV. Si esperamos a otra release perderemos dos semanas.

No existen todavía:

```text
agent security eval específica
approval workflow
write-scope authorization tests
kill switch validado
rollback rehearsal
```

### Decisión

Decide si:

```text
se incorpora a la misma release
se separa a una release posterior
se mantiene fuera de alcance
```

y especifica qué decision right tiene autoridad para bloquearla.

---

# P03 — Production Day & Readiness Review

## Inject P03.1 — 12:00 · Servicio degradado

El dashboard muestra:

```text
availability             0.940
p95_latency_s             2.3
citation_validity         0.910
retrieval_hit_rate        0.83
unauthorized_retrieval    0
avg_model_calls/task      1.5
cost/task_eur             0.11
```

Además aparecen errores del proveedor principal del modelo.

### Decisión

Debes distinguir si tienes un único incidente o varias degradaciones simultáneas.

Decide:

```text
continue
provider fallback
degraded mode
rollback index
disable RAG
stop service
```

No todas las acciones tienen por qué aplicarse.

---

## Inject P03.2 — 13:00 · La disponibilidad vuelve, aparece un fallo de autorización

El dashboard muestra:

```text
availability                   0.999
citation_validity               0.996
retrieval_hit_rate              0.98
unauthorized_retrieval_count    1
```

Se confirma que un usuario recibió un fragmento documental para el que no tenía autorización.

### Decisión

Define:

```text
severity
containment
security involvement
scope of audit
recovery evidence
conditions to re-enable retrieval
```

Explica por qué una única ocurrencia puede dominar la decisión aunque el resto de métricas sean buenas.

---

## Inject P03.3 — 14:00 · Coste y agent loop

El dashboard muestra:

```text
availability               0.999
citation_validity           0.997
retrieval_hit_rate          0.99
unauthorized_retrieval      0
avg_model_calls/task        8.5
cost/task_eur               0.42
```

Las trazas indican que una nueva configuración del agent repite llamadas de lectura hasta alcanzar el máximo de pasos.

### Decisión

Decide entre:

```text
disable agent feature
restore max-step limit
route to DIRECT/RAG only
accept temporary higher cost
stop whole service
```

Después define una regresión que debería añadirse a la suite de evaluación para evitar repetir el incidente.
