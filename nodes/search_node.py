from tools.search_tool import web_search_tool
from langchain.schema import Document


def web_search(state):
    question = state["question"]
    documents = state["documents"]
    web_results = str(web_search_tool.run(question))
    web_results = Document(page_content=web_results, metadata={"source": "Web Search"})
    documents.append(web_results)
    return {"documents": documents, "question": question}
