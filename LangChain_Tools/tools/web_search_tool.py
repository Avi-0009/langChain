import os

from langchain.tools import tool
from langchain_tavily import TavilySearch
from langchain_community.tools import DuckDuckGoSearchResults

@tool
def web_search(query: str) -> str:
    """Search the web for current events, facts, or general knowledge."""

    if os.getenv("TAVILY_API_KEY"):
        try:
            tavily = TavilySearch(
                max_results=3, 
                search_depth="basic"
            )

            return str(
                tavily.invoke({
                    "query": query
                })
            )
        except Exception as e:
            print(f"Tavily search failed: {e}")

    try:
        ddg = DuckDuckGoSearchResults(max_results=3)
        return str(
            ddg.invoke({
                "query":query
            })
        )
    except Exception as e:
        return (
            f"Error: Both Tavily and DuckDuckGo searches failed. "
            f"({e})"
        )