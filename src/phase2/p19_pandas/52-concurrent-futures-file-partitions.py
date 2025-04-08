import concurrent.futures
import pandas as pd

def process_file(path):
    df = pd.read_csv(path, parse_dates=["date"])
    df = df[df["montant"] > 0]
    return df.groupby("categorie")["montant"].mean()

paths = [f"big_transactions/transactions_{i:02d}.csv" for i in range(1,4)]

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(process_file, paths))

# Fusion des résultats
final = pd.concat(results).groupby(level=0).mean()
print(final)
