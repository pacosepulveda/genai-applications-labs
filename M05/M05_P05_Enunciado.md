# M05.P05 — Resumen, traducción y evaluación

**Modalidad:** individual o parejas  
**Entregable:** outputs, métricas simples y análisis de errores sobre un pequeño eval set

## Objetivo

Utilizarás un modelo text-to-text para resolver tareas generativas, pero la parte principal será **evaluarlas**.

## Dataset

Utiliza:

```text
assets/nlp_eval_cases.jsonl
```

Incluye casos de:

- resumen;
- traducción;
- generación.

## Parte A — Resumen

Con FLAN-T5:

1. resume los casos `SUM-*`;
2. compara con la referencia;
3. calcula una métrica ROUGE-1 simplificada;
4. verifica manualmente las restricciones `must_include`.

No interpretes ROUGE como factualidad.

## Parte B — Traducción

Traduce los casos `TR-*`.

Comprueba programáticamente que se conservan:

```text
${CUSTOMER_ID}
INC-2048
/api/v2/status
```

### Parte C — Hallucination check

Para cada resumen:

1. identifica afirmaciones concretas;
2. marca cuáles aparecen soportadas por el input;
3. registra cualquier detalle inventado.

### Parte D — Comparar decoding

Para una tarea de resumen compara:

- greedy;
- beam search;
- sampling.

Decide cuál utilizarías y justifica según el tipo de tarea.

### Parte E — Regression eval

Genera una tabla:

```text
case_id
task
output
rouge1
constraints_ok
notes
```

Guárdala como:

```text
m05_eval_results.csv
```

## Preguntas

1. ¿Por qué ROUGE no detecta automáticamente una alucinación?
2. ¿Por qué los placeholders requieren validación específica?
3. ¿Por qué un eval set privado es útil en una organización?
4. ¿Qué pruebas añadirías antes de cambiar de modelo?
