# Enterprise GenAI Assistant — M03

La implementación está completa para que el laboratorio se centre en comparar comportamiento y políticas.

## 1. Generar los archivos de modelo

Ejecuta primero `M03.P02`. El notebook guarda en `artifacts/`:

```text
classic_router.joblib
neural_preprocessor.joblib
neural_label_encoder.joblib
neural_router.pt
neural_router_config.json
```

## 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 3. Tests

```bash
pytest -q
```

## 4. Ejecutar

```bash
uvicorn src.main:app --reload --port 8080
```

Configura `ROUTER_BACKEND=classic` o `ROUTER_BACKEND=neural` para comparar ambos backends.

## Principio de diseño

El backend aprendido es intercambiable. Las políticas deterministas se ejecutan antes del router y no dependen del modelo elegido.
