from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from rag.loader import documents

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory="rag/chroma"
)

print("✅ ChromaDB created successfully.")