# **Au-delà des bases de NumPy**

- performance vectorielle
- broadcasting
- opérations avancées
- applications concrètes (math, analyse, image, machine learning)

---
### 🗂️ **1. Intro**
- Pourquoi NumPy ? (performance, compatibilité C, machine learning)
- Bench rapide vs liste Python
- Structure centrale : `ndarray`

### 🧪 Exemple :
```python
import numpy as np
import time

lst = list(range(10_000_000))
arr = np.arange(10_000_000)

# carré des éléments
start = time.time(); [x**2 for x in lst]; print("List:", time.time() - start)
start = time.time(); arr ** 2; print("NumPy:", time.time() - start)
```

---

### 🔢 **2. Création et inspection de tableaux**

#### Fonctions clés :
- `np.array`, `np.arange`, `np.linspace`, `np.zeros`, `np.ones`, `np.eye`, `np.random`

#### Propriétés utiles :
- `.shape`, `.dtype`, `.ndim`, `.size`

### 🧪 Exemple :
```python
import numpy as np
a = np.zeros((2, 3))
b = np.random.randint(0, 10, size=(3, 3))
print("Shape:", b.shape)
```

---

### ✂️ **3. Indexation, slicing et masques**

- Indexation classique vs booléenne
- Masquage (`arr[arr > 0.5]`)
- Modification par masque

### 🧪 Exemple :
```python
a = np.arange(10)
a[a % 2 == 0] = -1  # remplacer les pairs
```

---

### 🧮 **4. Opérations vectorisées (15 min)**

- Opérations élémentaires (`+`, `*`, `**`, `log`, `sin`)
- Comparaison avec boucle Python
- Broadcasting : opérations entre tableaux de formes différentes

### 🧪 Exemple :
```python
a = np.arange(3).reshape(3, 1)
b = np.arange(4).reshape(1, 4)
print(a + b)  # grille d'addition 3x4
```

---

### 🔁 **5. Agrégation et statistiques (10 min)**

- `np.sum`, `np.mean`, `np.std`, `np.min`, `np.max`, `np.percentile`, `np.cumsum`, `np.cumprod`
- Axe des dimensions (`axis=0` / `axis=1`)

### 🧪 Exemple :
```python
data = np.random.rand(5, 10)
print("Par ligne :", data.mean(axis=1))
```

---

### 🧩 **6. Manipulation des tableaux (15 min)**

- `reshape`, `flatten`, `ravel`, `transpose`, `swapaxes`
- `concatenate`, `stack`, `split`
- `np.tile`, `np.repeat`

### 🧪 Exemple :
```python
a = np.array([[1, 2], [3, 4]])
print(np.repeat(a, 2, axis=0))
```

---

### 🧰 **7. Cas concrets / démos (20-30 min)**

#### 🖼️ Image (via Pillow ou matplotlib)
```python
from PIL import Image
img = np.array(Image.open("example.png"))
gray = img.mean(axis=2)  # passage en niveaux de gris
```

#### 📊 Simulation : lancer de dés vectorisé
```python
np.random.seed(0)
rolls = np.random.randint(1, 7, size=(1000, 10))
sums = rolls.sum(axis=1)
```

#### 🧠 ML : produit matriciel pour prédiction
```python
X = np.random.rand(100, 3)
w = np.array([0.1, 0.5, -0.2])
y_pred = X @ w
```

---

### 🚀 **8. Bonus selon le temps**
- `np.where`, `np.clip`, `np.argsort`, `np.unique`, `np.isnan`
- `np.linalg` (inversion, déterminant, eigen)
- `np.memmap`, `dtype`, `structured arrays` pour les experts

---

## 🧩 Conclusion
- Utiliser NumPy, c’est penser "tableau entier", pas élément par élément
- Performances boostées, code plus concis, compatible avec pandas, sklearn, etc.

---
https://numpy.org/devdocs/user/
https://courspython.com/apprendre-numpy.html
https://zestedesavoir.com/tutoriels/pdf/4139/les-bases-de-numpy-et-matplotlib.pdf

