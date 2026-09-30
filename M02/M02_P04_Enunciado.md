# M02.P04 — Detección no supervisada de anomalías

**Modalidad:** individual o parejas  
**Entregable:** notebook con modelo de anomalías y análisis de resultados

## Objetivo

No todos los problemas tienen una etiqueta disponible.

Trabajarás con `assets/telemetry_events.csv`, que representa telemetría simplificada del Enterprise GenAI Assistant.

Las variables incluyen:

- latencia;
- longitud de entrada;
- longitud de salida;
- errores recientes del proveedor;
- bloqueos;
- código HTTP.

La columna `is_known_anomaly` existe únicamente para evaluar el ejercicio al final. **No debe utilizarse para entrenar el detector.**

## Tareas

Abre `notebooks/M02_P04_Anomaly_Detection.ipynb`.

1. Explora las distribuciones.
2. Selecciona features numéricas apropiadas.
3. Escálalas.
4. Entrena un `IsolationForest` sin utilizar `is_known_anomaly`.
5. Convierte su salida a:
   - normal;
   - anomalía.
6. Compara posteriormente con `is_known_anomaly`.
7. Analiza falsos positivos y falsos negativos.
8. Utiliza PCA para proyectar las features a dos dimensiones y visualizar los eventos.

## Discusión

- ¿Por qué una anomalía estadística no equivale necesariamente a un incidente?
- ¿Qué pasaría si la distribución normal de latencia cambiara tras migrar de proveedor?
- ¿Qué diferencia habría entre `data drift` y un incidente puntual?
