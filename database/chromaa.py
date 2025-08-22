from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

import tempfile

def ChromaDB(n):
    temp_dir = tempfile.mkdtemp()
    vectorstore = Chroma.from_documents(
        documents=n,
        embedding=embeddings,
        persist_directory=temp_dir,  # temporary directory
    )
    return vectorstore

