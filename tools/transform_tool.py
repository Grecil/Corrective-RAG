from models.LLM import llm
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


def question_rewriter():
    re_write_prompt = PromptTemplate(
        template="""You a question re-writer that converts an input question to a better \n 
        and simpler version that is optimized for vector database retrieval. \n
        Look at the initial question and formulate an improved yet simpler question. \n
        Here is the initial question: \n\n {question}. \nImproved question with no preamble: \n """,
        input_variables=["generation", "question"],
    )
    return re_write_prompt | llm | StrOutputParser()
