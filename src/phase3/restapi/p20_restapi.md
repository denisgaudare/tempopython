**Enrichissement avec une API REST météo** 
Cela permet d’aborder des notions très concrètes, 
avec un gros potentiel pédagogique :

- Appels HTTP (`requests`, `aiohttp`)
- Gestion de données asynchrones (optionnel)
- Structuration et validation des données (ex: `pydantic`)
- Enrichissement croisé entre deux sources (flights + météo)
- Analyse d’impact sur les retards
- (bonus) Caching local pour éviter trop d’appels

---

## 💡 Objectif pédagogique du projet

**Titre du projet** : *Flight Weather Enrichment & Delay Analysis*

> Enrichir les données de vols (`flights.csv`) avec des conditions météo extraites via API pour chaque aéroport de départ à la date et l’heure du vol, puis analyser l’impact de la météo sur les retards.

---

## 📂 Structure du projet

```
flight-weather-project/
│
├── data/
│   ├── flights.csv
│   ├── airports.csv
│   └── weather_cache.json  ← stockage local des requêtes
│
├── src/
│   ├── fetch_weather.py    ← fonctions d’appel API
│   ├── enrich.py           ← logique d’enrichissement
│   ├── analyze.py          ← impact météo sur les retards
│   └── models.py           ← dataclasses ou pydantic
│
├── notebooks/
│   └── impact_analysis.ipynb
│
├── requirements.txt
└── README.md
```

---

## 🔄 Pipeline de traitement

1. **Extraction des vols** (`flights.csv`)
   - Colonnes : `flight_id`, `departure_airport`, `departure_time`, `delay_minutes`

2. **Récupération de la météo** via API REST
   - Pour chaque `(departure_airport, departure_time)`
   - Exemple d’API : `https://api.weatherapi.com/v1/history.json?q=CDG&dt=2024-12-01`
   - À configurer avec clé API

3. **Enrichissement** :
   - Ajouter à chaque vol : `temperature`, `precip_mm`, `wind_kph`, `condition`

4. **Analyse de l’impact** :
   - Corrélation entre conditions météo (ex : pluie, vent) et retards
   - Visualisations (scatter plot, boxplot par condition météo)

---

## 🔧 API météo proposée (exemple)

Tu peux utiliser une vraie API comme :

- [WeatherAPI.com](https://www.weatherapi.com/)
- [Open-Meteo](https://open-meteo.com/)
- [Visual Crossing Weather](https://www.visualcrossing.com/weather-data-editions)

Ou bien **mock une API** avec FastAPI localement pour éviter les limites d’usage.

---

## 📜 Exemple de code (extrait simplifié)

### `fetch_weather.py`

```python
import requests
import json
from pathlib import Path

API_KEY = "YOUR_API_KEY"
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

    url = f"https://api.weatherapi.com/v1/history.json"
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
```

---

### `enrich.py`

```python
import pandas as pd
from fetch_weather import get_weather

flights = pd.read_csv("data/flights.csv")
flights["departure_date"] = pd.to_datetime(flights["departure_time"]).dt.date

def enrich_flight(row):
    weather = get_weather(row["departure_airport"], str(row["departure_date"]))
    return pd.Series(weather)

weather_data = flights.apply(enrich_flight, axis=1)
enriched = pd.concat([flights, weather_data], axis=1)
enriched.to_csv("data/flights_enriched.csv", index=False)
```

---

## 📊 Analyse possible

### Questions à poser aux étudiants :

- Les vols sous **pluie** sont-ils plus souvent en retard ?
- Le **vent fort** augmente-t-il le temps d’arrivée moyen ?
- Quelles sont les **conditions météo associées aux plus grands retards** ?

---

## 📈 Graphique attendu (exemple)

- Boxplot des retards par `condition` météo
- Nuage de points `wind_kph` vs `delay_minutes`
- Histogramme du retard moyen par `precip_mm` binned

---

## 🧪 Variante Bonus : asynchrone

Refaire le code `get_weather` avec `aiohttp` et `asyncio.gather` pour paralléliser les appels API.

---

Souhaites-tu que je te prépare un **repo Git complet** ou un **notebook Jupyter** prêt à l’emploi avec des données mockées et un exemple d’analyse ?