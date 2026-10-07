import os
import requests
from langchain.tools import tool

@tool
def get_github_repo(owner: str, repo: str) -> str:
    """Get information about a public GitHub repository."""

    # Standard headers required by GitHub
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"    

    response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}",
        headers=headers,
        timeout=15
    )

    if response.status_code != 200:
        return f"Error: Could not retrieve Repository (Status Code {response.raise_for_status}). Please verify the owner and repo name."

    data = response.json()

    return str({
        "name": data.get("full_name"),
        "description": data.get("description"),
        "stars" : data.get("stargazers_count"), 
        "language" : data.get("language"),
        "url": data.get("html_url")
    })