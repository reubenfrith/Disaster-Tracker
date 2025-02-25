

# Fetch earthquake data from USGS
import requests
from datetime import datetime

def fetch_earthquake_data():
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "geojson",
        "limit": 5,
        "minmagnitude": 4.0
    }
    response = requests.get(url, params=params)
    data = response.json()["features"]
    
    events = []
    for quake in data:
        event = {
            "id": quake["id"],
            "type": "earthquake",
            "location": quake["geometry"],
            "severity": "Moderate" if quake["properties"]["mag"] < 5 else "Severe",
            "timestamp": datetime.utcfromtimestamp(quake["properties"]["time"] / 1000).isoformat()
        }
        events.append(event)
    
    return events