On entre dans le domaine du **web scraping HTML**, 
très utile pour collecter automatiquement des données non disponibles via API — par exemple : horaires de vols, prix de billets, infos compagnies, etc.

---

## 🧰 Les librairies Python les plus utilisées pour le scraping

| Librairie | Type | Points forts | Cas d’usage |
|----------|------|---------------|-------------|
| **`requests`** | HTTP | Simple pour récupérer les pages | Téléchargement HTML brut |
| **`BeautifulSoup`** (`bs4`) | Parsing | Ultra lisible, parsing HTML/XML | Extraire du contenu balisé |
| **`lxml`** | Parsing (rapide) | Très rapide, support XPath | Structure complexe |
| **`Selenium`** | Navigateur headless | Pour les pages JS, simulateur humain | Scraper des sites dynamiques |
| **`Playwright`** | Navigateur moderne | Alternative + rapide à Selenium | JS lourd, interactions complexes |
| **`Scrapy`** | Framework complet | Scraping massif, pipeline intégré | Projets structurés / crawl en masse |

---

## ✈️ Exemple simple (horaires de vols, BeautifulSoup)

Imaginons qu’on scrape une page HTML qui contient ça :

```html
<div class="flight">
  <span class="flight-number">AF123</span>
  <span class="departure">CDG</span>
  <span class="arrival">JFK</span>
  <span class="time">10:45</span>
</div>
```

### 📜 Code avec `requests` + `BeautifulSoup`

```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com/flights-today"
response = requests.get(url)
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
```

---

## 🔄 Comparaison rapide des outils

| Outil | Simplicité | JS Support | Performance | Idéal pour |
|-------|------------|------------|-------------|-------------|
| `requests + bs4` | ⭐⭐⭐⭐⭐ | ❌ | ✅✅✅ | HTML statique |
| `lxml` | ⭐⭐⭐ | ❌ | ✅✅✅✅ | HTML structuré, XPath |
| `Selenium` | ⭐⭐ | ✅✅✅ | ❌❌ | Sites interactifs JS |
| `Playwright` | ⭐⭐⭐ | ✅✅✅✅ | ✅✅✅ | Scraping JS moderne |
| `Scrapy` | ⭐⭐ (setup) | 🔸 (via middlewares) | ✅✅✅✅✅ | Crawling massif et structuré |

---

## 🚀 Exemple plus avancé avec `Playwright`

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://example.com/flights")

    flights = page.query_selector_all(".flight")
    for f in flights:
        print(f.inner_text())

    browser.close()
```

> 👉 **Playwright** est très utile si le site charge les données **en JS après chargement**.

---

https://scrapeops.io/python-web-scraping-playbook/python-requests-beautifulsoup-beginners-guide/
