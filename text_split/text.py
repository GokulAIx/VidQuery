from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

def Split(text):
    splitt=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
    doc = Document(page_content=text)
    splitted=splitt.split_documents([doc])
    return splitted