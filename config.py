from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
USGS_API_URL = os.getenv("USGS_API_URL")
ETHIOPIA_BOUNDS = {
    "minlatitude": float(os.getenv("ETHIOPIA_BOUNDS_MINLAT", 3.5)),
    "maxlatitude": float(os.getenv("ETHIOPIA_BOUNDS_MAXLAT", 15.5)),
    "minlongitude": float(os.getenv("ETHIOPIA_BOUNDS_MINLON", 33.0)),
    "maxlongitude": float(os.getenv("ETHIOPIA_BOUNDS_MAXLON", 48.0)),
}
