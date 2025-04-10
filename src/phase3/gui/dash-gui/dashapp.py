import dash
from dash import html, dcc, Input, Output
import dash_leaflet as dl
from dash import dash_table
import pandas as pd
import plotly.express as px
from datetime import date

# --- Données internes (pas de fichier externe) ---
airports = pd.DataFrame([
    {"airport_code": "CDG", "airport_name": "Charles de Gaulle", "latitude": 49.0097, "longitude": 2.5479},
    {"airport_code": "JFK", "airport_name": "John F. Kennedy", "latitude": 40.6413, "longitude": -73.7781},
    {"airport_code": "LAX", "airport_name": "Los Angeles", "latitude": 33.9416, "longitude": -118.4085},
])

flights = pd.DataFrame([
    {"flight_id": "AF123", "origin_airport": "CDG", "destination_airport": "JFK", "airline": "Air France",
     "departure_time": pd.Timestamp("2025-04-09 14:00"), "scheduled_arrival_time": pd.Timestamp("2025-04-09 16:30"),
     "arrival_time": pd.Timestamp("2025-04-09 16:50")},
    {"flight_id": "DL456", "origin_airport": "JFK", "destination_airport": "LAX", "airline": "Delta",
     "departure_time": pd.Timestamp("2025-04-09 16:00"), "scheduled_arrival_time": pd.Timestamp("2025-04-09 19:00"),
     "arrival_time": pd.Timestamp("2025-04-09 19:05")},
    {"flight_id": "AF789", "origin_airport": "CDG", "destination_airport": "LAX", "airline": "Air France",
     "departure_time": pd.Timestamp("2025-04-09 10:00"), "scheduled_arrival_time": pd.Timestamp("2025-04-09 13:00"),
     "arrival_time": pd.Timestamp("2025-04-09 12:55")},
])

flights["departure_day"] = flights["departure_time"].dt.date
flights["arrival_delay"] = (flights["arrival_time"] - flights["scheduled_arrival_time"]).dt.total_seconds() / 60

# --- Application Dash ---
app = dash.Dash(__name__)
app.title = "Mini Dash Flights App"

app.layout = html.Div([
    html.H1("✈️ Mini Dash App - Flights Overview", style={"textAlign": "center"}),

    html.Div([
        html.Label("📅 Choisissez une date"),
        dcc.DatePickerSingle(
            id="date-picker",
            date=flights["departure_day"].min(),
            display_format="YYYY-MM-DD"
        ),
        html.Label("🛫 Compagnie aérienne"),
        dcc.Dropdown(
            id="airline-dropdown",
            options=[{"label": a, "value": a} for a in sorted(flights["airline"].unique())],
            value="Air France"
        ),
    ], style={"width": "30%", "float": "left", "padding": "2rem"}),

    html.Div([
        dcc.Graph(id="delay-graph"),
        dash_table.DataTable(
            id="flights-table",
            columns=[{"name": col, "id": col} for col in flights.columns],
            page_size=5,
            style_table={"overflowX": "auto"},
        ),
        html.H4("🗺️ Carte des aéroports de départ"),
        dl.Map(id="airport-map", center=[45, 2], zoom=2, style={"width": "100%", "height": "400px"}),
    ], style={"marginLeft": "35%", "padding": "1rem"}),
])


@app.callback(
    Output("delay-graph", "figure"),
    Output("flights-table", "data"),
    Output("airport-map", "children"),
    Input("date-picker", "date"),
    Input("airline-dropdown", "value"),
)
def update_dashboard(selected_date, selected_airline):
    selected_date = pd.to_datetime(selected_date).date()
    df = flights[(flights["departure_day"] == selected_date) & (flights["airline"] == selected_airline)]

    # Histogramme des retards
    fig = px.histogram(df, x=df["departure_time"].dt.hour,
                       title=f"Départs horaires - {selected_airline}",
                       labels={"x": "Heure", "count": "Nombre de vols"})

    # Données du tableau
    table_data = df.to_dict("records")

    # Carte des aéroports d’origine
    merged = pd.merge(df[["origin_airport"]].drop_duplicates(), airports,
                      left_on="origin_airport", right_on="airport_code", how="left")
    markers = [
        dl.Marker(position=(row["latitude"], row["longitude"]),
                  children=dl.Tooltip(f"{row['airport_name']} ({row['airport_code']})"))
        for _, row in merged.iterrows()
    ]
    map_tiles = dl.TileLayer(url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png")
    leaflet_map = [map_tiles] + markers

    return fig, table_data, leaflet_map


if __name__ == "__main__":
    app.run(debug=True)
