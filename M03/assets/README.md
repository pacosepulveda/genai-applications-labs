# Assets del M03

`intent_requests.csv` es el mismo conjunto de solicitudes utilizado en M02. Se reutiliza deliberadamente para comparar un modelo clásico y una red neuronal sobre **el mismo problema y la misma partición**.

El laboratorio CNN utiliza `sklearn.datasets.load_digits`, que forma parte de scikit-learn y no requiere descargar un dataset externo.

El laboratorio de atención genera secuencias sintéticas dentro del propio notebook para que sea reproducible y no dependa de servicios externos.
