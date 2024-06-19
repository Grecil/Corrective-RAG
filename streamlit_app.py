import streamlit as st
from models.LLM import llm
from tools.index_tool import indexer
from graph import workflow

st.set_page_config(page_title="Assistant", layout="centered")

# st.markdown("""
#     <style>
#         .reportview-container {
#             margin-top: -2em;
#         }
#         #MainMenu {visibility: hidden;}
#         .stDeployButton {display:none;}
#         footer {visibility: hidden;}
#         #stDecoration {display:none;}
#     </style>
# """, unsafe_allow_html=True)


st.markdown(
    "<h1 style='text-align: center; color: white;'>ASSISTANT</h1> <br>",
    unsafe_allow_html=True,
)
indexed = False
uploaded_file = st.file_uploader("Choose a PDF file",type=["pdf"])
if uploaded_file:
    temp_file = f"./{uploaded_file.name}"
    with open(temp_file, "wb") as file:
        file.write(uploaded_file.getvalue())
        file_name = uploaded_file.name
    indexer(temp_file)
    app = workflow.compile()
    indexed = True


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
        s = str(i.page_content).replace("\n", " ")
        if len(s) > 100:
            ans += "\n\n(" + s[:45] + "." * 10 + s[-45:] + ")\n" + str(i.metadata)
        else:
            ans += "\n\n(" + s + ")\n" + str(i.metadata)
    container.info(ans)


with st.form("my_form"):
    text = st.text_area("Enter text:", "How can I help you?")
    submitted = st.form_submit_button("Submit")
    if submitted:
        if indexed:
            generate_rag_response(text)
        else:
            generate_llm_response(text)
