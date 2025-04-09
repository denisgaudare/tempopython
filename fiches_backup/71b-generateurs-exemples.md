# **📌 Différentes méthodes de création d’un générateur en Python 🚀**
Les **générateurs** sont une **fonctionnalité clé** en Python qui permet **de générer des valeurs à la demande**, évitant ainsi l’utilisation excessive de mémoire.

Il existe **plusieurs façons de créer un générateur** en Python :
1. ✅ **Avec `yield`** (fonction génératrice classique)
2. ✅ **Avec une expression génératrice (`genexpr`)**
3. ✅ **Avec un décorateur**
4. ✅ **Avec une classe implémentant `__iter__` et `__next__`**
5. ✅ **Avec une bibliothèque spécialisée (`itertools`, `more-itertools`)**

---

# **🔹 1. Générateur avec `yield`**
📌 **La méthode classique et intuitive.**  
✅ **Utilise `yield` pour "suspendre" et reprendre l’exécution.**  

### **Exemple : Générateur de nombres pairs**
```python
def even_numbers(n: int):
    """Génère les n premiers nombres pairs."""
    num = 0
    for _ in range(n):
        yield num
        num += 2

gen = even_numbers(5)
print(list(gen))  # ✅ [0, 2, 4, 6, 8]
```
✅ **Évite de stocker la liste entière en mémoire**.  

---

# **🔹 2. Générateur avec une expression (`genexpr`)**
📌 **Plus concis que `yield`, idéal pour des itérations simples.**  

### **Exemple : Carrés des nombres de 0 à 9**
```python
gen = (x ** 2 for x in range(10))

print(next(gen))  # ✅ 0
print(next(gen))  # ✅ 1
print(list(gen))  # ✅ [4, 9, 16, ..., 81]
```
✅ **Écriture compacte et efficace**.  
❌ **Moins flexible que `yield` pour des logiques complexes**.

---

# **🔹 3. Générateur avec un décorateur**
📌 **Encapsuler une fonction génératrice dans un décorateur** pour **modifier ou enrichir son comportement**.

### **Exemple : Décorateur qui double les valeurs générées**
```python
from functools import wraps

def double_values(generator_func):
    """Décorateur qui double chaque valeur générée."""
    @wraps(generator_func)
    def wrapper(*args, **kwargs):
        for value in generator_func(*args, **kwargs):
            yield value * 2
    return wrapper

@double_values
def countdown(n: int):
    """Génère un compte à rebours."""
    while n > 0:
        yield n
        n -= 1

print(list(countdown(5)))  # ✅ [10, 8, 6, 4, 2]
```
✅ **Modularité accrue** → On peut facilement ajouter un nouveau comportement.  

---

# **🔹 4. Générateur avec une classe (`__iter__` et `__next__`)**
📌 **Approche orientée objet**, utile pour un **état persistant**.  
✅ **Meilleure encapsulation des données**.

### **Exemple : Générateur de Fibonacci**
```python
class Fibonacci:
    def __init__(self, max: int):
        self.max = max
        self.a, self.b = 0, 1

    def __iter__(self):
        return self  # Un itérable est aussi un itérateur

    def __next__(self):
        if self.a > self.max:
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

fib_gen = Fibonacci(10)
print(list(fib_gen))  # ✅ [0, 1, 1, 2, 3, 5, 8]
```
✅ **Bonne gestion des états internes**.  
❌ **Code plus long que `yield`**.  

---

# **🔹 5. Générateur avec `itertools` (librairie standard)**
📌 **Optimisé et performant pour les séquences infinies et combinatoires**.  

### **Exemple : Générer une séquence infinie de nombres**
```python
from itertools import count, cycle

gen = count(start=10, step=5)  # 10, 15, 20, 25...
print(next(gen))  # ✅ 10
print(next(gen))  # ✅ 15
print(next(gen))  # ✅ 20

# Exemple : Boucle infinie sur une liste
colors = cycle(["🔴", "🟢", "🔵"])
print(next(colors))  # ✅ 🔴
print(next(colors))  # ✅ 🟢
```
✅ **Extrêmement optimisé pour les séquences infinies**.  

---

# **🔹 6. Générateur avec `more-itertools` (librairie externe)**
📌 **Fournit des générateurs avancés pour manipuler les données**.

### **Installation**
```bash
pip install more-itertools
```

### **Exemple : Générer des combinaisons glissantes (windows)**
```python
from more_itertools import windowed

gen = windowed(range(10), 3)  # Crée des fenêtres de taille 3
print(list(gen))  # ✅ [(0, 1, 2), (1, 2, 3), ..., (7, 8, 9)]
```
✅ **Idéal pour manipuler des flux de données en continu.**  

---

# **🔹 7. Comparaison des méthodes**
| **Méthode** | **Avantages** | **Inconvénients** |
|------------|--------------|----------------|
| `yield` | Facile à écrire et à lire | Moins optimisé pour les itérations simples |
| **Expression (`genexpr`)** | Ultra-compact et rapide | Moins flexible que `yield` |
| **Avec un décorateur** | Modularité et extensibilité | Complexe à comprendre au début |
| **Avec une classe (`__iter__`)** | Bonne gestion d’état | Code plus long |
| **Avec `itertools`** | Ultra-performant et optimisé | Moins lisible pour un débutant |
| **Avec `more-itertools`** | Puissant pour manipuler les flux | Nécessite une installation externe |

---

# **🔥 Conclusion**
| **Pourquoi utiliser des générateurs ?** ✅ |
|-------------------------------------------|
| **Optimisent la mémoire** 🏋️‍♂️ |
| **Améliorent les performances** 🚀 |
| **Évitent les structures lourdes** 📉 |
| **Permettent une exécution paresseuse (`lazy evaluation`)** ⚡ |