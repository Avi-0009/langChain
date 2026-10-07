import os
import requests

from langchain.tools import tool

@tool
def get_vercel_deployments() -> str:
    """Get the latest Vercel deployments from the user's Vercel account."""

    token = os.getenv("VERCEL_ACCESS_TOKEN")

    if not token:
        return "VERCEL_ACCESS_TOKEN is not configured."

    response = requests.get(
        "https://api.vercel.com/v6/deployments",
        headers={
            "Authorization": f"Bearer {token}"
        },
        params={
            "limit": 5
        },
        timeout=15
    )

    response.raise_for_status()

    data = response.json()

    deployments = []

    for deployment in data.get("deployments", []):
        deployment.append({
            "name": deployment.get("name"),
            "state": deployment.get("state"),
            "url": deployment.get("url"),
            "created": deployment.get("created")
        })

    return str(deployments)