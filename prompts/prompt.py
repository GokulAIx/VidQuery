from langchain_core.prompts import PromptTemplate

def Template():
    temp = PromptTemplate(
        template="""
you are a helpful Youtube Video question answering assistant. The user asks a question related to the video and you will get the relevant contextual chunks of that video. Answer ONLY from the given context. If the context is not sufficient, just say: need more data to answer your query, Master.

question: {question}
CONTEXT: {context}
""",
        input_variables=["context", "question"]
    )
    return temp

def Final_Prompt(retrieved, query):
    final_prompt = Template()
    # Pass a single dictionary to invoke
    finale = final_prompt.invoke({"context": retrieved, "question": query})
    return finale
