# M02.P01 — Datos, particiones y fuga de información

**Modalidad:** individual o parejas  
**Entregable:** notebook completado con diagnóstico de calidad y estrategia de partición

## Objetivo

Antes de entrenar un modelo debes demostrar que el dataset permite formular un experimento válido.

Trabajarás con `assets/intent_requests.csv`, un conjunto de solicitudes dirigidas a un asistente corporativo.

El objetivo futuro será predecir la columna `label`, pero **en esta práctica no debes entrenar todavía el modelo final**.

## Tareas

Abre `notebooks/M02_P01_Data_Quality_Leakage.ipynb`.

1. Inspecciona:
   - número de filas y columnas;
   - tipos de datos;
   - valores nulos;
   - duplicados;
   - distribución de `label`;
   - periodo cubierto por `created_at`.

2. Clasifica las columnas en:
   - identificadores;
   - features candidatas;
   - target;
   - metadatos;
   - posibles fugas de información.

3. Localiza al menos **una columna que no debería utilizarse como feature** porque revelaría directa o indirectamente el resultado.

4. Compara dos estrategias de partición:
   - split aleatorio estratificado;
   - split temporal.

   En el split aleatorio, **estratificar por `label`** significa mantener aproximadamente la proporción de cada clase en train y test. Esto ayuda a evitar que una clase poco frecuente quede accidentalmente mal representada en una de las particiones.

5. Explica cuál utilizarías para:
   - una prueba didáctica inicial;
   - una estimación más realista del comportamiento futuro.

6. Genera dos DataFrames:
   - `train_df`;
   - `test_df`.

7. Verifica programáticamente que no existe solapamiento de `request_id`.

## Criterios de éxito

Tu notebook debe dejar claro:

- cuál es el target;
- qué columnas usarías;
- cuál excluirías por leakage;
- qué distribución tiene cada clase;
- qué estrategia de split has elegido y por qué.
