# **Fonctions plus avancées avec NumPy**, 
## et utilisation avec Pandas

### 🔧 Exemples de Fonctions Avancées NumPy

#### 1. **`np.where`** – Filtrage conditionnel
```python
import numpy as np

arr = np.array([10, 15, 20, 25])
result = np.where(arr > 18, "Yes", "No")
print(result)  # ['No' 'No' 'Yes' 'Yes']
```

#### 2. **`np.select`** – Cas multiples (équivalent de `case when`)
```python
conditions = [arr < 15, (arr >= 15) & (arr < 25), arr >= 25]
choices = ['low', 'medium', 'high']
labels = np.select(conditions, choices)
print(labels)  # ['low' 'medium' 'medium' 'high']
```

#### 3. **`np.vectorize`** – Appliquer une fonction Python à un tableau
```python
def custom_func(x):
    return x ** 2 + 1

vec_func = np.vectorize(custom_func)
print(vec_func(arr))  # [101 226 401 626]
```

#### 4. **`np.apply_along_axis`** – Appliquer une fonction sur un axe
```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Moyenne de chaque ligne
means = np.apply_along_axis(np.mean, axis=1, arr=matrix)
print(means)  # [2. 5.]
```

#### 5. **`np.linalg`** – Algèbre linéaire
```python
from numpy.linalg import inv

A = np.array([[1, 2], [3, 4]])
inv_A = inv(A)
print(inv_A)
```

#### 6. **Broadcasting avancé**
```python
a = np.array([[1], [2], [3]])   # shape (3,1)
b = np.array([10, 20, 30])      # shape (3,)
print(a + b)
```

---

### 🔄 Interconnexion NumPy / Pandas

#### 1. **Pandas est construit sur NumPy**
- Un `DataFrame` ou `Series` Pandas **utilise un tableau NumPy** en interne pour stocker les données.
- Cela permet d’avoir les performances et la vectorisation de NumPy **avec une interface plus haut niveau** (colonnes nommées, types mixtes, gestion des dates, etc.).

#### 2. **Conversion entre les deux**
```python
import pandas as pd

# De pandas vers NumPy
df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
np_array = df.to_numpy()

# De NumPy vers pandas
new_df = pd.DataFrame(np_array, columns=["a", "b"])
```

#### 3. **Utiliser des fonctions NumPy dans Pandas**
Pandas permet d’utiliser des fonctions NumPy directement :
```python
df = pd.DataFrame({"val": [1, 2, 3, 4]})
df["log"] = np.log(df["val"])
```

#### 4. **Performance / mémoire**
- NumPy est plus rapide pour des **données homogènes** et des **opérations numériques lourdes**.
- Pandas est plus adapté pour des **données tabulaires complexes**, avec des colonnes hétérogènes, du texte, des dates, etc.

---

### 📌 Résumé

| Aspect | NumPy | Pandas |
|-------|-------|--------|
| Structure principale | `ndarray` | `DataFrame` / `Series` |
| Vitesse | Très rapide | Rapide (sur NumPy) |
| Données | Homogènes | Hétérogènes |
| Utilisation | Traitement numérique, ML | Analyse de données, Data Science |
