import requests

from langchain.tools import tool

@tool
def get_weather(latitude:float, longitude:float) -> str:
    """Get the current weather for a latitude and longitude."""

    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,wind_speed_10m"
        },
        timeout=15
    )

    if response.status_code != 200:
        return f"Error: Could not retrieve weather (Status Code {response.status_code})."

    data = response.json()

    current = data.get("current", {})
    units = data.get("current_units", {})

    return str({
        "temperature": f"{current.get("temperature_2m")}{units.get("temperature_2m", "")}",
        "wind_speed": f"{current.get("wind_speed_10m")} {units.get("wind_speed_10m", "")}"
    })