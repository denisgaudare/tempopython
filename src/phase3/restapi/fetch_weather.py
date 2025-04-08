import requests
import json
from pathlib import Path

API_KEY = "ca0d9d47d08248b2804151113252403"
CACHE_FILE = Path("data/weather_cache.json")

def load_cache():
    return json.loads(CACHE_FILE.read_text()) if CACHE_FILE.exists() else {}

def save_cache(cache):
    CACHE_FILE.write_text(json.dumps(cache, indent=2))

def get_weather(airport_code, date):
    cache = load_cache()
    key = f"{airport_code}_{date}"
    if key in cache:
        return cache[key]

    #url = "https://api.weatherapi.com/v1/history.json"
    url = "https://api.weatherapi.com/v1/forecast.json"
    params = {"key": API_KEY, "q": airport_code, "dt": date}
    r = requests.get(url, params=params)
    data = r.json()

    weather = {
        "temperature": data["forecast"]["forecastday"][0]["day"]["avgtemp_c"],
        "precip_mm": data["forecast"]["forecastday"][0]["day"]["totalprecip_mm"],
        "condition": data["forecast"]["forecastday"][0]["day"]["condition"]["text"],
        "wind_kph": data["forecast"]["forecastday"][0]["day"]["maxwind_kph"],
    }

    cache[key] = weather
    save_cache(cache)
    return weather
