# M06.P01 — Runnables, prompt y structured output

**Ruta de clase** · notebook completamente implementado

## Objetivo

Comprobar que podemos cambiar el componente generativo sin cambiar el contrato que recibe el backend.

Abre `notebooks/M06_P01_Runnables_Structured_Output.ipynb` y ejecútalo de arriba abajo.

## Experimentos

1. Inspecciona el `ChatPromptTemplate` y localiza los roles `system` y `user`.
2. Ejecuta el pipeline determinista y confirma que el resultado es un `IncidentAnalysis`.
3. Cambia `requires_review` en el mock y comprueba que el contrato Pydantic no cambia.
4. Si Bedrock está disponible, ejecuta la misma entrada con GPT-5.6 Luna y compara el tipo de salida.
5. Introduce deliberadamente un JSON incompatible con el schema y observa dónde falla.

## Preguntas

- ¿Qué ventaja aporta mantener un contrato Pydantic estable?
- ¿Qué valida el schema y qué no puede validar?
- ¿Qué parte del sistema cambia al sustituir mock por Luna?

## Ampliación

Prueba `batch()`, `RunnableParallel` o `ainvoke()`.
