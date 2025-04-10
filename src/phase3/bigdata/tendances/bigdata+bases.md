

## 🚀 Alternatives à SQLite pour le big data

### 🔷 1. **PostgreSQL** (relationnelle, robuste, open source)

> ✔ Excellent pour les gros volumes de données structurées avec index, vues, et requêtes SQL complexes.

#### 🔌 Connexion avec `sqlalchemy` ou `psycopg2`

```bash
pip install sqlalchemy psycopg2 pandas
```

```python
from sqlalchemy import create_engine
import pandas as pd

# Exemple : chargement depuis CSV
df = pd.read_csv("flights.csv")

# Connexion PostgreSQL
engine = create_engine("postgresql+psycopg2://user:password@host:port/dbname")

# Sauvegarde
df.to_sql("flights", engine, if_exists="replace", index=False)
```

✅ **Avantages** :
- Requêtes SQL avancées
- Indexation, partitionnement, performances
- Supporte extensions : `PostGIS`, `TimescaleDB`…

---

### 🟣 2. **Apache Hive / Presto / Trino** (via `pyhive`, `trino-python-client`)

> ✔ Pour des volumes massifs dans des data lakes (stockage HDFS, S3…)

#### Exemple avec Trino (anciennement PrestoSQL)

```bash
pip install trino pandas
```

```python
import pandas as pd
from trino.dbapi import connect

conn = connect(
    host='trino-server-host',
    port=8080,
    user='your_user',
    catalog='hive',
    schema='default',
)

cursor = conn.cursor()

# Exemple : insérer avec SQL ou via df.to_sql avec sqlalchemy (expérimental)
cursor.execute("CREATE TABLE IF NOT EXISTS flights (flight_id VARCHAR, ...)")
```

✅ **Avantages** :
- Massivement scalable
- Peut requêter des formats Parquet/ORC sur S3
- Intégré dans les écosystèmes big data

❗ **Inconvénient** :
- Plutôt en lecture (batch analytics), pas en écriture fréquente
- Nécessite un écosystème (cluster Hive, Trino, etc.)

---

### 🔶 3. **ClickHouse** (OLAP, très rapide)

> ✔ Pour de l’analytique ultra-rapide sur des milliards de lignes

```bash
pip install clickhouse-connect pandas
```

```python
import clickhouse_connect
client = clickhouse_connect.get_client(host='localhost', database='default')

client.command("""
CREATE TABLE IF NOT EXISTS flights (
    flight_id String,
    origin String,
    destination String,
    departure DateTime,
    arrival DateTime,
    airline String
) ENGINE = MergeTree()
ORDER BY (departure)
""")

# Insertion via dataframe
import pandas as pd
df = pd.read_csv("flights.csv")
client.insert_dataframe('flights', df)
```

✅ **Avantages** :
- Super rapide en lecture (OLAP)
- Parfait pour les dashboards en temps réel
- Compression efficace

---

### 🔷 4. **DuckDB** : le SQLite du big data

> ✔ In-memory SQL analytics engine, compatible avec Pandas, Parquet, CSV, etc.

```bash
pip install duckdb
```

```python
import duckdb
import pandas as pd

df = pd.read_csv("flights.csv")

# DuckDB en mémoire ou sur disque
con = duckdb.connect("flights.duckdb")
con.execute("CREATE TABLE IF NOT EXISTS flights AS SELECT * FROM df")
```

✅ **Avantages** :
- Zéro configuration, rapide, léger
- Requêtes SQL vectorisées sur fichiers Parquet ou CSV
- Supporte les jointures complexes

---

## 📊 Tableau comparatif des bases "big data"

| Base         | Type         | Volume     | Points forts                          | Limites                        |
|--------------|--------------|------------|----------------------------------------|--------------------------------|
| PostgreSQL   | SQL/OLTP     | 10-100M+   | Solide, index, extension, SQL riche    | Moins adapté au scale horizontal |
| ClickHouse   | OLAP         | 100M-1B+   | Vitesse de lecture, analytique rapide | Pas pour transactions          |
| Trino/Hive   | Data Lake    | 1B+        | Multi-source, SQL sur S3/HDFS         | Infrastructure lourde          |
| DuckDB       | In-Memory    | 10M-1B     | Léger, analytique, support parquet    | Moins bon en multi-utilisateur |
| SQLite       | Local SQL    | <10M       | Simple, local                         | Pas scalable                   |

---