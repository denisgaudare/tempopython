### **📌 Les Piliers du Paradigme Fonctionnel en Python**
Le **paradigme fonctionnel** repose sur plusieurs concepts clés. En Python, bien que le langage soit principalement **orienté objet**, il prend en charge **la programmation fonctionnelle** grâce à des outils spécifiques.

---

## **🔹 1. First-Class Functions (Fonctions de Première Classe)**
✅ **Définition** : Les fonctions sont **des objets comme les autres**, pouvant être :
- Assignées à des variables
- Passées en arguments
- Retourner d'autres fonctions

```python
def square(x):
    return x * x

func = square  # Affectation
print(func(5))  # 25
```
➡ **Pourquoi ?** Cela permet d’écrire **du code générique et réutilisable**.

---

## **🔹 2. Fonctions Pures et Immutabilité**
✅ **Définition** :
- Une **fonction pure** **ne modifie pas l’état global** et **dépend uniquement de ses entrées**.
- L’**immutabilité** empêche la modification des variables après leur création.

```python
# Fonction pure : pas d'effet de bord
def add(a, b):
    return a + b

print(add(2, 3))  # Toujours 5
```

❌ Mauvaise approche (effet de bord) :
```python
total = 0
def add_to_total(x):
    global total
    total += x  # Effet de bord

add_to_total(5)  # Modifie `total`
```
➡ **Pourquoi ?** Évite les **bugs imprévisibles** liés à l'état global.

---

## **🔹 3. Fonctions d’Ordre Supérieur**
✅ **Définition** : Une fonction qui prend **une autre fonction en argument** ou qui en retourne une.

```python
def apply_function(func, value):
    return func(value)

print(apply_function(lambda x: x * 2, 10))  # 20
```
➡ **Pourquoi ?** Permet de **paramétrer le comportement** d'une fonction.

---

## **🔹 4. Fonctions Anonymes (`lambda`)**
✅ **Définition** : Fonction courte sans `def`.

```python
double = lambda x: x * 2
print(double(4))  # 8
```
➡ **Pourquoi ?** Idéal pour **les opérations simples et les callbacks**.

---

## **🔹 5. Fonctions `map()`, `filter()`, `reduce()`**
### **📌 `map()`**
✅ **Applique une fonction à chaque élément d’un iterable**.

```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16]
```

---

### **📌 `filter()`**
✅ **Filtre une liste en fonction d’une condition**.

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6]
```

---

### **📌 `reduce()`**
✅ **Réduit une liste à une seule valeur** (ex. somme cumulée).

```python
from functools import reduce
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)  # 10
```
➡ **Pourquoi ?** Évite l’usage de **boucles explicites**.

---

## **🔹 6. Compréhensions de Listes et Générateurs**
### **📌 List Comprehensions**
✅ Alternative à `map()` et `filter()`.

```python
numbers = [1, 2, 3, 4]
squared = [x ** 2 for x in numbers]
print(squared)  # [1, 4, 9, 16]
```

### **📌 Générateurs (Lazy Evaluation)**
✅ **Utilisation efficace de la mémoire**.

```python
def count():
    num = 0
    while True:
        yield num
        num += 1

counter = count()
print(next(counter))  # 0
print(next(counter))  # 1
```
➡ **Pourquoi ?** Évite de stocker **toute la liste en mémoire**.

---

## **🔹 7. Recursion**
✅ **Définition** : Une fonction qui **s’appelle elle-même**.

```python
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

print(factorial(5))  # 120
```
➡ **Pourquoi ?** Permet de résoudre **des problèmes récursifs naturellement**.

---

## **📌 Conclusion**
Le **paradigme fonctionnel** en Python repose sur :
1️⃣ **Les fonctions de première classe**  
2️⃣ **Les fonctions pures et l'immutabilité**  
3️⃣ **Les fonctions d'ordre supérieur**  
4️⃣ **Les lambdas pour des expressions courtes**  
5️⃣ **Les transformations de données avec `map()`, `filter()`, `reduce()`**  
6️⃣ **Les compréhensions et générateurs pour une meilleure gestion de la mémoire**  
7️⃣ **La récursion**  

💡 **Python n’est pas un langage purement fonctionnel**, mais il permet **une approche mixte**, combinant POO et programmation fonctionnelle pour plus de flexibilité. 🚀