import requests
from datetime import datetime, timedelta
from config import USGS_API_URL, ETHIOPIA_BOUNDS


def fetch_earthquake_data():
    try:
        params = {
            "format": "geojson",
            "starttime": (datetime.utcnow() - timedelta(days=1)).isoformat(),
            "endtime": datetime.utcnow().isoformat(),
            **ETHIOPIA_BOUNDS,
            "orderby": "time-asc"
        }
        full_url = requests.Request("GET", USGS_API_URL, params=params).prepare().url
        response = requests.get(full_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching earthquake data: {e}")
        return None
