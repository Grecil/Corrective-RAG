from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.faiss import FAISS
from langchain_community.document_loaders import PyPDFLoader
from models.EM import embedding


def indexer(file):
    docs = PyPDFLoader(file).load()
    splits = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=1024, chunk_overlap=128
    ).split_documents(docs)
    vectorstore = FAISS.from_documents(splits, embedding)
    vectorstore.save_local("index")
