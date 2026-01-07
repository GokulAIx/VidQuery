from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def Split(text, metadata=None):
    # Validate input text
    if not text or not isinstance(text, str) or len(text.strip()) == 0:
        return []
    
    splitt = RecursiveCharacterTextSplitter(chunk_size=4000, chunk_overlap=400)
    doc = Document(page_content=text, metadata=metadata or {})
    splitted = splitt.split_documents([doc])
    return splitted
