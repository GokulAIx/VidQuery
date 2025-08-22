# from langchain_google_genai import ChatGoogleGenerativeAI
# from retrieval.Retrieve import get_retriever
# from prompts.prompt import Final_Prompt
# from text_split.text import Split
# from data.transcripts import Trans
# from database.chromaa import ChromaDB
# from langchain.schema.runnable import RunnableSequence , RunnableLambda
# from dotenv import load_dotenv
# import streamlit as st
# import re


# load_dotenv()
# # P0N6aMczu78

# def set_custom_css():
#     st.markdown("""
#     <style>
#     /* Background for entire app */
#     .stApp {
#         background: linear-gradient(135deg, #1e1e2f 0%, #2b2d42 100%);
#         font-family: 'Poppins', sans-serif;
#         color: #f8f8f2;
#     }

#     /* Fix footer & bottom padding area */
#     .stApp footer, .stApp [data-testid="stStatusWidget"], .stApp [data-testid="stDecoration"] {
#         background: transparent !important;
#         color: #888 !important;
#     }
#     .viewerBadge_link__qRIco, .viewerBadge_container__r5tak, .stApp footer {
#         display: none !important;  /* hides the "Made with Streamlit" footer */
#     }

#     /* Title */
#     h1 {
#         color: #ffb86c !important;
#         text-shadow: 2px 2px 4px #00000055;
#         text-align: center;
#     }

#     /* Input boxes */
#     .stTextInput>div>div>input {
#         border-radius: 12px;
#         border: 2px solid #ff79c6;
#         padding: 8px;
#         background-color: #2e2f4f;
#         color: white;
#     }

#     /* Buttons */
#     button {
#         background-color: #ff5555 !important;
#         color: white !important;
#         border-radius: 12px !important;
#         font-weight: bold !important;
#     }

#     /* Response box */
#     .response-box {
#         background-color: #2e2f4f;
#         border-radius: 15px;
#         padding: 15px;
#         margin-top: 20px;
#         box-shadow: 0 4px 15px rgba(0,0,0,0.3);
#         color: #f8f8f2;
#     }
#     </style>
#     """, unsafe_allow_html=True)


# def main():
#     st.title("RAG App")
#     user_YT=st.text_input("enter the youtube video link ")
#     user_Query=st.text_input("enter your question")

#     match = re.search(r"(?:v=|youtu\.be/|embed/)([a-zA-Z0-9_-]{11})", user_YT)
#     user_YT=match.group(1) if match else None





#     model=ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")
    
#     if user_Query and user_YT:
#         data=Trans(user_YT)
#         split=Split(data)
#         store=ChromaDB(split)
#         # store.add_documents([split])

#         retriever=get_retriever(store)
#         final_retrieved=retriever.get_relevant_documents(user_Query)

#         finale="\n\n".join(i.page_content for i in final_retrieved)

#         prompt=Final_Prompt(finale,user_Query)


#         # chain1=RunnableSequence(data,split,store)
#         # chain2=RunnableSequence(prompt,model)

#         response = model.invoke(prompt)
#         st.write(response.content)

#         st.markdown(f"""
#         <div class="response-box">
#         <h3>📝 Sage Answer</h3>
#         <p>{response.content}</p>
#         </div>
#         """, unsafe_allow_html=True)


# if __name__=="__main__":
#     main()



from langchain_google_genai import ChatGoogleGenerativeAI
from retrieval.Retrieve import get_retriever
from prompts.prompt import Final_Prompt
from text_split.text import Split
from data.transcripts import Trans
from database.chromaa import ChromaDB
from dotenv import load_dotenv
import streamlit as st
import re

load_dotenv()

def set_custom_css():

    st.markdown("""
    <style>
    /* Background for entire app */
    .stApp {
        background: linear-gradient(135deg, #1e1e2f 0%, #2b2d42 100%);
        font-family: 'Poppins', sans-serif;
        color: #f8f8f2;
    }

    /* Fix footer & bottom padding area */
    .stApp footer, .stApp [data-testid="stStatusWidget"], .stApp [data-testid="stDecoration"] {
        background: transparent !important;
        color: #888 !important;
    }
    .viewerBadge_link__qRIco, .viewerBadge_container__r5tak, .stApp footer {
        display: none !important;  /* hides the "Made with Streamlit" footer */
    }

    /* Title */
    h1 {
        color: #ffb86c !important;
        text-shadow: 2px 2px 4px #00000055;
        text-align: center;
    }

    /* Input boxes */
    .stTextInput>div>div>input {
        border-radius: 12px;
        border: 2px solid #ff79c6;
        padding: 8px;
        background-color: #2e2f4f;
        color: white;
    }

    /* Buttons */
    button {
        background-color: #ff5555 !important;
        color: white !important;
        border-radius: 12px !important;
        font-weight: bold !important;
    }

    /* Response box */
    .response-box {
        background-color: #2e2f4f;
        border-radius: 15px;
        padding: 15px;
        margin-top: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        color: #f8f8f2;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Apply CSS theme
    set_custom_css()
    st.image("assets/gokulaix_logo.png", width=40) 
    st.title(" VidQuery ")

    user_YT = st.text_input("🎥 Enter the YouTube video link")
    user_Query = st.text_input("❓ Enter your question")

    match = re.search(r"(?:v=|youtu\\.be/|embed/)([a-zA-Z0-9_-]{11})", user_YT)
    user_YT = match.group(1) if match else None

    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")

    if user_Query and user_YT:
        if st.button("⚡Get Answer⚡"):
            with st.spinner("⚡GokulAIx is summoning transcripts..."):
                data = Trans(user_YT)
                if data ==-1:
                    st.error("🚫 No transcripts are available for this video.")
                    st.stop()
                split = Split(data)
                store = ChromaDB(split)

                retriever = get_retriever(store)
                final_retrieved = retriever.get_relevant_documents(user_Query)

                finale = "\n\n".join(i.page_content for i in final_retrieved)
                prompt = Final_Prompt(finale, user_Query)

                response = model.invoke(prompt)

            st.markdown(f"""
        <div class="response-box">
        <h3>📝 GOAT Answer </h3>
        <p>{response.content}</p>
        </div>
        """, unsafe_allow_html=True)

            st.markdown(
        """
        <div style='text-align: center; padding: 20px; color: #aaa;'>
        ⚡ Powered by <b style="color:#00ffcc;">GokulAIx</b>
        </div>
        """,
        unsafe_allow_html=True
                 )
    

if __name__ == "__main__":
    main()
