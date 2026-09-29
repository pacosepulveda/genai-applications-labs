# M01.P01 — ¿IA, ML, GenAI o software convencional?

**Modalidad:** parejas o grupos de 3  
**Entregable:** matriz de decisión completada en el notebook

## Contexto

Una de las decisiones más importantes de un proyecto de IA ocurre antes de elegir modelo, framework o proveedor: **decidir si realmente hace falta IA y qué tipo de capacidad necesita el problema**.

En este laboratorio analizarás diez situaciones empresariales. No busques una palabra clave que “revele” la respuesta. Debes justificar la solución a partir de:

- la naturaleza de la entrada;
- el tipo de salida esperado;
- si existe una regla exacta;
- si necesitamos aprender patrones históricos;
- si necesitamos generar contenido nuevo;
- si necesitamos recuperar información existente;
- el impacto de equivocarnos.

## Categorías

Utiliza una de estas categorías principales:

- `RULES`: software determinista / reglas.
- `SEARCH`: recuperación o búsqueda de información.
- `ML`: Machine Learning predictivo o discriminativo.
- `GENAI`: generación mediante un modelo generativo.
- `OPTIMIZATION`: algoritmo de optimización.
- `HYBRID`: combinación de varias capacidades.

## Tarea

1. Abre `notebooks/M01_P01_Technology_Fit.ipynb` en el entorno web de laboratorio.
2. Carga `assets/technology_cases.csv`.
3. Para cada caso indica:
   - categoría principal;
   - si utilizarías o no un LLM;
   - justificación en una o dos frases;
   - principal riesgo de una mala elección tecnológica.
4. Selecciona dos casos en los que exista **más de una solución razonable** y explica de qué depende la decisión.
5. Responde a la pregunta final: **¿en cuáles de los diez casos un LLM sería técnicamente posible pero arquitectónicamente innecesario o contraproducente?**

## Criterio de éxito

No se evalúa que coincidas palabra por palabra con una solución única. Se evalúa que puedas justificar la arquitectura y que no confundas “un modelo puede hacerlo” con “es la tecnología adecuada para hacerlo”.
