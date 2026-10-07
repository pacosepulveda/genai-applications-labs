# M06.P02 — De documentos a retriever

**Modalidad:** individual o parejas  
**Entregable:** retriever en memoria con metadata y filtro de vigencia

## Objetivo

Construirás el pipeline mínimo:

```text
Markdown -> Document -> chunks -> embeddings -> vector store -> retrieval
```

## Dataset

Utiliza:

```text
assets/knowledge_base/
```

El corpus contiene una versión vigente y otra obsoleta de `PROC-017`.

## Tareas

Abre:

```text
notebooks/M06_P02_Ingestion_VectorStore.ipynb
```

### Parte A — Document y metadata

Carga los Markdown y conserva al menos:

```text
source_id
version
status
classification
```

Muestra qué versión está marcada como `OBSOLETE`.

### Parte B — Chunking

Utiliza una única configuración:

```text
chunk_size=500
chunk_overlap=80
```

Comprueba que la metadata del documento padre se mantiene en los chunks.

### Parte C — Embeddings y vector store

Utiliza:

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

con CPU y `InMemoryVectorStore`.

### Parte D — Retrieval observable

Prueba estas dos consultas:

```text
¿Cuánto dura un acceso privilegiado?
¿Cuándo se envían actualizaciones de un P1?
```

Muestra para cada resultado:

```text
source_id
version
status
fragmento
```

### Parte E — Vigencia

Implementa un filtro que impida utilizar documentos con:

```text
status=OBSOLETE
```

Comprueba que `PROC-017 v2.1` nunca entra en el contexto final.

## Ampliación

Compara otro tamaño de chunk o analiza `/api/v2/status`.

## Preguntas

1. ¿Por qué metadata forma parte del comportamiento del RAG?
2. ¿Por qué similitud no equivale a vigencia?
3. ¿Por qué cambiar el embedding model suele requerir reindexar?
