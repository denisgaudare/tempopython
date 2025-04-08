# ✅ Objectifs pédagogiques

À l’issue de cette formation, les participants devront être capables de :
- Comprendre la structure interne de Matplotlib (Figure/Axes/Artist).
- Créer des visualisations personnalisées et adaptées à des jeux de données complexes.
- Exploiter les intégrations avec Pandas, Numpy.
- Contrôler précisément l’apparence, le layout et les styles.
- Générer des graphiques réutilisables, interactifs, ou exportables (SVG, PDF, etc).

---

## 🧱 Partie 1 — Fondations : l'architecture de Matplotlib

### 🔸 1.1 — Architecture orientée objets
#### Concepts clés :
- `Figure` : conteneur global du dessin.
- `Axes` : zone de tracé (grille, axes X/Y, titres, etc).
- `Axis` : axe horizontal/vertical (gère les ticks, labels).
- `Artist` : tout ce qui est dessiné (courbe, texte, titre...).

**Exercice** : créer un graphe avec l’approche objet.

```python
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot([1, 2, 3], [4, 1, 2])
plt.show()
```

> 💡 Pourquoi cette architecture ? Pour un contrôle fin de chaque élément.

---

## 📊 Partie 2 — Utilisation de haut niveau avec `pyplot`

### 🔸 2.1 — Interface de type état (state-based)
`matplotlib.pyplot` agit comme une surcouche à l’API objet, en maintenant une figure/axes active.

```python
plt.plot([1, 2, 3], [4, 1, 2])  # Ajoute à la figure/axes active
plt.title("Simple plot")
plt.show()
```

**Comparaison entre style OO et pyplot**  
> Avantage de pyplot pour les scripts rapides ou notebooks.

---

## 🎨 Partie 3 — Personnalisation avancée

### 🔸 3.1 — Axes, ticks et grilles
- `ax.set_xlim`, `ax.set_ylim`
- `ax.set_xticks`, `ax.set_xticklabels`
- `ax.grid(True, linestyle='--')`

### 🔸 3.2 — Styles et apparence
- Couleurs (`color`, `cmap` pour colormaps)
- Styles de lignes (`linestyle`, `linewidth`)
- Marqueurs (`marker`, `markersize`)

```python
ax.plot(x, y, linestyle='--', marker='o', color='r')
```

### 🔸 3.3 — Annotations
```python
ax.annotate('Max point', xy=(x, y), xytext=(x+1, y+1),
            arrowprops=dict(facecolor='black'))
```

---

## 🧩 Partie 4 — Layouts complexes et sous-graphes

### 🔸 4.1 — Subplots, subgrids
- `plt.subplots(nrows, ncols)`
- `fig.add_gridspec(...)` pour des layouts plus précis

### 🔸 4.2 — `tight_layout()` vs `constrained_layout()`
Gestion des espacements automatiques

---

## 🧮 Partie 5 — Intégration avec Pandas & Numpy

### 🔸 5.1 — Séries et DataFrames
```python
import pandas as pd
df = pd.DataFrame({"A": [1, 2, 3], "B": [3, 1, 2]})
df.plot(kind='line')  # utilise matplotlib en backend
```

### 🔸 5.2 — Visualisation de données numériques
- Histogrammes, scatter plots, heatmaps

```python
ax.hist(data, bins=30)
ax.scatter(x, y, alpha=0.5)
```

---

## 🖼️ Partie 6 — Sauvegarde & Export

- `fig.savefig('output.png', dpi=300)`
- Format vectoriel : SVG, PDF
- Transparence, taille personnalisée

---

## 🔁 Partie 7 — Animations & Interactions (avancé)

### 🔸 7.1 — `FuncAnimation` pour créer des animations dynamiques
```python
from matplotlib.animation import FuncAnimation
```

### 🔸 7.2 — Utilisation interactive dans Jupyter : `%matplotlib notebook`

---

## 🌈 Partie 8 — Styles et Thèmes

- `plt.style.use('ggplot')`, `seaborn`, `dark_background`, etc.
- Créer son propre style (`.mplstyle`)

---

## 🔧 Partie 9 — Bonnes pratiques & Performance

- Réutiliser les objets Figure/Axes
- Éviter `plt.*` dans du code modulaire
- Limiter le nombre de redessins

---

## 🧪 Exercices finaux

1. Reproduire un graphique de type **multi-axes synchronisés** (deux y-axes).
2. Visualiser un **DataFrame temporel** avec moyennes mobiles, fenêtres glissantes.
3. Créer une **carte thermique** de corrélation avec annotations.
4. Générer un **dashboard statique** avec plusieurs subplots.

---

Souhaites-tu que je te prépare :
- les **exemples de code complets** pour chaque partie ?
- un **notebook Jupyter interactif** pour les participants ?
- un **support PDF** de la formation avec théorie + exos ?
- une **grille de progression** pour les exercices avec corrections ?