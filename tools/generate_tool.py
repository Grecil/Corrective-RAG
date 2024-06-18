from models.LLM import llm
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate(
    template="""You are an assistant for question-answering tasks. \n
                Use the following pieces of retrieved context and your knowledge to answer the question. \n
                If you don't know the answer, just say that you don't know. \n
                Question: {question} 
                Context: {context} 
                Answer:""",
    input_variables=["generation", "question", "context"],
)

rag_chain = prompt | llm | StrOutputParser()
