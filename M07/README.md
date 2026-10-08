# Módulo 7 — Estrategia de Inteligencia Artificial Generativa

## Objetivo

M07 cambia el tipo de práctica del curso.

```text
M01–M06
construir · ejecutar · medir · depurar

M07
decidir · priorizar · justificar · gobernar
```

El resultado esperado ya no es código. Es una **decisión defendible** sobre qué merece la pena construir, con qué evidencia, qué datos, qué riesgo y bajo qué condiciones debe avanzar.

Por eso las prácticas de este módulo se realizan como **tabletops y workshops de decisión**. No requieren notebooks, kernel de Python ni llamadas a modelos.

## Ruta práctica

```text
M07.P01  Opportunity Triage
         problema → tarea → fit → autonomía → Use Case Card

M07.P02  Evidence & Readiness Committee
         baseline → métricas → priorización → datos → estrategia técnica

M07.P03  Pilot Gate Under Pressure
         riesgo → controles → resiliencia → GO / NOT_YET / NO_GO
```

## Ubicación recomendada en el deck reducido

```text
Después de slide 9   → M07.P01
Después de slide 19  → M07.P02
Después de slide 25  → M07.P03
Slide 26             → síntesis
```

De esta forma cada tabletop se realiza después de haber explicado los conceptos que necesita.

## Cómo trabajar

Cada práctica incluye un enunciado y una plantilla Markdown en `templates/`.

Duplica la plantilla correspondiente dentro de `work/` y trabaja sobre esa copia. `work/` está ignorado por Git para que tus decisiones y anotaciones no interfieran con futuras actualizaciones del repositorio.

No es necesario escribir Python. Los CSV y JSONL de `assets/` funcionan como **evidence pack**: puedes inspeccionarlos directamente desde JupyterLab cuando necesites justificar una decisión.

## Material

### Enunciados

- `M07_P01_Enunciado.md`
- `M07_P02_Enunciado.md`
- `M07_P03_Enunciado.md`

### Plantillas

- `templates/M07_P01_Opportunity_Triage.md`
- `templates/M07_P02_Evidence_Readiness.md`
- `templates/M07_P03_Pilot_Gate.md`

### Evidencia

- `assets/opportunity_backlog.csv`
- `assets/baseline_procedure_search.csv`
- `assets/prioritization_candidates.csv`
- `assets/data_inventory.csv`
- `assets/risk_scenarios.jsonl`
- `assets/enterprise_genai_assistant_case.md`

## Caso transversal

El Enterprise GenAI Assistant construido hasta M06 se utiliza como caso principal. M07 parte de una PoC técnicamente viable y pregunta si existe evidencia suficiente para avanzar a un piloto controlado.

El criterio del módulo es siempre el mismo:

```text
no avanzar porque la tecnología funcione

avanzar cuando la evidencia justifique
valor + datos + riesgo + operación + ownership
```
