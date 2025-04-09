## **Code Pythonique**

#### Du code plus court, elegant, efficace (on ne parle pas ici forcement de performance)

---

### 1. **Itération sur une liste**
#### ❌ Non-pythonic :
```python
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i])
```
#### ✅ Pythonic :
```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
```
---

### 2. **Utilisation de `range(len(...))` au lieu de `enumerate()`**
#### ❌ Non-pythonic :
```python
items = ['a', 'b', 'c']
for i in range(len(items)):
    print(f"Index {i}: {items[i]}")
```
#### ✅ Pythonic :
```python
items = ['a', 'b', 'c']
for i, item in enumerate(items):
    print(f"Index {i}: {item}")
```
---

### 3. **Construction d'une liste avec `append()` au lieu de la compréhension de liste**
#### ❌ Non-pythonic :
```python
squares = []
for x in range(10):
    squares.append(x ** 2)
```
#### ✅ Pythonic :
```python
squares = [x ** 2 for x in range(10)]
```
---

### 4. **Utilisation inefficace de `if` pour attribuer une valeur**
#### ❌ Non-pythonic :
```python
x = 10
if x > 5:
    category = "big"
else:
    category = "small"
```
#### ✅ Pythonic :
```python
x = 10
category = "big" if x > 5 else "small"
```
---

### 5. **Suppression des doublons avec une boucle au lieu d'un set**
#### ❌ Non-pythonic :
```python
unique_items = []
items = [1, 2, 2, 3, 4, 4, 5]

for item in items:
    if item not in unique_items:
        unique_items.append(item)
```
#### ✅ Pythonic :
```python
items = [1, 2, 2, 3, 4, 4, 5]
unique_items = list(set(items))
```
---

### 6. **Concaténation de chaînes avec `+` au lieu de `join()`**
#### ❌ Non-pythonic :
```python
words = ["Hello", "World", "!"]
sentence = ""
for word in words:
    sentence += word + " "
sentence = sentence.strip()
```
#### ✅ Pythonic :
```python
words = ["Hello", "World", "!"]
sentence = " ".join(words)
```
---

### 7. **Utilisation de `try-except` pour vérifier la présence d'une clé dans un dictionnaire**
#### ❌ Non-pythonic :
```python
data = {"name": "Alice", "age": 25}
if "age" in data:
    age = data["age"]
else:
    age = None
```
#### ✅ Pythonic :
```python
data = {"name": "Alice", "age": 25}
age = data.get("age")
```
---

### 8. **Échange de valeurs avec une variable temporaire inutile**
#### ❌ Non-pythonic :
```python
a = 5
b = 10
temp = a
a = b
b = temp
```
#### ✅ Pythonic :
```python
a, b = 10, 5
```
---

### 9. **Vérification de nullité en comparant directement à `None`**
#### ❌ Non-pythonic :
```python
if variable == None:
    pass
```
#### ✅ Pythonic :
```python
if variable is None:
    pass
```
---

### 10. **Utilisation de `map()` au lieu d'une boucle classique**
#### ❌ Non-pythonic :
```python
numbers = [1, 2, 3, 4]
doubled = []
for num in numbers:
    doubled.append(num * 2)
```
#### ✅ Pythonic :
```python
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))  # Ou [x * 2 for x in numbers]
```
---

### 11. **Utilisation de `zip()` au lieu d'une boucle avec index**
#### ❌ Non-pythonic :
```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for i in range(len(names)):
    print(f"{names[i]} has {ages[i]} years old")
```
#### ✅ Pythonic :
```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} has {age} years old")
```
---

### 12. **Vérification de la présence dans une liste au lieu d'un set**
#### ❌ Non-pythonic :
```python
names = ["Alice", "Bob", "Charlie"]
if "Alice" in names:
    print("Found!")
```
#### ✅ Pythonic :
```python
names = {"Alice", "Bob", "Charlie"}  # Utilisation d'un set pour une recherche rapide
if "Alice" in names:
    print("Found!")
```
---

### 13. **Utilisation de `defaultdict` pour éviter des vérifications inutiles**
#### ❌ Non-pythonic :
```python
counts = {}
words = ["apple", "banana", "apple", "orange"]

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
```
#### ✅ Pythonic :
```python
from collections import defaultdict

counts = defaultdict(int)
words = ["apple", "banana", "apple", "orange"]

for word in words:
    counts[word] += 1
```
---

Tous ces exemples montrent comment rendre le code plus lisible, efficace et concis en utilisant les fonctionnalités idiomatiques de Python.