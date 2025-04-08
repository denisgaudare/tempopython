# Tirer parti à la fois du **CPU** et de l’**I/O** efficacement en Python !
## Combiner **multiprocessing** (pour le calcul) et **asyncio** (pour les I/O). 

### 🧠 Stratégie générale :

- **Parties CPU-intensives** → utilisent plusieurs **processus** (`multiprocessing`)
- **Parties I/O-intensives** (ex : requêtes web, lecture fichiers réseau) → utilisent **asyncio**

---

### ✅ Exemple concret :

Imaginons un script qui :
1. Charge des fichiers JSON distants (I/O)
2. Fait un gros traitement mathématique sur chaque (CPU)
3. Sauvegarde les résultats (I/O)

---

### 📦 Code hybride `asyncio` + `multiprocessing`

```python
import asyncio
import aiohttp
import json
from multiprocessing import Pool, cpu_count

# === Partie CPU (calcul intensif) ===

def analyse_json(data):
    # Simulation de calcul lourd
    total = sum(x**2 for x in data["values"])
    return {"id": data["id"], "score": total}

# === Partie I/O (chargement fichiers) ===

async def fetch_json(session, url):
    async with session.get(url) as response:
        return await response.json()

async def download_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_json(session, url) for url in urls]
        return await asyncio.gather(*tasks)

# === Orchestration générale ===

def main():
    urls = [
        "https://example.com/file1.json",
        "https://example.com/file2.json",
        "https://example.com/file3.json",
    ]

    # Étape 1 : Download des fichiers en parallèle (I/O avec asyncio)
    json_data = asyncio.run(download_all(urls))

    # Étape 2 : Traitement CPU en parallèle (multiprocessing)
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(analyse_json, json_data)

    # Étape 3 : Sauvegarde (I/O, ici simulée)
    for result in results:
        with open(f"output_{result['id']}.json", "w") as f:
            json.dump(result, f)

if __name__ == "__main__":
    main()
```

---

### 💡 Points clés :

- `asyncio.run(...)` pour lancer le code asynchrone (I/O)
- `Pool.map(...)` pour paralléliser le calcul CPU
- On **évite de mélanger** asyncio et multiprocessing dans le même thread/process
- Les données JSON sont d’abord collectées, puis traitées

---

### 🔧 En bonus : alternatives avancées

- Combiner avec **ThreadPoolExecutor** pour du I/O bloquant (genre accès fichiers, DB)
- Découper le pipeline avec un **scheduler** (ex : `concurrent.futures`, `ray`, ou `dask`)

---
