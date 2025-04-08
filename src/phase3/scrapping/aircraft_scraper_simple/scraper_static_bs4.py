import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging

# Logger setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("scraper_static")

def scrape_static_flights(url):
    logger.info(f"Fetching {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    flights = []
    for flight in soup.select(".flight"):
        flights.append({
            "number": flight.select_one(".flight-number").text.strip(),
            "departure": flight.select_one(".departure").text.strip(),
            "arrival": flight.select_one(".arrival").text.strip(),
            "time": flight.select_one(".time").text.strip()
        })

    logger.info(f"{len(flights)} vols trouvés.")
    return pd.DataFrame(flights)

if __name__ == "__main__":
    url = "http://localhost:88/../flights_all.html"
    df = scrape_static_flights(url)
    df.to_csv("../output/flights_bs4.csv", index=False)
    logger.info("Export CSV terminé.")
