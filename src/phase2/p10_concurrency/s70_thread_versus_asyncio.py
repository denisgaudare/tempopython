import asyncio
import random
import tempfile
import os
import time
import threading

N_FILES = 2000 #essaye avec 5000
ECRITURE = 6000 #essaye avec 1000

def create_and_delete_tempfile(index):
    with tempfile.NamedTemporaryFile(delete=False, mode='w+') as tmp:
        for i in range(ECRITURE):
            tmp.write(f"Temporary data {i}-{index}")
        tmp_path = tmp.name
    os.remove(tmp_path)
    return tmp_path


async def async_create_and_delete_tempfile(index):
    return await asyncio.to_thread(create_and_delete_tempfile, index)


def run_threaded():
    print("Démarrage threading...")
    start = time.time()
    threads = []
    results = []

    def task(index):
        result = create_and_delete_tempfile(index)
        results.append(result)

    for i in range(N_FILES):
        t = threading.Thread(target=task, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end = time.time()
    print(f"Threading terminé en {end - start:.2f} secondes.")
    return {"method": "threading", "duration": end - start, "files": len(results)}


async def run_async():
    print("Démarrage asyncio...")
    start = time.time()
    tasks = [async_create_and_delete_tempfile(i) for i in range(N_FILES)]
    results = await asyncio.gather(*tasks)
    end = time.time()
    print(f"Asyncio terminé en {end - start:.2f} secondes.")
    return {"method": "asyncio", "duration": end - start, "files": len(results)}


def main():
    print("Comparaison entre threading et asyncio\n")
    threading_report = run_threaded()
    asyncio_report = asyncio.run(run_async())

    print("\n📊 Rapport final :")
    for report in [threading_report, asyncio_report]:
        print(f"- Méthode : {report['method']}")
        print(f"  Temps écoulé : {report['duration']:.2f} secondes")
        print(f"  Fichiers traités : {report['files']}\n")


if __name__ == "__main__":
    main()
