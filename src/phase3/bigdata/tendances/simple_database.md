
## ✈️ Cas d’usage : Sauvegarde de `flights.csv` dans SQLite

### 🎯 Objectif :
1. Charger un fichier CSV de vols (`flights.csv`) dans un `pandas.DataFrame`.
2. Nettoyer les données (optionnel).
3. Sauvegarder les données dans une base SQLite nommée `flights.db`.

---

### 📁 Exemple de fichier `flights.csv` (extrait fictif)

```csv
flight_id,origin,destination,departure,arrival,airline
AB1234,CDG,JFK,2025-04-10 08:30,2025-04-10 11:30,Air France
XY5678,LHR,DXB,2025-04-10 10:00,2025-04-10 18:00,Emirates
```

---

### 📦 Prérequis

```bash
pip install pandas
```

---

### 🧠 Code complet

```python
import pandas as pd
import sqlite3

# 1. Chargement du CSV dans un DataFrame
df = pd.read_csv("flights.csv")
print("Aperçu du fichier CSV :")
print(df.head())

# 2. Nettoyage simple (optionnel)
# Exemple : enlever les doublons
df.drop_duplicates(inplace=True)

# 3. Connexion à SQLite (fichier flights.db créé s’il n’existe pas)
conn = sqlite3.connect("flights.db")

# 4. Sauvegarde dans la base : table 'flights'
df.to_sql("flights", conn, if_exists="replace", index=False)

print("Les données ont été sauvegardées dans flights.db")

# 5. Vérification (lecture depuis SQLite)
df_from_db = pd.read_sql("SELECT * FROM flights", conn)
print("Données relues depuis la base :")
print(df_from_db.head())

# 6. Fermeture de la connexion
conn.close()
```

---

### ✅ Résultat attendu

- Création d’un fichier `flights.db`.
- Création d’une table `flights` avec les colonnes issues du CSV.
- Lecture et impression d’un aperçu des données depuis SQLite.

---

### ⚖️ Avantages de cette approche

- **Très rapide à mettre en place**.
- Idéal pour les scripts de data pipeline.
- Intégration directe entre `pandas` et `SQLite`.

### ❗ Limites

- Pas de typage explicite (tout est interprété automatiquement par pandas/sqlite).
- Moins de contrôle sur les relations (pas de clé étrangère).
- Pas optimal pour de très grosses bases ou des modèles complexes (→ préférer SQLAlchemy ou PostgreSQL).
