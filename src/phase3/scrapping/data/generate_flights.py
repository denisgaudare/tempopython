import random

# Quelques exemples d'aéroports (codes IATA)
airports = ['CDG', 'JFK', 'LHR', 'FRA', 'AMS', 'DXB', 'MAD', 'ORD', 'LAX', 'SIN']
airlines = ['AF', 'LH', 'BA', 'KL', 'EK', 'IB', 'UA', 'AA', 'SQ', 'DL']

def generate_flight_html(n=100):
    html = [
        '<!DOCTYPE html>',
        '<html lang="en">',
        '<head>',
        '    <meta charset="UTF-8">',
        '    <title>Liste des vols</title>',
        '</head>',
        '<body>'
    ]

    for _ in range(n):
        airline = random.choice(airlines)
        flight_number = f"{airline}{random.randint(100, 9999)}"
        departure = random.choice(airports)
        arrival = random.choice([a for a in airports if a != departure])
        hour = random.randint(0, 23)
        minute = random.choice([0, 15, 30, 45])
        time = f"{hour:02}:{minute:02}"

        html.append('    <div class="flight">')
        html.append(f'        <span class="flight-number">{flight_number}</span>')
        html.append(f'        <span class="departure">{departure}</span>')
        html.append(f'        <span class="arrival">{arrival}</span>')
        html.append(f'        <span class="time">{time}</span>')
        html.append('    </div>')

    html.append('</body>')
    html.append('</html>')

    return '\n'.join(html)

# Générer et sauvegarder le fichier
with open("flights.html", "w", encoding="utf-8") as f:
    f.write(generate_flight_html(100))

print("Fichier flights.html généré avec 100 vols.")
