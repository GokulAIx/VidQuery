from langchain.embeddings import HuggingFaceEmbeddings


embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")



from langchain_community.vectorstores import Chroma


embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def get_retriever(n):
    retriever = n.as_retriever(search_kwargs={"k": 3})
    return retriever
