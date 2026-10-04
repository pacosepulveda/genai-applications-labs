# Caso M07 — Enterprise GenAI Assistant v0.7

## Punto de partida

M06 ha demostrado viabilidad técnica para tres modos:

```text
DIRECT
RAG obligatorio para conocimiento corporativo
AGENT read-only para asistencia operacional
```

Controles ya demostrados:

- documentación obsoleta excluida;
- metadata y citas verificables;
- `NO_EVIDENCE`;
- tools read-only;
- policy separada del modelo;
- estado aislado por thread.

## Problema

Los técnicos de Operations pierden tiempo localizando el procedimiento vigente
durante incidencias y, en algunos casos, terminan utilizando una fuente incorrecta
o escalando la consulta a un experto.

## Baseline del caso

El dataset del laboratorio reproduce aproximadamente:

```text
11 min   mediana de búsqueda
6%       documento incorrecto
18%      escalado a experto
```

## Gate actual

```text
PoC -> Pilot
```

La pregunta no es si la demo funciona.

La pregunta es si existe evidencia suficiente para probar valor con usuarios reales
dentro de un alcance controlado.

## Alcance candidato del piloto

```text
20 técnicos
1 departamento: Operations
5 procedimientos aprobados
8 semanas
modo read-only
```

Procedimientos iniciales:

```text
PROC-017
PROC-021
PROC-031
POL-004
STD-009
```

Funciones incluidas:

- búsqueda RAG;
- respuesta con citas;
- consulta read-only de incidentes;
- cálculo de duración de incidentes.

Funciones fuera de alcance:

- ejecutar cambios en producción;
- aprobar accesos privilegiados;
- tools de escritura;
- comunicaciones externas automáticas.

## Criterios de éxito

```text
reducción del tiempo mediano >= 30%
citation validity >= 98%
satisfacción >= 4/5
```

## Criterios de parada o replanteamiento

```text
retrieval miss > 15%
alucinación crítica
security blocker
```

## Preguntas del comité

1. ¿Debe el RAG read-only pasar a piloto?
2. ¿Debe incluirse la consulta read-only de incidentes?
3. ¿Qué capacidades quedan en NOT_YET?
4. ¿Qué capacidades reciben NO_GO para este alcance?
5. ¿Qué debe demostrar el piloto antes de Production?
