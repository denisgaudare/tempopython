from playwright.sync_api import sync_playwright
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("scraper_playwright")

def scrape_dynamic_flights(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        logger.info(f"Accès à {url}")
        page.goto(url)
        page.wait_for_timeout(3000)  # attendre chargement JS

        flights = page.query_selector_all(".flight")
        data = []
        for f in flights:
            number = f.query_selector(".flight-number").inner_text().strip()
            departure = f.query_selector(".departure").inner_text().strip()
            arrival = f.query_selector(".arrival").inner_text().strip()
            time = f.query_selector(".time").inner_text().strip()
            data.append({
                "number": number,
                "departure": departure,
                "arrival": arrival,
                "time": time
            })

        browser.close()
        logger.info(f"{len(data)} vols récupérés.")
        return pd.DataFrame(data)

if __name__ == "__main__":
    url = "https://example.com/flights"
    df = scrape_dynamic_flights(url)
    df.to_parquet("flights_playwright.parquet", index=False)
    logger.info("Export Parquet terminé.")
