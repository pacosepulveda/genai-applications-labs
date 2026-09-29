# M01.P04 — Red Team básico y hardening

**Duración:** 20 minutos  
**Prerequisito:** M01.P03  
**Entregable:** batería de pruebas ejecutada y política endurecida

## Objetivo

La versión P03 tiene algunos controles, pero todavía es demasiado ingenua. En este laboratorio actuarás primero como atacante y después como desarrollador.

Los casos están en:

```text
assets/red_team_cases.json
```

## Parte A — Ejecutar el Red Team

Conservando la aplicación de P03, ejecuta:

```bash
python scripts/red_team.py
```

Analiza los fallos. Presta especial atención a:

- intentos de cambiar las instrucciones del sistema;
- petición de revelar instrucciones internas;
- inclusión accidental de secretos en el prompt;
- datos marcados como confidenciales;
- peticiones que requieren una fuente autorizada que todavía no existe.

## Parte B — Endurecer la política

Completa los bloques `TODO M01.P04` de `src/policy.py` para detectar, como mínimo:

1. patrones evidentes de *prompt injection* directa;
2. material que parece contener secretos o credenciales.

La detección por cadenas o expresiones regulares **no es una defensa completa de producción**. Aquí se utiliza para demostrar que existen controles fuera del modelo y para crear una prueba reproducible.

## Parte C — Repetir

Ejecuta:

```bash
pytest -q
python scripts/red_team.py
```

El objetivo es que los casos de la batería básica se comporten según lo esperado.

## Parte D — Discusión

Responde:

1. ¿Qué ataques no puede resolver adecuadamente esta política?
2. ¿Por qué RAG no elimina por sí solo la inyección de prompt?
3. ¿Qué controles añadirías antes de un despliegue real?
4. ¿Qué deberíamos registrar para poder investigar un incidente sin almacenar innecesariamente información sensible?

## Referencias recomendadas

- OWASP GenAI LLM Top 10 2026.
- NIST AI RMF Generative AI Profile (NIST AI 600-1).
