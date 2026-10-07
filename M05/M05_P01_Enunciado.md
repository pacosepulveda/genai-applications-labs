# M05.P01 — Tokenización y presupuesto de contexto

**Ruta esencial**

## Objetivo

Observarás qué recibe realmente un modelo de lenguaje y cómo una aplicación gestiona el presupuesto de contexto.

Abre:

```text
notebooks/M05_P01_Tokenization_Context.ipynb
```

El notebook está completo. Ejecútalo de principio a fin antes de modificar nada.

## Trabajo

1. Inspecciona tokens e IDs de una frase.
2. Observa la fragmentación de identificadores técnicos.
3. Comprueba qué ocurre con `INFORMACION_CRITICA_FINAL` al aplicar truncation.
4. Ejecuta los dos escenarios de `estimate_budget()`.
5. Añade al menos dos identificadores técnicos nuevos.
6. Cambia `max_length=64` a `128` y compara.
7. Aumenta `output_reserve` hasta conseguir que un escenario deje de caber.

## Preguntas

1. ¿Por qué token no equivale a palabra?
2. ¿Por qué un identificador corto puede consumir muchos tokens?
3. ¿Qué riesgo tiene truncar sin estrategia?
4. ¿Por qué la salida también consume context window?
