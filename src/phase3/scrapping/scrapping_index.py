import os

import requests
from bs4 import BeautifulSoup
import pathlib
from src.phase3.scrapping.localfileadapter import LocalFileAdapter

absol = os.path.abspath("index.html")
url = pathlib.Path(absol).as_uri()

s = requests.Session()
s.mount('file://', LocalFileAdapter())

response = s.request(method="GET", url=url)
soup = BeautifulSoup(response.text, "html.parser")

flights = []

for flight in soup.select(".flight"):
    number = flight.select_one(".flight-number").text.strip()
    departure = flight.select_one(".departure").text.strip()
    arrival = flight.select_one(".arrival").text.strip()
    time = flight.select_one(".time").text.strip()

    flights.append({
        "number": number,
        "departure": departure,
        "arrival": arrival,
        "time": time
    })

print(flights)