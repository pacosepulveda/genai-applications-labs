# M08.P01 — Operating Model & Decision Rights

**Modalidad:** equipos pequeños  
**Entregable:** operating model de una página + mapa de decision rights

## Objetivo

Convertirás un conjunto de capabilities en responsabilidades operables para Enterprise GenAI Assistant.

No empezarás por títulos. Empezarás por:

```text
capability
owner
decision right
escalation path
```

## Material

```text
assets/enterprise_genai_assistant_v08_case.md
assets/ownership_activities.csv
templates/M08_P01_Operating_Model_Worksheet.md
```

No necesitas ningún artefacto generado en M07.

## Situación inicial

La aplicación está entrando en una fase operativa. Participan cuatro grupos:

```text
Product Squad
AI Platform
Security / Risk
Service Operations
```

El problema es que varias responsabilidades todavía están expresadas como "AI Team", "IT" o "the business".

## Parte A — Capabilities

Para cada actividad de `ownership_activities.csv`, identifica la capability principal:

```text
PRODUCT
AI_SOFTWARE
DATA_KNOWLEDGE
DOMAIN_SME
PLATFORM
SECURITY_RISK
SERVICE_OPERATIONS
```

Después decide qué grupo debe participar.

## Parte B — Owner único

Asigna un owner concreto a cada actividad.

Evita ownership difuso como:

```text
AI Team
IT
Everyone
The business
```

Una actividad puede requerir colaboración de varios grupos, pero debe quedar claro quién responde por el resultado.

## Parte C — Decision rights

Para cada actividad define quién puede:

```text
APPROVE
BLOCK
ROLLBACK
```

No todas las actividades necesitan los tres derechos.

Presta especial atención a:

- cambio de modelo;
- publicación de corpus;
- cambio de ACL;
- promoción a producción;
- rollback durante un incidente;
- aceptación de riesgo residual.

## Parte D — Interfaces

Identifica al menos tres handoffs críticos y conviértelos en interfaces explícitas.

Ejemplo:

```text
Data/Knowledge publica un nuevo corpus
→ Product valida propósito
→ Security valida ACL
→ Delivery ejecuta retrieval eval
→ owner autorizado aprueba promoción
```

## Inyecto 1 — "Que AI Engineering sea owner de todo"

El sponsor propone simplificar el modelo:

> Como la aplicación es de IA, AI Engineering debería ser owner del prompt, corpus, riesgo, coste e incidentes.

Decide:

```text
ACCEPT
REJECT
ACCEPT_WITH_LIMITS
```

y justifica qué responsabilidades no deberían transferirse.

## Inyecto 2 — Rollback a las 02:00

Una nueva versión del índice empieza a devolver fuentes incorrectas durante una incidencia crítica.

El Product Owner no está disponible.

Debéis decidir:

- quién puede ordenar rollback inmediato;
- quién debe ser informado;
- qué evidencia mínima se necesita para actuar;
- qué decisión puede esperar al horario normal.

## Entregable

Completa:

```text
templates/M08_P01_Operating_Model_Worksheet.md
```

El resultado debe incluir:

```text
capability map
owners
decision rights
escalation paths
interfaces críticas
respuesta a los dos inyectos
```

## Debrief

1. ¿Qué diferencia hay entre capability, participación y accountability?
2. ¿Qué decisiones no deben quedar en manos exclusivas de AI Engineering?
3. ¿Quién puede bloquear una release por riesgo?
4. ¿Quién puede ordenar un rollback urgente?
5. ¿Qué ownership del corpus permanece cerca del dominio aunque la infraestructura RAG sea compartida?
