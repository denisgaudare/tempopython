import asyncio
import time

import requests

# 🎯 Un tuple avec 5 URLs différentes
URLS = [
        "https://www.cnn.com",
        "https://www.pypy.org",
        "https://fr.wikipedia.org/wiki/Dune_(roman)",
        "https://www.allocine.fr/film/fichefilm_gen_cfilm=249.html"
    ] * 100


# 🧱 Fonction bloquante classique avec requests
def fetch_url(url):
    print(f"📡 Downloading: {url}")
    response = requests.get(url, timeout=10)
    print(f"✅ Done: {url} with status {response.status_code}")
    return url, response.status_code


# 🌐 Fonction async qui délègue à un thread
async def async_fetch_url(url):
    return await asyncio.to_thread(fetch_url, url)


# 🚀 Fonction principale
async def main():
    start = time.perf_counter()
    tasks = [async_fetch_url(url) for url in URLS]
    results = await asyncio.gather(*tasks)

    print("\n📊 Résultats :")
    for url, status in results:
        print(f"- {url} → HTTP {status}")
    duree = time.perf_counter() - start
    print(f"Duree {duree}")

# 🏁 Démarrer l'application
if __name__ == "__main__":
    asyncio.run(main())
    print("Fin test Asyncio Downloads")
