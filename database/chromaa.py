from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Make sure you use a folder your app can write to
PERSIST_DIR = "chromadb"  # relative to app root
os.makedirs(PERSIST_DIR, exist_ok=True)

def ChromaDB(documents):
    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=PERSIST_DIR,
        collection_name="vidquery_collection"
    )
    vectorstore.persist()
    return vectorstore
