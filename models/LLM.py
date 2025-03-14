from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
import streamlit as st

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp", google_api_key=st.secrets["GEMINI-API-KEY"]
)
