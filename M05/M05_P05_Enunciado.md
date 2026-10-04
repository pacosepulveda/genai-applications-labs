# M05.P05 — Resumen, traducción, generación y evaluación

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
- generación controlada.

## Parte A — Resumen

Con FLAN-T5:

1. resume los casos `SUM-*`;
2. compara con la referencia;
3. calcula una métrica ROUGE-1 simplificada;
4. verifica manualmente las restricciones `must_include`.

No interpretes ROUGE como factualidad.

## Parte B — Traducción

Traduce los casos `TR-*`.

Comprueba programáticamente que se conservan los spans protegidos, por ejemplo:

```text
${CUSTOMER_ID}
INC-2048
/api/v2/status
```

## Parte C — Generación controlada

Ejecuta los casos `GEN-*`.

Comprueba las restricciones `must_not_claim`.

En `GEN-01`, por ejemplo, el input no proporciona una fecha ni una hora exactas. La salida no debe inventarlas.

Registra cualquier afirmación concreta que no esté soportada por la entrada.

## Parte D — Hallucination check

Para cada resumen y caso de generación:

1. identifica afirmaciones concretas;
2. marca cuáles aparecen soportadas por el input;
3. registra cualquier detalle inventado.

## Parte E — Comparar decoding

Para una tarea de resumen compara:

- greedy;
- beam search;
- sampling.

Decide cuál utilizarías y justifica según el tipo de tarea.

## Parte F — Regression eval

Genera una tabla:

```text
case_id
task
output
metric
constraints_ok
unsupported_claims
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
4. ¿Qué aporta un caso de generación sin referencia única?
5. ¿Qué pruebas añadirías antes de cambiar de modelo?
