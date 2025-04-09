import random
from jinja2 import Environment, FileSystemLoader

from projectaircraft import config
from projectaircraft.models.airport import Airport


def generate_airports(n: int):

    CITIES = [
        ("CDG", "Charles de Gaulle", "Paris", "France", 49.0097, 2.5479),
        ("JFK", "John F. Kennedy", "New York", "USA", 40.6413, -73.7781),
        ("HND", "Haneda", "Tokyo", "Japan", 35.5494, 139.7798),
        ("DXB", "Dubai International", "Dubai", "UAE", 25.2532, 55.3657),
        ("SIN", "Changi", "Singapore", "Singapore", 1.3644, 103.9915),
        ("LHR", "Heathrow", "London", "UK", 51.4700, -0.4543),
        ("FRA", "Frankfurt", "Frankfurt", "Germany", 50.0379, 8.5622),
    ]

    airports = []
    for i in range(n):
        base = random.choice(CITIES)
        code, name, city, country, latitude, longitude = base
        altitude = random.randint(-2, 100)
        airport = Airport(
            code=f"{code}{i%1000:03}",  # CDG001, CDG002...
            name=f"{name} {i}",
            city=city,
            country=country,
            latitude=latitude,
            longitude=longitude,
            altitude=altitude
        )
        airports.append(airport)
    return airports




def render_airports_to_json(airports, templates, output_file):
    env = Environment(
        loader=FileSystemLoader(searchpath=templates),
        trim_blocks=True,
        lstrip_blocks=True
    )
    template = env.get_template("airports_template.json.j2")
    rendered = template.render(airports=airports)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(rendered)
    print(f"✅ Fichier JSON généré : {output_file}")

if __name__ == "__main__":
    airports = generate_airports(10)
    render_airports_to_json(airports, config.TEMPLATE, config.DATA / "airports.json" )
