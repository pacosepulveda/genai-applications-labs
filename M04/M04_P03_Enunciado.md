# M04.P03 — GAN desde cero: Generator vs Discriminator

**Modalidad:** individual o parejas  
**Entregable:** GAN entrenada, checkpoint y evolución visual usando ruido fijo

## Objetivo

Implementarás una GAN simple desde cero sobre imágenes 8×8.

El objetivo no es obtener calidad fotográfica ni entrenar un generador grande. El objetivo es entender el entrenamiento adversarial con redes MLP pequeñas y tiempos previsibles en una `ml.t3.large` sin GPU.

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

Utiliza una MLP pequeña y una activación final compatible con el rango `[-1,1]` de las imágenes reales.

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

Mantén el entrenamiento acotado; como referencia, utiliza un máximo aproximado de 40 épocas.

Crea `fixed_noise` una sola vez y reutilízalo cada varias épocas para observar la evolución de las mismas entradas latentes.

### Parte F — Checkpoints

Guarda un artefacto ligero para serving:

```text
enterprise-genai-assistant/artifacts/generator.pt
enterprise-genai-assistant/artifacts/gan_config.json
```

Guarda además un checkpoint de entrenamiento que incluya como mínimo:

```text
generator_state_dict
discriminator_state_dict
optimizer_g_state_dict
optimizer_d_state_dict
epoch
config
```

Así podrás reanudar o inspeccionar el experimento sin confundir serving con estado de entrenamiento.

## Preguntas

1. ¿Por qué utilizamos `detach()` al entrenar D con imágenes generadas?
2. ¿Por qué no queremos aplicar una `sigmoid` manual si usamos `BCEWithLogitsLoss`?
3. ¿Por qué las losses de una GAN son más difíciles de interpretar que las de un clasificador?
4. ¿Qué ventaja aporta observar siempre el mismo `fixed_noise`?
5. ¿Por qué `generator.pt` y un checkpoint completo resuelven necesidades distintas?
