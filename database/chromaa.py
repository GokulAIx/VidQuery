from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def ChromaDB(documents , user_YT):
    vectorstore = Chroma(
        embedding_function=embeddings,
        persist_directory="./chroma_db", 
        collection_name=user_YT
    )       
    if vectorstore.get()['documents']:
        return vectorstore



    if not documents:
        return vectorstore
    
    vectorstore.add_documents(documents)
    return vectorstore    