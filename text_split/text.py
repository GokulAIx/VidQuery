from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

def Split(text):
    splitt=RecursiveCharacterTextSplitter(chunk_size=4000,chunk_overlap=400)
    doc = Document(page_content=text)
    splitted=splitt.split_documents([doc])
    return splitted
