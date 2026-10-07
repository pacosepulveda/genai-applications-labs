# M06.P02 — De documentos a retriever

**Ruta de clase** · notebook completamente implementado

## Objetivo

Observar el pipeline `Document -> chunks -> embeddings -> vector store -> retrieval` y comprobar por qué metadata y vigencia forman parte del comportamiento del RAG.

Abre `notebooks/M06_P02_Ingestion_VectorStore.ipynb` y ejecútalo.

## Experimentos

1. Inspecciona `source_id`, `version`, `status` y `classification`.
2. Localiza `PROC-017` vigente y la versión `OBSOLETE`.
3. Ejecuta las consultas preparadas y revisa qué documentos devuelve el retriever.
4. Comprueba que el filtro `only_current()` excluye la versión obsoleta del contexto final.
5. Cambia una consulta por otra equivalente y observa si cambia el ranking.
6. Opcional: cambia `chunk_size=500` por `300` y compara el resultado.

## Preguntas

- ¿Por qué similarity no equivale a vigencia?
- ¿Por qué la metadata debe sobrevivir al chunking?
- ¿Qué implicaría cambiar el embedding model de un índice ya construido?
