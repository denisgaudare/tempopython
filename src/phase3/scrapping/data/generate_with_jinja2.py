import random
from jinja2 import Environment, FileSystemLoader

# Configuration de Jinja2
env = Environment(loader=FileSystemLoader(''))
# Le template est dans le  dossier data
template = env.get_template("flights.template")

# Données simulées
airports = ['CDG', 'JFK', 'LHR', 'FRA', 'AMS', 'DXB', 'MAD', 'ORD', 'LAX', 'SIN']
airlines = ['AF', 'LH', 'BA', 'KL', 'EK', 'IB', 'UA', 'AA', 'SQ', 'DL']

def generate_flights(n=100):
    flights = []
    for _ in range(n):
        airline = random.choice(airlines)
        number = f"{airline}{random.randint(100, 9999)}"
        departure = random.choice(airports)
        arrival = random.choice([a for a in airports if a != departure])
        hour = random.randint(0, 23)
        minute = random.choice([0, 15, 30, 45])
        time = f"{hour:02}:{minute:02}"
        flights.append({
            "number": number,
            "departure": departure,
            "arrival": arrival,
            "time": time
        })
    return flights

# Génération du HTML via le template
flights_data = generate_flights(100)
html_output = template.render(flights=flights_data)

# Écriture dans le fichier
with open("flights_all.html", "w", encoding="utf-8") as f:
    f.write(html_output)

print("Fichier flights.html généré avec Jinja2.")
