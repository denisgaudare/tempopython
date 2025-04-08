# Filtrage des données avec `pandas`**, 
# avec exemples concrets pour bien comprendre :

### 🔹 1. **Filtrage par condition logique simple**
```python
df[df['colonne'] > 10]
```

> Ex : toutes les lignes où la valeur dans la colonne `"colonne"` est supérieure à 10.

---

### 🔹 2. **Filtrage avec plusieurs conditions**
```python
df[(df['col1'] > 5) & (df['col2'] == 'A')]
```

> Utilise `&`, `|`, `~` pour AND, OR, NOT avec des parenthèses autour de chaque condition.

---

### 🔹 3. **Filtrage avec `isin()`**
```python
df[df['ville'].isin(['Paris', 'Lyon'])]
```

> Garde les lignes où la ville est soit Paris, soit Lyon.

---

### 🔹 4. **Filtrage avec `str.contains()` pour les chaînes**
```python
df[df['nom'].str.contains('Jean')]
```

> Filtre les lignes où la colonne `'nom'` contient le mot `'Jean'`.

---

### 🔹 5. **Filtrage avec `query()`**
```python
df.query("col1 > 5 and col2 == 'A'")
```

> Plus lisible pour les requêtes complexes, fonctionne comme une mini-langue SQL.

---

### 🔹 6. **Filtrage par index**
```python
df.loc['2023-01-01']           # si index est une date
df.iloc[0:10]                  # 10 premières lignes
```

---

### 🔹 7. **Filtrage avec `between()`**
```python
df[df['colonne'].between(10, 20)]
```

> Garde les lignes entre deux bornes incluses.

---

### 🔹 8. **Filtrage des valeurs manquantes**
```python
df[df['colonne'].notna()]     # ou ~df['colonne'].isna()
```

---

### 🔹 9. **Filtrage avec une fonction personnalisée**
```python
df[df['colonne'].apply(lambda x: x % 2 == 0)]
```

> Filtre les lignes selon une logique arbitraire (ici : valeurs paires).
