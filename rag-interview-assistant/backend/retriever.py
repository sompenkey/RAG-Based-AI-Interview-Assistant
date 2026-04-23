from langchain_community.vectorstores import FAISS
from backend.embeddings import get_embeddings

def create_vectorstore(chunks):
    embeddings = get_embeddings()
    db = FAISS.from_texts(chunks, embeddings)
    return db

def get_retriever(db):
    return db.as_retriever(search_kwargs={"k": 3})