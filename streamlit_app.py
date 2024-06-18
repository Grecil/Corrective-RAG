import streamlit as st
from graph import app
from models.LLM import llm

st.set_page_config(page_title="Assistant", layout="centered")

st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)


st.markdown(
    "<h1 style='text-align: center; color: white;'>ASSISTANT</h1> <br>",
    unsafe_allow_html=True,
)

on = st.toggle("Get Context from Files")


def generate_llm_response(input_text):
    ans = ""
    container = st.empty()
    for token in llm.stream(input_text):
        ans += token.content
        container.info(ans)


def generate_rag_response(input_text):
    ans = ""
    input_dict = {"question": str(input_text)}
    container = st.empty()
    response = app.invoke(input_dict)
    arr = []
    for token in response["generation"]:
        ans += token
        arr.append(token)
        container.info(ans)
    ans += "\n\nSources - "
    for i in response["documents"]:
        s = i.page_content
        if len(s) > 110:
            ans += "\n\n" + s[:40] + "." * 10 + s[-40:] + " " + str(i.metadata)
        else:
            ans += "\n\n" + s + " " + str(i.metadata)
    container.info(ans)


with st.form("my_form"):
    text = st.text_area("Enter text:", "How can I help you?")
    submitted = st.form_submit_button("Submit")
    if submitted:
        if on:
            generate_rag_response(text)
        else:
            generate_llm_response(text)
