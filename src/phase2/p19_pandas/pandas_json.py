import json
import pandas as pd

from commontools.consoles import pause

def print_full(x,message=None):
    if message:
        tirets = "-" * len(message)
        print(tirets + "\n"+message+"\n"+tirets)
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')


# lecture BRUTE
print("Avec read_json")
df = pd.read_json("pandas_json.json")
print(df)

pause()

print("Avec open")
with open("pandas_json.json") as f:
    data = json.load(f)

# Transformer le JSON en DataFrame plat
df = pd.json_normalize(
    data,
    sep="_"  # remplace le '.' par '_' dans les noms de colonnes
)

print(df)


pause()

# Lire le fichier
df_raw = pd.read_json("pandas_json.json")

# Aplatir les colonnes imbriquées
df_flat = pd.json_normalize(df_raw.to_dict(orient="records"), sep="_")

print_full(df_flat)