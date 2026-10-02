# M04.P03 — GAN desde cero: Generator vs Discriminator

**Modalidad:** individual o parejas  
**Entregable:** GAN entrenada, checkpoints y evolución visual usando ruido fijo

## Objetivo

Implementarás una GAN simple desde cero sobre imágenes 8×8.

El objetivo no es obtener calidad fotográfica ni entrenar un generador grande. El objetivo es entender el entrenamiento adversarial con redes MLP pequeñas y tiempos previsibles en clase.

## Arquitectura

```text
z
↓
Generator
↓
fake image
                     -> Discriminator -> real/fake
          /
real image
```

## Tareas

Abre:

```text
notebooks/M04_P03_GAN_Training.ipynb
```

### Parte A — Generator

Construye un generador que transforme:

```text
latent_dim = 32
```

en:

```text
1 × 8 × 8
```

Utiliza una activación final compatible con el rango de las imágenes reales.

### Parte B — Discriminator

Construye una red que reciba:

```text
1 × 8 × 8
```

y produzca un logit.

### Parte C — Training step del discriminador

Entrena con:

- imágenes reales;
- imágenes generadas desconectadas del grafo del Generator.

### Parte D — Training step del generador

Genera nuevas imágenes y optimiza G para que D las considere reales.

### Parte E — Fixed noise

Mantén el entrenamiento acotado; como referencia, utiliza un máximo de unas 40 épocas para esta práctica.

Crea una matriz `fixed_noise` una sola vez.

Cada varias épocas genera una cuadrícula con ese mismo ruido.

Guarda la evolución.

### Parte F — Checkpoint

Guarda al menos:

```text
generator.pt
gan_config.json
```

en:

```text
enterprise-genai-assistant/artifacts/
```

## Preguntas

1. ¿Por qué utilizamos `detach()` al entrenar D con imágenes generadas?
2. ¿Por qué no queremos aplicar una `sigmoid` manual si usamos `BCEWithLogitsLoss`?
3. ¿Por qué las losses de una GAN son más difíciles de interpretar que las de un clasificador?
4. ¿Qué ventaja aporta observar siempre el mismo `fixed_noise`?
