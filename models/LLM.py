from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
import streamlit as st

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", google_api_key=st.secrets["GEMINI-API-KEY"]
)
