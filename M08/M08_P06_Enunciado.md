# M08.P06 — Enterprise GenAI Assistant v0.8: Operating Model Pack

**Modalidad:** equipos pequeños  
**Entregable:** `M08_Operating_Model_Pack.md`

## Objetivo

Diseñar la organización capaz de ejecutar el piloto definido en M07 y operar posteriormente el servicio.

## Material

```text
assets/enterprise_genai_assistant_v08_case.md
```

Además reutiliza los resultados de P01–P05.

## Parte A — Team Topology

Define:

```text
Product Squad
AI Platform
Governance/Risk/Enablement
```

Para cada bloque:

```text
mission
capabilities
roles
interfaces
```

## Parte B — Ownership Map

Asigna owner a:

```text
product
service
model catalog
prompt
knowledge corpus
ingestion pipeline
index
eval datasets
incident tool
risk
cost
```

Evita:

```text
"AI Team"
```

como owner genérico.

## Parte C — RACI crítica

Incluye al menos:

- nuevo data source;
- prompt change;
- model change;
- index release;
- new read tool;
- future write tool;
- production deployment;
- risk acceptance;
- AI incident.

## Parte D — Delivery / LLMOps

Define:

```text
Git workflow
quality gates
environments
versioned artifacts
promotion
rollback
```

## Parte E — Operations Readiness

Antes de producción, comprueba:

```text
SLO
dashboard
alerts
on-call
runbooks
kill switch
incident process
cost dashboard
```

## Parte F — Talent Plan

Define:

- upskill;
- reskill;
- recruiting;
- partners;
- bus-factor mitigations.

## Parte G — Change Management

Incluye:

```text
executive sponsor
user champions
AI literacy
training
feedback
communication
```

## Parte H — Operating Model Pack

Genera un documento con:

```text
Executive summary
Team topology
Roles and skill gaps
Ownership
RACI
Delivery workflow
LLMOps quality gates
Operations
Talent plan
Change management
Open risks/dependencies
```

## Preguntas finales

1. ¿Qué capacidades centralizarías?
2. ¿Qué capacidades deben estar cerca del dominio?
3. ¿Quién es accountable del servicio productivo?
4. ¿Quién es owner del contenido RAG?
5. ¿Qué ocurre si AI Platform se convierte en bottleneck?
6. ¿Qué debemos tener listo antes de M09 y de escalar a nuevos casos?
