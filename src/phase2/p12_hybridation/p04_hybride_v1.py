import asyncio
import aiohttp
import json
from multiprocessing import Pool, cpu_count

from phase1.p15_decorateurs.decorators import timeit


def analyse_json(data):
    # Simulation de calcul lourd
    total=0
    for i,d in enumerate(data):
        total += int(d['id'])**2*i
    return {"id": 0, "score": total}

# === Partie I/O (chargement fichiers) ===

async def fetch_json(session, url):
    async with session.get(url) as response:
        return await response.json()

async def download_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_json(session, url) for url in urls]
        return await asyncio.gather(*tasks)

# === Orchestration générale ===

@timeit
def main():
    urls = [
        "https://jsonplaceholder.typicode.com/comments",
        "https://jsonplaceholder.typicode.com/users"
    ] * 100

    # ASYNC
    json_data = asyncio.run(download_all(urls))

    # PROCESS
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(analyse_json, json_data)

    for result in results:
        with open(f"output_{result['id']}.json", "w") as f:
            json.dump(result, f)

if __name__ == "__main__":
    main()
