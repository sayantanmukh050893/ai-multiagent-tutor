from crewai_tools import tool
from duckduckgo_search import DDGS

@tool("Search YouTube Videos")
def search_youtube(topic: str) -> str:
    """
    Searches YouTube for top 5 videos related to topic.
    """
    results = []
    
    with DDGS() as ddgs:
        query = f"{topic} site:youtube.com"
        for r in ddgs.text(query, max_results=5):
            results.append(f"Title: {r['title']}\nURL: {r['href']}\n")

    return "\n\n".join(results)
