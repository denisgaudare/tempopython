# Flight Weather Enrichment & Delay Analysis

## Objectif
Enrichir les données de vols (`flights.csv`) avec des conditions météo extraites via une API REST, puis analyser l’impact de la météo sur les retards.

## Structure du projet

```
flight-weather-project/
│
├── data/
│   ├── flights.csv
│   ├── airports.csv
│   └── weather_cache.json  ← stockage local des requêtes
│
├── src/
│   ├── fetch_weather.py
│   ├── enrich.py
│   ├── analyze.py
│   └── models.py
│
├── notebooks/
│   └── impact_analysis.ipynb
│
├── requirements.txt
└── README.md
```

## Étapes principales

1. Extraction des vols depuis `flights.csv`
2. Récupération météo via API (`fetch_weather.py`)
3. Enrichissement des données (`enrich.py`)
4. Analyse d’impact (`analyze.py`, `impact_analysis.ipynb`)

## API météo
Utilise [https://www.weatherapi.com/](https://www.weatherapi.com/) (ou toute autre API météo REST).

## Lancer l'enrichissement

```bash
pip install -r requirements.txt
python src/enrich.py
```
