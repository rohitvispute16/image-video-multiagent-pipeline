from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

_embeddings = None
_db = None
_retriever = None


def get_retriever():
    global _embeddings, _db, _retriever

    if _retriever is None:
        print("Loading HuggingFace embedding model...")

        _embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        _db = Chroma(
            persist_directory="rag/chroma",
            embedding_function=_embeddings,
        )

        _retriever = _db.as_retriever(
            search_kwargs={"k": 3}
        )

    return _retriever