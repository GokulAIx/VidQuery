from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.retrievers.multi_query import MultiQueryRetriever
import os 

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def get_retriever(n):
    retriever = n.as_retriever(search_kwargs={"k": 3})
    return retriever

def get_multi_query_retriever(vectorstore):

    llm_for_queries = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", google_api_key=os.getenv("GOOGLE_API_KEY"))


    retriever_base = vectorstore.as_retriever()


    multi_query_retriever = MultiQueryRetriever.from_llm(
        retriever=retriever_base,
        llm=llm_for_queries,
        include_original=True # This ensures the original query is also used
    )
    return multi_query_retriever