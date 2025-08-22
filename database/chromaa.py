from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def ChromaDB(n):
    vectorstore = Chroma.from_documents(
        documents=n,
        embedding=embeddings,
        persist_directory=None  # in-memory
    )
    return vectorstore
