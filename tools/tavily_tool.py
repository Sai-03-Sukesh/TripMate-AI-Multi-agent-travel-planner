import os
from tavily import TavilyClient
from dotenv import load_dotenv
load_dotenv()

os.environ['TAVILY_API_KEY'] = os.getenv("TAVILY_API_KEY")

client = TavilyClient()

def tavily_search(query):
    response = client.search(
        query = query,
        max_results = 3
    )

    results = []

    for i, r in enumerate(response["results"], 1):
        title = r.get("title", "Unknown")
        url = r.get("url", "")
        content = r.get('content', "").strip()

        if len(content) > 300:
            content = content[:300].rsplit(" ", 1)[0] + "..."

        results.append(f"{i}. **{title}**\n  {url}\n  {content}")

    return "\n\n".join(results)
