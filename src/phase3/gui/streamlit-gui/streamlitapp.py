from pathlib import Path

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")
st.title("✈️ Flights & Airports - Visualisation des retards")

# --- Chargement des données ---
@st.cache_data
def load_data():
    p = Path("..")
    flights = pd.read_csv(p / "flights.csv", parse_dates=["departure_time", "scheduled_arrival_time", "arrival_time"])
    airports = pd.read_csv(p / "airports.csv")
    return flights, airports

flights, airports = load_data()

# --- Calcul des retards (en minutes) ---
flights["arrival_delay"] = (flights["arrival_time"] - flights["scheduled_arrival_time"]).dt.total_seconds() / 60

# --- Interface de filtre ---
st.sidebar.header("Filtres")
selected_day = st.sidebar.date_input("Date")

# --- Filtrage ---
df = flights[flights["departure_time"].dt.date == selected_day]

st.subheader("Vols du jour sélectionné")
st.dataframe(df)

# --- Calcul du retard moyen par aéroport d’origine ---
delay_by_origin = df.groupby("origin_airport")["arrival_delay"].mean().reset_index()
delay_by_origin.columns = ["airport_code", "mean_delay"]

# --- Fusion avec les coordonnées ---
merged = pd.merge(delay_by_origin, airports, on="airport_code", how="left").dropna(subset=["latitude", "longitude"])

# --- Carte Folium ---
st.subheader("Carte des aéroports (retards moyens à l'arrivée)")

m = folium.Map(location=[47, 2], zoom_start=4, tiles="CartoDB positron")

for _, row in merged.iterrows():
    color = "green" if row["mean_delay"] < 5 else "orange" if row["mean_delay"] < 15 else "red"
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=6,
        popup=f"{row['airport_name']} ({row['airport_code']})<br>Retard moyen : {row['mean_delay']:.1f} min",
        color=color,
        fill=True,
        fill_opacity=0.7,
    ).add_to(m)

st_data = st_folium(m, width=1200, height=500)
