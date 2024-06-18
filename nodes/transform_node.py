from tools.transform_tool import question_rewriter


def transform_query(state):
    question = state["question"]
    documents = state["documents"]
    formatted_docs = "\n\n".join(doc.page_content for doc in documents)
    better_question = question_rewriter.invoke(
        {"question": question, "documents": formatted_docs}
    )
    return {"documents": documents, "question": better_question}
