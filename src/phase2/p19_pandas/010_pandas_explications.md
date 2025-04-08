# **Opérations sur un DataFrame Pandas**, 
## pour **chaque étape** une fonction **différente**

https://www.python-simple.com/python-pandas/panda-intro.php
https://datascientist.fr/blog/guide-ultime-maitriser-pandas-numpy-python/

### 🧪 Exemple de base

On commence avec ce DataFrame :

```python
import pandas as pd

data = {
    "nom": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [25, 30, 35, 40, 45],
    "ville": ["Paris", "Lyon", "Marseille", "Paris", "Lyon"],
    "revenu": [3000, 2500, 4000, 3500, 2700],
}

df = pd.DataFrame(data)
print(df)
```

---

### 🧩 Étapes de modification avec explications

---

#### 1. `df.rename()`
**But** : Renommer les colonnes pour améliorer la lisibilité ou standardiser.

```python
df = df.rename(columns={"nom": "prenom", "ville": "localisation"})
```

✅ Ici on remplace `"nom"` par `"prenom"` et `"ville"` par `"localisation"`.

---

#### 2. `df["colonne"] = ...`
**But** : Ajouter une nouvelle colonne calculée.

```python
df["revenu_annuel"] = df["revenu"] * 12
```

✅ On ajoute une colonne "revenu_annuel" en multipliant par 12.

---

#### 3. `df.drop()`
**But** : Supprimer une ou plusieurs colonnes (ou lignes).

```python
df = df.drop(columns=["revenu"])
```

✅ On supprime la colonne `"revenu"` car on a maintenant `"revenu_annuel"`.

---

#### 4. `df.loc[]` ou `df.iloc[]`
**But** : Modifier certaines lignes/cellules précises.

```python
df.loc[df["prenom"] == "Eva", "age"] = 46
```

✅ On corrige l’âge d’Eva à 46 ans.

---

#### 5. `df.sort_values()`
**But** : Trier le DataFrame par une ou plusieurs colonnes.

```python
df = df.sort_values(by="revenu_annuel", ascending=False)
```

✅ On trie du revenu annuel le plus élevé au plus faible.

---

#### 6. `df.groupby()`
**But** : Regrouper les données pour effectuer des agrégations (somme, moyenne, etc.).

```python
revenu_par_ville = df.groupby("localisation")["revenu_annuel"].mean()
```

✅ Moyenne des revenus par ville dans une **Série Pandas**.

---

#### 7. `df.merge()`
**But** : Joindre deux DataFrames (comme une jointure SQL).

```python
infos_villes = pd.DataFrame({
    "localisation": ["Paris", "Lyon", "Marseille"],
    "population": [2200000, 500000, 870000]
})

df = df.merge(infos_villes, on="localisation", how="left")
```

✅ Ajoute la population des villes à chaque ligne du DataFrame principal.

---

#### 8. `df.apply()` avec `axis`
**But** : Appliquer une fonction à chaque ligne ou colonne.

```python
df["categorie_age"] = df["age"].apply(lambda x: "jeune" if x < 35 else "senior")
```

✅ On crée une catégorie en fonction de l'âge.

---

#### 9. `df.fillna()`
**But** : Remplacer les valeurs manquantes.

```python
df["revenu_annuel"] = df["revenu_annuel"].fillna(0)
```

✅ Très utile après une jointure ou des calculs.

---

#### 10. `df.query()`
**But** : Filtrer les lignes avec une syntaxe proche de SQL.

```python
df_jeunes = df.query("categorie_age == 'jeune' and revenu_annuel > 30000")
```

✅ On filtre les jeunes ayant un revenu annuel > 30 000.

---

### 🧾 Résumé des fonctions utilisées

| Fonction Pandas      | Rôle                                      |
|----------------------|-------------------------------------------|
| `rename()`           | Renommer colonnes                         |
| `drop()`             | Supprimer colonnes ou lignes              |
| `sort_values()`      | Trier                                      |
| `groupby()`          | Agréger par groupe                        |
| `merge()`            | Joindre deux DataFrames                   |
| `apply()`            | Appliquer une fonction ligne/colonne      |
| `fillna()`           | Gérer les valeurs manquantes              |
| `query()`            | Filtrer de manière lisible                |
| `loc[]` / `iloc[]`   | Accès/modif par position ou condition     |

---
Autres liens

https://www.datacamp.com/fr/tutorial/pandas

https://moncoachdata.com/blog/pandas-pour-le-traitement-de-donnees/

https://dzone.com/articles/comprehensive-guide-to-data-analysis
https://dzone.com/articles/the-power-of-visualization-in-exploratory-data-ana
