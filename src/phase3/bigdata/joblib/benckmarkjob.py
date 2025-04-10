# Mini projet : Comparaison de performance entre joblib et multiprocessing
import os
import glob
import pandas as pd
from joblib import Memory, Parallel, delayed
from multiprocessing import Pool
import time
import psutil

# Créer le cache pour mémoization
memory = Memory(location=".joblib_cache", verbose=1)

# Dossier contenant les fichiers flights_*.csv ou .parquet
DATA_DIR = "data"

# Fonction lourde simulée : calcule moyenne retard
def _process_file(file_path):
    print(f"Traitement de {file_path}...")
    time.sleep(1)  # Simulation traitement long
    df = pd.read_csv(file_path) if file_path.endswith(".csv") else pd.read_parquet(file_path)
    return df.groupby("airline")["delay"].mean()

@memory.cache
def process_file_cached(file_path):
    return _process_file(file_path)

# Liste des fichiers CSV ou Parquet
def get_flight_files(extension=".csv"):
    return sorted(glob.glob(os.path.join(DATA_DIR, f"*{extension}")))

# Traitement avec multiprocessing.Pool
def process_all_files_mp(extension=".csv"):
    files = get_flight_files(extension)
    with Pool(processes=4) as pool:
        results = pool.map(_process_file, files)
    return pd.concat(results, axis=1).mean(axis=1).sort_values(ascending=False)

# Benchmark avec usage CPU/RAM
def benchmark_processing(extension=".csv"):
    print("\n--- Traitement Multiprocessing ---")
    process = psutil.Process(os.getpid())
    cpu_before = psutil.cpu_percent(interval=None)
    mem_before = process.memory_info().rss / 1024**2
    start = time.time()
    result = process_all_files_mp(extension)
    duration = time.time() - start
    mem_after = process.memory_info().rss / 1024**2
    cpu_after = psutil.cpu_percent(interval=None)

    print(result)
    print(f"Durée : {duration:.2f}s")
    print(f"Mémoire utilisée : {mem_after - mem_before:.2f} Mo")
    print(f"CPU utilisé : {cpu_after}% (valeur ponctuelle)")

def benchmark_jobs(extension=".csv"):
    files = get_flight_files(extension)
    print("\n--- Traitement Joblib ---")
    process = psutil.Process(os.getpid())
    cpu_before = psutil.cpu_percent(interval=None)
    mem_before = process.memory_info().rss / 1024**2
    start = time.time()
    results = Parallel(n_jobs=4)(delayed(process_file_cached)(f) for f in files)
    duration = time.time() - start
    mem_after = process.memory_info().rss / 1024**2
    cpu_after = psutil.cpu_percent(interval=None)

    print(results)
    print(f"Durée : {duration:.2f}s")
    print(f"Mémoire utilisée : {mem_after - mem_before:.2f} Mo")
    print(f"CPU utilisé : {cpu_after}% (valeur ponctuelle)")
if __name__ == "__main__":
    benchmark_processing(".csv")
    benchmark_jobs(".csv")
    #benchmark_processing(".parquet")
