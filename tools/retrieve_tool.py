from langchain_community.vectorstores import FAISS
from models.EM import embedding

vectorstore = FAISS.load_local(
    folder_path="index", embeddings=embedding, allow_dangerous_deserialization=True
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
