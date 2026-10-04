# M02.P02 — Baseline y clasificador de intenciones

**Modalidad:** individual o parejas  
**Entregable:** pipeline entrenado, baseline comparado y artefacto `intent_router.joblib`

## Objetivo

Construirás el primer componente de Machine Learning del proyecto transversal: un **router de intenciones**.

Debe clasificar solicitudes en:

- `DRAFT`
- `SUMMARIZE`
- `CLASSIFY`
- `QUESTION`
- `CODE`
- `CORPORATE_KNOWLEDGE`
- `UNSUPPORTED`

## Restricción importante

No utilices `final_route` como feature. Esa columna representa información disponible después de resolver la solicitud y produciría **data leakage**.

## Decisión didáctica sobre el split

En P01 has comparado un split aleatorio estratificado con un split temporal. En esta práctica utilizaremos deliberadamente un **split aleatorio estratificado** para mantener representación de todas las clases y obtener resultados reproducibles durante el laboratorio.

Esto no significa que sea siempre la estrategia adecuada para producción. Si el objetivo es estimar comportamiento futuro y existe dependencia temporal, un holdout temporal puede ser más realista.

## Tareas

Abre `notebooks/M02_P02_Intent_Classifier.ipynb`.

1. Carga el dataset.
2. Separa features y target.
3. Reserva un test estratificado con `random_state=42`.
4. Crea un **baseline** con `DummyClassifier`.
5. Construye un `Pipeline` que combine:
   - `TfidfVectorizer` para `request_text`;
   - `OneHotEncoder` para variables categóricas;
   - un clasificador supervisado.

La opción recomendada para empezar es `LogisticRegression`.

6. Entrena el pipeline.
7. Compara el modelo con el baseline mediante:
   - accuracy;
   - macro F1: calcula F1 por clase dando el mismo peso a todas;
   - weighted F1: calcula F1 por clase ponderando según el número de ejemplos de cada una.
8. Obtén la matriz de confusión.
9. Revisa al menos cinco errores.
10. Guarda el pipeline completo en:

```text
enterprise-genai-assistant/artifacts/intent_router.joblib
```

## Preguntas

- ¿Por qué guardamos el pipeline completo y no solo el clasificador?
- ¿Qué ventaja aporta TF-IDF frente a utilizar directamente cadenas?
- ¿Por qué macro F1 es relevante cuando las clases no tienen el mismo tamaño?
- ¿Qué errores serían más costosos para la aplicación?
