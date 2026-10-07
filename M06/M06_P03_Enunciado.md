# M06.P03 — Retrieval evaluation mínima

**Modalidad:** individual o parejas  
**Entregable:** Hit Rate@k y decisión entre dos configuraciones

## Objetivo

Medirás el retriever **antes de añadir generación**.

## Dataset

```text
assets/retrieval_eval.jsonl
```

Para la ruta esencial utiliza:

```text
R01
R03
R09
```

`R09` es un caso `NO_EVIDENCE`.

## Tareas

Abre:

```text
notebooks/M06_P03_Retrieval_Evaluation.ipynb
```

### Parte A — Hit Rate@k

Implementa:

```python
hit_rate_at_k(...)
```

Un caso es hit si alguna fuente esperada aparece en top-k.

### Parte B — k=2 frente a k=4

Ejecuta los casos con:

```text
k=2
k=4
```

y compara el resultado.

### Parte C — NO_EVIDENCE

Para `R09`, explica por qué recuperar el documento "menos malo" no debe contarse automáticamente como éxito.

### Parte D — Decisión

Elige el `k` que utilizarás en P04 y justifica la decisión considerando:

- cobertura;
- ruido;
- número de chunks enviados al modelo.

## Ampliación

Implementa MRR, compara MMR o amplía el benchmark al dataset completo.

## Preguntas

1. ¿Por qué separar retrieval eval de generation eval?
2. ¿Por qué `k` alto no es siempre mejor?
3. ¿Qué significa realmente `NO_EVIDENCE`?
