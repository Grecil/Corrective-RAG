from tools.generate_tool import rag_chain


def generate(state):
    question = state["question"]
    documents = state["documents"]

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    generation = rag_chain.stream(
        {"context": format_docs(documents), "question": question}
    )
    return {"context": documents, "question": question, "generation": generation}
