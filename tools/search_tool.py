from langchain_community.tools import DuckDuckGoSearchRun


def web_search_tool():
    return DuckDuckGoSearchRun()
