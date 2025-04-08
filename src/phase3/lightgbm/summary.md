Ah là tu touches à du **lourd pour la modélisation rapide et performante** !  
### 🚀 `LightGBM` = Light Gradient Boosting Machine

---

## 🔍 C’est quoi LightGBM ?

**LightGBM** est une **librairie de machine learning** open-source développée par **Microsoft**.  
Elle implémente l’algorithme **gradient boosting** de façon **ultra-optimisée**, notamment pour les gros datasets.

### ✅ C’est l’une des meilleures librairies pour :
- 🔮 **Classification / Régression**
- 📈 **Ranking (ex. moteur de recherche)**
- 🧠 Features très hautement catégoriques
- 🏎️ Gérer des **millions de lignes avec peu de RAM**
- 🧪 Gagner des **compétitions Kaggle** (elle est adorée là-bas)

---

## ⚙️ Pourquoi LightGBM est rapide ?

| Optimisation | Description |
|--------------|-------------|
| **Histogram-based** | Regroupe les valeurs en bins pour accélérer les splits |
| **Leaf-wise growth** | L’arbre se développe selon la *meilleure perte* plutôt que par niveau |
| **Support du multi-thread** | Exploite plusieurs cœurs CPU |
| **Support GPU** | Pour de gros jeux de données |

---

## 📦 Installation

```bash
pip install lightgbm
```

Pour GPU :
```bash
pip install lightgbm --install-option=--gpu
# ou mieux : compiler depuis source avec CUDA
```

---

## 🔁 Exemple rapide d’utilisation avec Pandas

```python
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# Exemple fictif
df = pd.read_csv("flights.csv")
df = df[df["duration_minutes"] < 1000]

X = df[["duration_minutes"]]  # ou plus de features
y = (df["duration_minutes"] > 300).astype(int)  # prédire si vol long

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)

train_data = lgb.Dataset(X_train, label=y_train)
val_data = lgb.Dataset(X_val, label=y_val, reference=train_data)

params = {
    "objective": "binary",
    "metric": "binary_logloss",
    "verbosity": -1
}

model = lgb.train(params, train_data, valid_sets=[val_data], num_boost_round=100, early_stopping_rounds=10)

# Prédictions
y_pred = model.predict(X_val)
y_pred_labels = (y_pred > 0.5).astype(int)
print("Accuracy:", accuracy_score(y_val, y_pred_labels))
```

---

## 🧠 Pour aller plus loin :

- Compatible avec **scikit-learn API** : `lgb.LGBMClassifier()`, etc.
- Gère les **valeurs manquantes**, les **catégories**, les **poids**
- Très utilisé en production (très stable)
- Peut être **interprété** (via SHAP ou `plot_importance`)
- Autres librairies comme XGBoost ou CatBoost 

---
