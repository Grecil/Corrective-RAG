from langgraph.graph import END, StateGraph
from typing_extensions import TypedDict
from typing import List
from nodes.transform_node import transform_query
from nodes.retrieve_node import retrieve
from nodes.search_node import web_search
from nodes.grade_node import grade_documents
from nodes.generate_node import generate
from nodes.decision_node import decide_to_generate


def app():
    class GraphState(TypedDict):
        question: str
        generation: str
        web_search: str
        documents: List[str]

    workflow = StateGraph(GraphState)

    workflow.add_node("retrieve", retrieve)
    workflow.add_node("grade_documents", grade_documents)
    workflow.add_node("generate", generate)
    workflow.add_node("transform_query", transform_query)
    workflow.add_node("web_search_node", web_search)

    workflow.set_entry_point("retrieve")
    workflow.add_edge("retrieve", "grade_documents")
    workflow.add_conditional_edges(
        "grade_documents",
        decide_to_generate,
        {
            "transform_query": "transform_query",
            "generate": "generate",
        },
    )
    workflow.add_edge("transform_query", "web_search_node")
    workflow.add_edge("web_search_node", "generate")
    workflow.add_edge("generate", END)
    return workflow.compile()
