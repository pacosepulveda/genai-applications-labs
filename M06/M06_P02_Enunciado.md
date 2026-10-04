# M06.P02 — De documentos a retriever: metadata, chunking y vector store

**Modalidad:** individual o parejas  
**Entregable:** índice en memoria y análisis comparativo de estrategias de chunking

## Objetivo

Construirás la parte offline de un RAG:

```text
Markdown -> Document -> metadata -> chunks -> embeddings -> InMemoryVectorStore -> retriever
```

## Dataset

`assets/knowledge_base/` incluye documentación vigente y una versión obsoleta.

## Tareas

Abre `notebooks/M06_P02_Ingestion_VectorStore.ipynb`.

### Parte A — Carga y metadata

Extrae `source_id`, `version`, `status`, `department`, `classification` y `effective_date`.

### Parte B — Inspección

Comprueba documentos, versiones y cuál está `OBSOLETE`.

### Parte C — Chunking

Compara dos configuraciones de `RecursiveCharacterTextSplitter`, registra número de chunks, longitud media y máxima, y conserva metadata del documento padre.

### Parte D — Embeddings locales

Utiliza el modelo precargado `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` mediante `HuggingFaceEmbeddings`, en CPU. No se utiliza Bedrock para embeddings.

Incluye además una representación local didáctica basada en TF-IDF o hashing para entender `vector store != embedding model`.

### Parte E — InMemoryVectorStore

Crea el store y añade los chunks.

### Parte F — Retrieval

Prueba preguntas sobre acceso privilegiado, incidentes P1, RPO de Tier-1 y `/api/v2/status`. Muestra `source_id`, versión, status, fragmento y score.

### Parte G — Vigencia

Demuestra que similitud puede recuperar `PROC-017 v2.1` y exclúyelo antes de construir contexto.

## Preguntas

1. ¿Por qué metadata es parte funcional del RAG?
2. ¿Qué trade-off existe entre chunks pequeños y grandes?
3. ¿Por qué cambiar el embedding model puede requerir reindexar?
4. ¿Por qué una versión obsoleta no debe resolverse con una instrucción al LLM?
