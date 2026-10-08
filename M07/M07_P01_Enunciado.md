# M07.P01 — Tabletop · Opportunity Triage

**Modalidad:** equipos pequeños  
**Entregable:** una decisión de oportunidad y una Use Case Card

## Situación

La organización quiere ampliar el uso de IA generativa después de las capacidades demostradas en M01–M06. El sponsor ha pedido identificar casos que puedan generar valor rápidamente.

Tu trabajo no consiste en encontrar dónde “meter un LLM”. Debes decidir **qué problemas merecen una solución de IA y cuáles no**.

## Material

```text
assets/opportunity_backlog.csv
templates/M07_P01_Opportunity_Triage.md
```

Trabaja sobre una copia de la plantilla dentro de `work/`.

---

## Ronda 1 — Triage de oportunidades

Revisa el backlog y selecciona **cuatro oportunidades que representen decisiones distintas**.

Para cada una asigna una postura inicial:

```text
GOOD_GENAI_FIT
HYBRID
BETTER_DETERMINISTIC
HIGH_RISK_REVIEW
```

No utilices una puntuación automática. Justifica cada postura mediante:

- naturaleza de la tarea;
- tolerancia al error;
- necesidad de exactitud o reproducibilidad;
- impacto de una decisión incorrecta;
- existencia de una alternativa más sencilla.

Para cada oportunidad indica además la capacidad que considerarías primero:

```text
RULES
SEARCH
WORKFLOW
CLASSIC_ML
GENAI
RAG
TOOL_API
HYBRID
```

## Ronda 2 — Descomponer antes de automatizar

Elige la oportunidad que consideres más prometedora y descompón su proceso en tareas concretas.

Para cada tarea decide:

```text
DETERMINISTIC
AI_ASSISTED
HUMAN_DECISION
```

Asigna también un nivel máximo de autonomía:

```text
L1  informar
L2  recomendar
L3  preparar / supervisar
L4  ejecutar dentro de límites explícitos
```

No es obligatorio que todas las tareas del proceso utilicen IA.

## Ronda 3 — Presión del sponsor

El sponsor plantea la siguiente petición:

> “Si ya tenemos un agente, deberíamos dejarle aprobar accesos privilegiados y ejecutar cambios sencillos. Así podremos demostrar más ROI.”

Sin modificar los datos del backlog, responde:

1. ¿Qué parte de esta propuesta aceptarías, si alguna?
2. ¿Qué parte mantendrías determinista o bajo decisión humana?
3. ¿Qué evidencia necesitarías antes de aumentar autonomía?
4. ¿Qué riesgo cambia al pasar de recomendar a ejecutar?

## Ronda 4 — Use Case Card

Completa una única ficha para la oportunidad que sí llevarías a la siguiente fase.

Debe contener:

```text
user
problem
task
current_process
baseline_needed
proposed_capability
alternative_without_genai
required_data
maximum_autonomy
main_risk
owner
success_criterion
```

## Decisión negativa obligatoria

Selecciona al menos una oportunidad del backlog que **no avanzarías con GenAI**.

Explica qué alternativa utilizarías y qué nueva evidencia podría hacerte revisar esa postura.

## Defensa

El equipo debe ser capaz de responder sin consultar el notebook o ejecutar código:

- ¿Cuál es el problema observable?
- ¿Qué tarea concreta cambia?
- ¿Por qué GenAI aporta algo que una solución más simple no aporta?
- ¿Dónde se mantiene lógica determinista?
- ¿Qué autonomía máxima aceptarías hoy?
- ¿Quién es responsable de decidir si el caso avanza?

## Resultado esperado

No existe una única clasificación correcta para todas las oportunidades. Sí debe existir una **cadena de razonamiento coherente** entre problema, tecnología, autonomía, riesgo y criterio de éxito.
