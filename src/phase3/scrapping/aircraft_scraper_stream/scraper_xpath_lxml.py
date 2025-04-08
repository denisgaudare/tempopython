import requests
from lxml import html
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("scraper_xpath")

def scrape_with_xpath(url):
    logger.info(f"Fetching {url}")
    response = requests.get(url)
    tree = html.fromstring(response.content)

    flights = []
    for flight in tree.xpath('//div[@class="flight"]'):
        number = flight.xpath('.//span[@class="flight-number"]/text()')[0].strip()
        departure = flight.xpath('.//span[@class="departure"]/text()')[0].strip()
        arrival = flight.xpath('.//span[@class="arrival"]/text()')[0].strip()
        time = flight.xpath('.//span[@class="time"]/text()')[0].strip()
        flights.append({
            "number": number,
            "departure": departure,
            "arrival": arrival,
            "time": time
        })

    logger.info(f"{len(flights)} vols trouvés.")
    return pd.DataFrame(flights)

if __name__ == "__main__":
    url = "https://example.com/flights-today"
    df = scrape_with_xpath(url)
    df.to_csv("flights_xpath.csv", index=False)
    logger.info("Export CSV terminé.")
