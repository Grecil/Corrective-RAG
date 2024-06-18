def decide_to_generate(state):
    web_search = state["web_search"]
    if web_search == "Yes":
        return "transform_query"
    else:
        return "generate"
