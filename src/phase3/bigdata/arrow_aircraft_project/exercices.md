# 🧠 Exercices avancés PyArrow

---

## 🧪 Exercice 1 — Création et typage explicite

**Objectif** : Créer un tableau Arrow typé explicitement pour un gros DataFrame (> 1M lignes).

### Code à compléter :

```python
import pyarrow as pa
import numpy as np

n = 1_000_000
data = {
    "user_id": np.arange(n),
    "age": np.random.randint(18, 90, size=n),
    "score": np.random.rand(n),
    "active": np.random.choice([True, False], size=n)
}

# Créer un tableau Arrow avec un schéma typé
schema = ...
table = pa.table(data, schema=schema)
print(table.schema)
```

🧠 *Erreur fréquente : oublier de convertir les types numpy → Arrow types compatibles.*

---

## 🧪 Exercice 2 — Écriture Parquet optimisée

**Objectif** : Écrire un tableau en Parquet avec **compression**, puis le relire et vérifier sa taille.

### Code à compléter :

```python
import pyarrow.parquet as pq
import os

# table = ... (généré dans l’exercice 1)
output_path = "big_data.parquet"

# Écriture avec compression zstd
...

# Relecture + taille fichier
table2 = ...
print(table2.num_rows, os.path.getsize(output_path) / 1024**2, "MB")
```

🧠 *Erreur fréquente : mauvaise compression ou oubli de `use_dictionary=True`.*

---

## 🧪 Exercice 3 — Lecture conditionnelle avec filtre

**Objectif** : Lire un fichier Parquet et filtrer les données sans tout charger.

### Code à compléter :

```python
# Lire uniquement les utilisateurs actifs avec age > 50
filtered = pq.read_table(
    "big_data.parquet",
    filters=[
        ("active", "==", True),
        ("age", ">", 50)
    ]
)

print(filtered.num_rows)
```

🧠 *Erreur fréquente : vouloir filtrer manuellement avec `.to_pandas()` (inefficace en mémoire).*

---

## 🧪 Exercice 4 — Agrégation sans conversion pandas

**Objectif** : Calculer la moyenne de score par tranche d'âge sans passer par Pandas.

### Code à compléter :

```python
# Grouper par tranches : 18–29, 30–49, 50–69, 70+
# Bonus : utiliser pyarrow.compute (pa.compute)

import pyarrow.compute as pc

# Étapes :
# 1. ajouter une colonne 'age_group'
# 2. grouper et agréger

# -> Cette partie nécessite de faire des conditions + concaténation dans Arrow
```

🧠 *C'est un peu tricky, car `pyarrow` n’a pas de `groupby()` direct comme Pandas.*

---

## ✅ Corrigés

---

### ✅ Corrigé 1

```python
schema = pa.schema([
    ("user_id", pa.int32()),
    ("age", pa.int8()),
    ("score", pa.float64()),
    ("active", pa.bool_())
])

table = pa.table(data, schema=schema)
```

---

### ✅ Corrigé 2

```python
pq.write_table(table, output_path, compression="zstd", use_dictionary=True)
table2 = pq.read_table(output_path)
```

---

### ✅ Corrigé 3

```python
filtered = pq.read_table(
    output_path,
    filters=[("active", "==", True), ("age", ">", 50)]
)
```

---

### ✅ Corrigé 4 (simplifié)

```python
import pyarrow.compute as pc

age = table.column("age")
conditions = [
    pc.and_(age >= 18, age <= 29),
    pc.and_(age >= 30, age <= 49),
    pc.and_(age >= 50, age <= 69),
    age >= 70
]
labels = ["18-29", "30-49", "50-69", "70+"]

age_groups = pc.case_when(zip(conditions, [pa.scalar(l) for l in labels]), "70+")
table = table.append_column("age_group", age_groups)

# Simuler un groupby avec Pandas :
df = table.to_pandas()
result = df.groupby("age_group")["score"].mean()
print(result)
```

