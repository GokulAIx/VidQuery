from langchain_google_genai import ChatGoogleGenerativeAI
from retrieval.Retrieve import get_retriever
from prompts.prompt import Final_Prompt
from text_split.text import Split
from data.transcripts import Trans
from database.chromaa import ChromaDB
from dotenv import load_dotenv
import streamlit as st
import re
import os
load_dotenv()
def set_custom_css():
    st.markdown("""
    <style>
    .stApp {background: linear-gradient(135deg, #1e1e2f 0%, #2b2d42 100%); color: #f8f8f2; font-family: 'Poppins', sans-serif;}
    .stApp footer, .stApp [data-testid="stStatusWidget"], .stApp [data-testid="stDecoration"] {background: transparent !important; color: #888 !important;}
    .viewerBadge_link__qRIco, .viewerBadge_container__r5tak, .stApp footer {display: none !important;}
    h1 {color: #ffb86c !important; text-shadow: 2px 2px 4px #00000055; text-align: center;}
    .stTextInput>div>div>input {border-radius: 12px; border: 2px solid #ff79c6; padding: 8px; background-color: #2e2f4f; color: white;}
    button {background-color: #ff5555 !important; color: white !important; border-radius: 12px !important; font-weight: bold !important;}
    .response-box {background-color: #2e2f4f; border-radius: 15px; padding: 15px; margin-top: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); color: #f8f8f2;}
    </style>
    """, unsafe_allow_html=True)


def main():
    set_custom_css()
    st.image("assets/gokulaix_logo.png", width=40)
    st.title("VidQuery")

    with st.form(key="query_form"):
        user_YT = st.text_input("🎥 Enter the YouTube video link")
        user_Query = st.text_input("❓ Enter your question")
        submit_button = st.form_submit_button(label="⚡ Get Answer ⚡")


    match = re.search(r"(?:v=|youtu\.be/|embed/)([a-zA-Z0-9_-]{11})", user_YT)
    user_YT = match.group(1) if match else None

    if submit_button:
        if not user_YT or not user_Query:
            st.warning("Please enter a valid YouTube link and a question.")
            return

        with st.spinner("⚡ GokulAIx is fetching transcripts..."):
            api_key = os.getenv("GOOGLE_API_KEY") 
            if not api_key:
                st.error("API key not found. Please set GOOGLE_API_KEY in your Streamlit secrets.")
                return
            model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", google_api_key=api_key)
            import requests
            try:
                response = requests.get(f"https://vidquery-backend-8t04.onrender.com/transcript/{user_YT}")
                data = response.text
                
                if not data:
                    st.error("🚫 No transcripts are available for this video.")
                    return
            except Exception as e:
                st.error(f"Error fetching transcript: {e}")
                return

            split = Split(data)
            
            # --- Move the hot-swap code here ---
            import sys
            __import__('pysqlite3')
            sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
            # ------------------------------------

            store = ChromaDB(split)

            retriever = get_retriever(store)
            final_retrieved = retriever.get_relevant_documents(user_Query)

            if not final_retrieved:
                st.info("No relevant information found in this video.")
                return

            finale = "\n\n".join(i.page_content for i in final_retrieved)
            prompt = Final_Prompt(finale, user_Query)

            response = model.invoke(prompt)

        st.markdown(f"""
        <div class="response-box">
        <h3>📝 GOAT Answer</h3>
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