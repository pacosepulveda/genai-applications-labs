# M06.P02 — De documentos a retriever: metadata, chunking y vector store

**Modalidad:** individual o parejas  
**Entregable:** índice en memoria y análisis comparativo de estrategias de chunking

## Objetivo

Construirás la parte **offline** de un RAG.

```text
Markdown
-> Document
-> metadata
-> chunks
-> embeddings
-> InMemoryVectorStore
-> retriever
```

## Dataset

Utiliza:

```text
assets/knowledge_base/
```

La base contiene documentación vigente y una versión obsoleta.

## Tareas

Abre:

```text
notebooks/M06_P02_Ingestion_VectorStore.ipynb
```

### Parte A — Carga

Lee cada Markdown y crea un `Document`.

Extrae del front matter:

```text
source_id
version
status
department
classification
effective_date
```

### Parte B — Inspección

Antes de indexar, verifica:

- cuántos documentos hay;
- qué versiones existen;
- cuál está `OBSOLETE`.

### Parte C — Chunking

Compara dos configuraciones de `RecursiveCharacterTextSplitter`.

Ejemplo conceptual:

```text
A: chunks pequeños
B: chunks mayores
```

Para cada una registra:

- número de chunks;
- longitud media;
- longitud máxima.

Conserva metadata del documento padre.

### Parte D — Embeddings

El entorno puede utilizar:

```text
HuggingFaceEmbeddings
```

con el modelo precargado por el instructor.

Construye también una alternativa local didáctica basada en hashing o TF-IDF para entender que:

```text
vector store != embedding model
```

### Parte E — InMemoryVectorStore

Crea:

```python
InMemoryVectorStore(...)
```

y añade chunks.

### Parte F — Retrieval

Prueba preguntas sobre:

- acceso privilegiado;
- incidentes P1;
- RPO de Tier-1;
- endpoint `/api/v2/status`.

Muestra:

```text
source_id
version
status
fragmento
score
```

### Parte G — Documento obsoleto

Demuestra que la similitud por sí sola puede recuperar `PROC-017 v2.1`.

Después evita utilizarlo mediante metadata/filtering en tu lógica de retrieval.

## Preguntas

1. ¿Por qué metadata es parte funcional del RAG?
2. ¿Qué trade-off existe entre chunks pequeños y grandes?
3. ¿Por qué cambiar el embedding model puede requerir reindexar?
4. ¿Por qué una versión obsoleta no debe resolverse mediante una instrucción al LLM?
