from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.retrievers.multi_query import MultiQueryRetriever
import os 
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever

class SafeRetriever:
    def __init__(self, retriever):
        self.retriever = retriever

    def invoke(self, query):
        # 🔒 block empty / whitespace queries
        if not query or not query.strip():
            return []
        return self.retriever.invoke(query)



embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def get_retriever(n):
    retriever = n.as_retriever(search_kwargs={"k": 3})
    return retriever

def get_multi_query_retriever(vectorstore):

    llm_for_queries = ChatGoogleGenerativeAI(model="gemini-2.5-flash"
, google_api_key=os.getenv("GOOGLE_API_KEY"))


    retriever_base = SafeRetriever(
    vectorstore.as_retriever(search_kwargs={"k": 10})
)



    multi_query_retriever = MultiQueryRetriever.from_llm(
        retriever=retriever_base,
        llm=llm_for_queries,
        include_original=True 
    )
    return multi_query_retriever




def get_hybrid_retriever(vectorstore, documents):

    bm25_retriever = BM25Retriever.from_documents(documents)
    bm25_retriever.k = 5 


    semantic_retriever = get_multi_query_retriever(vectorstore)


    ensemble_retriever = EnsembleRetriever(
        retrievers=[bm25_retriever, semantic_retriever],
        weights=[0.4, 0.6] 
    )
    
    return ensemble_retriever