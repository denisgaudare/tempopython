import json
from pathlib import Path

from phase3.gui.exercice.models.airport import Airport


def generate_map_html(airports: list[Airport], output_path: str = "ui/airports_map.html"):
    markers = [
        {
            "code": a.airport_code,
            "name": a.airport_name,
            "lat": a.latitude,
            "lon": a.longitude
        }
        for a in airports
    ]

    # HTML basique avec Leaflet
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <title>Carte des aéroports</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css"/>
        <style>
            html, body, #map {{ height: 100%; margin: 0; }}
        </style>
    </head>
    <body>
        <div id="map"></div>
        <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
        <script>
            const map = L.map('map').setView([48.8566, 2.3522], 4);
            L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png').addTo(map);

            const airports = {{json.dumps(markers)}};
            airports.forEach(a => {{
                const marker = L.marker([a.lat, a.lon]).addTo(map)
                    .bindPopup(`<b>${{a.name}}</b><br>Code: <a href="#" onclick="window.location.href='filter://' + a.code">${{a.code}}</a>`);
            }});
        </script>
    </body>
    </html>
    """
    mymap = Path(output_path).absolute()
    mymap.write_text(html, encoding='utf-8')
    return mymap
