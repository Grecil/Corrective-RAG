from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
import streamlit as st

embedding = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004", google_api_key=st.secrets["GEMINI-API-KEY"]
)
