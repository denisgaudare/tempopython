### 🧠 Stratégie hybridation :
"""
**Parties CPU-intensives** → utilisent plusieurs **processus** (`multiprocessing`)
**Parties I/O-intensives** (ex : requêtes web, lecture fichiers réseau) → utilisent **asyncio**

### ✅ Exemple concret :

Imaginons un script qui :
1. Charge des fichiers JSON distants (I/O)
2. Fait un gros traitement mathématique sur chaque (CPU)
3. Sauvegarde les résultats (I/O)
"""

### 📦 Code hybride

import asyncio
#import aiohttp
import json
from multiprocessing import Pool, cpu_count

# === Partie CPU (calcul intensif) ===

def analyse_json(data):
    # Simulation de calcul lourd
    total = sum(x**2 for x in data["values"])
    return {"id": data["id"], "score": total}

# === Partie I/O (chargement fichiers) ===

def fetch_json(session, url):
    pass

def download_all(urls):
    pass

# === Orchestration générale ===

def main():
    urls = [
        "https://jsonplaceholder.typicode.com/comments",
        "https://jsonplaceholder.typicode.com/users"
    ] * 10

    # Étape 1 : Download des fichiers en parallèle (I/O avec asyncio)

    # Étape 2 : Traitement CPU en parallèle (multiprocessing)

    # Étape 3 : Sauvegarde (I/O, ici simulée)

if __name__ == "__main__":
    main()
"""
### 💡 Points clés :
- `asyncio.run(...)` pour lancer le code asynchrone (I/O)
- `Pool.map(...)` pour paralléliser le calcul CPU
- On **évite de mélanger** asyncio et multiprocessing dans le même thread/process
- Les données JSON sont d’abord collectées, puis traitées

- Bonus1 : Combiner avec **ThreadPoolExecutor** pour du I/O bloquant (genre accès fichiers, DB)
- Bonus2 : Découper le pipeline avec un **scheduler** (ex : `concurrent.futures`, `ray`, ou `dask`)
"""
