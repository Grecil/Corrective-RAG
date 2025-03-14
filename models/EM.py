from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
import streamlit as st

embedding = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-exp-03-07", google_api_key=st.secrets["GEMINI-API-KEY"]
)
