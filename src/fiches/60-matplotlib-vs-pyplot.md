Voici plusieurs exemples de code utilisant **Matplotlib bas niveau** et leurs équivalents en **Pyplot (approche MATLAB-like)**.  

---

## **1. Tracé simple de courbe**
📌 **Approche Matplotlib bas niveau (orienté objet)**
```python
import matplotlib.figure as mpl_fig
import matplotlib.backends.backend_agg as agg

# Création de la figure et de l'axe
fig = mpl_fig.Figure()
canvas = agg.FigureCanvasAgg(fig)
ax = fig.add_subplot(1, 1, 1)

# Ajout de la courbe
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='blue', label='Courbe')

# Ajout des titres et labels
ax.set_title("Courbe en Matplotlib (bas niveau)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.legend()

# Dessin (pas d'affichage interactif ici)
canvas.draw()
```

📌 **Approche Pyplot (MATLAB-like)**
```python
import matplotlib.pyplot as plt

# Tracé rapide avec Pyplot
plt.plot([1, 2, 3, 4], [10, 20, 25, 30], color='blue', label='Courbe')

# Ajout des titres et labels
plt.title("Courbe en Pyplot (MATLAB-like)")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

# Affichage direct
plt.show()
```

---

## **2. Création de plusieurs sous-graphiques (subplots)**
📌 **Matplotlib bas niveau (avec gestion d'axes explicite)**
```python
import matplotlib.pyplot as plt

# Création de la figure et des axes
fig = plt.figure()

# Ajout de deux sous-graphiques (subplot)
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

# Tracé des données
ax1.plot([1, 2, 3, 4], [10, 20, 30, 40], 'r')
ax2.plot([1, 2, 3, 4], [40, 30, 20, 10], 'b')

# Ajout de titres
ax1.set_title("Graphe 1")
ax2.set_title("Graphe 2")

# Affichage
plt.show()
```

📌 **Approche Pyplot avec `plt.subplots()` (simplifiée)**
```python
import matplotlib.pyplot as plt

# Création des sous-graphiques
fig, (ax1, ax2) = plt.subplots(2, 1)

# Tracé des données
ax1.plot([1, 2, 3, 4], [10, 20, 30, 40], 'r')
ax2.plot([1, 2, 3, 4], [40, 30, 20, 10], 'b')

# Ajout de titres
ax1.set_title("Graphe 1")
ax2.set_title("Graphe 2")

# Affichage
plt.show()
```

---

## **3. Histogramme**
📌 **Matplotlib bas niveau**
```python
import numpy as np
import matplotlib.pyplot as plt

# Données aléatoires
data = np.random.randn(1000)

# Création de la figure et de l'axe
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Création de l'histogramme
ax.hist(data, bins=30, color='green', edgecolor='black')

# Titre et labels
ax.set_title("Histogramme (Matplotlib bas niveau)")
ax.set_xlabel("Valeurs")
ax.set_ylabel("Fréquence")

# Affichage
plt.show()
```

📌 **Approche Pyplot**
```python
import numpy as np
import matplotlib.pyplot as plt

# Données aléatoires
data = np.random.randn(1000)

# Histogramme rapide
plt.hist(data, bins=30, color='green', edgecolor='black')

# Titre et labels
plt.title("Histogramme (Pyplot MATLAB-like)")
plt.xlabel("Valeurs")
plt.ylabel("Fréquence")

# Affichage
plt.show()
```

---

## **4. Scatter Plot (Nuage de points)**
📌 **Matplotlib bas niveau**
```python
import numpy as np
import matplotlib.pyplot as plt

# Données aléatoires
x = np.random.rand(50)
y = np.random.rand(50)

# Création de la figure et de l'axe
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Création du scatter plot
ax.scatter(x, y, color='purple', label='Points')

# Ajout des titres et légende
ax.set_title("Scatter Plot (Matplotlib bas niveau)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.legend()

# Affichage
plt.show()
```

📌 **Approche Pyplot**
```python
import numpy as np
import matplotlib.pyplot as plt

# Données aléatoires
x = np.random.rand(50)
y = np.random.rand(50)

# Scatter plot rapide
plt.scatter(x, y, color='purple', label='Points')

# Ajout des titres et légende
plt.title("Scatter Plot (Pyplot MATLAB-like)")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

# Affichage
plt.show()
```

---

## **💡 Comparaison et Conclusion**
| **Critère**              | **Matplotlib (bas niveau)**                         | **Pyplot (MATLAB-like)**                   |
|-------------------------|------------------------------------------------|--------------------------------------------|
| **Simplicité**          | Plus verbeux, plus de contrôle | Syntaxe concise, facile à comprendre |
| **Flexibilité**         | Gestion avancée des figures et axes | Automatisation de la gestion des figures |
| **Utilisation typique** | Projets complexes, applications GUI | Notebooks, scripts d’analyse rapide |

👉 **Si vous voulez une approche plus proche de MATLAB et rapide à écrire, utilisez Pyplot (`plt`).**  
👉 **Si vous voulez un contrôle total (ex. plusieurs figures dans une application), utilisez Matplotlib en bas niveau.**