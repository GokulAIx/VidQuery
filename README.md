# VidQuery - Ask Any Question From a YouTube Video!

A lightweight Streamlit app that allows users to ask questions about a YouTube video and get answers using the video's transcript. This is a Retrieval-Augmented Generation (RAG) based application leveraging embeddings for semantic search and natural language understanding.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-red?logo=streamlit)

---

## 1. How It Works / Model Overview

- **Input:** YouTube video link + User query  
- **Processing:** 
  - Video transcript is fetched and split into chunks
  - Chunks are embedded using `sentence-transformers/all-MiniLM-L6-v2`
  - Semantic search performed using Chroma vector store
- **Output:** Answer to the user query using the video transcript  

---

## 2. App Features

- Input a YouTube video link
- Ask any question related to the video
- Get a concise answer using the video's transcript
- Powered by RAG and embeddings for accurate results

---

## 3. Example Inputs

- **YouTube Link:** `https://www.youtube.com/watch?v=P0N6aMczu78`  
- **Question:** "Who was Admiral Richard Byrd Jr and what did he discover in Antarctica?"  
- **Output:** Relevant answer extracted from the transcript

---

## 4. Project Structure


---


---

## 5. How to Run Locally
# 1. First, fork this repository to your own GitHub account
# 2. Clone the repository:


```bash
git clone https://github.com/<your-username>/VidQuery.git
cd rag_app
pip install -r requirements.txt
streamlit run app.py
```


## 10. Contact Info

- **Name:** P Gokul Sree Chandra  
- **Email:** polavarapugokul@gmail.com  
- **LinkedIn:** [Gokul Sree Chandra](https://www.linkedin.com/in/gokulsreechandra/)  
- **Portfolio:** [GokulAIx](https://soft-truffle-eada3e.netlify.app/)

## 11. License
# This project is licensed under the [MIT License](LICENSE).
