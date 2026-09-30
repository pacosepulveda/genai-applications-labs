# Caso M07 — Enterprise GenAI Assistant

## Problema

Los técnicos de operaciones y seguridad deben localizar rápidamente procedimientos vigentes durante incidentes y tareas operativas. La información está distribuida entre varias fuentes y existe riesgo de abrir documentación histórica.

## Capability construida hasta M06

La aplicación ya dispone conceptualmente de:

```text
DIRECT
RAG obligatorio para conocimiento corporativo
AGENT read-only para asistencia operacional
```

Controles técnicos existentes:

- filtrado de documentación obsoleta;
- metadata;
- citation validation;
- no-answer;
- tools read-only;
- separación entre policy y modelo;
- estado por thread.

## Baseline de ejercicio

El fichero:

```text
baseline_procedure_search.csv
```

contiene observaciones ficticias del proceso actual.

No deben asumirse como datos de una organización real.

## Alcance candidato del piloto

Usuarios:

```text
20 técnicos de Operations/Security
```

Fuentes iniciales:

```text
procedimientos operativos
políticas corporativas
runbooks aprobados
```

Funciones propuestas:

```text
buscar procedimientos
responder con citas
resumir incidentes
consultar incidentes read-only
calcular duraciones
```

Funciones explícitamente fuera de alcance:

```text
aplicar cambios en producción
aprobar accesos
enviar comunicaciones externas automáticamente
```

## Restricciones

- No debe existir fallback directo al conocimiento paramétrico cuando se exijan fuentes corporativas.
- Documentos OBSOLETE no deben utilizarse como evidencia operativa.
- Las ACL deben aplicarse antes del contexto del modelo.
- Los logs no deben almacenar secretos ni texto completo de forma indiscriminada.
- Acciones de escritura quedan fuera del piloto.

## Pregunta del comité

> ¿Debemos pasar de PoC técnico a piloto read-only?  
> ¿Qué condiciones deben cumplirse antes de producción?  
> ¿Qué funcionalidades deberían quedar como NOT YET?
