## **Code Pythonique**

#### Du code plus court, elegant, efficace (on ne parle pas ici forcement de performance)

---

## **LISTES (`list`)**

### 1. **Création d'une liste à partir d'une autre avec une boucle**
#### ❌ Non-pythonic :
```python
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num ** 2)
```
#### ✅ Pythonic :
```python
squares = [num ** 2 for num in [1, 2, 3, 4, 5]]
```
---

### 2. **Suppression des doublons dans une liste**
#### ❌ Non-pythonic :
```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
```
#### ✅ Pythonic :
```python
unique_numbers = list(set(numbers))
```
---

### 3. **Fusionner plusieurs listes**
#### ❌ Non-pythonic :
```python
list1 = [1, 2]
list2 = [3, 4]
list3 = [5, 6]
merged = []
for lst in (list1, list2, list3):
    merged.extend(lst)
```
#### ✅ Pythonic :
```python
merged = list1 + list2 + list3  # Ou sum([list1, list2, list3], [])
```
---

### 4. **Trouver le maximum d'une liste**
#### ❌ Non-pythonic :
```python
numbers = [10, 20, 30, 40]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
```
#### ✅ Pythonic :
```python
max_num = max(numbers)
```
---

### 5. **Filtrage des éléments pairs**
#### ❌ Non-pythonic :
```python
numbers = [1, 2, 3, 4, 5, 6]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
```
#### ✅ Pythonic :
```python
evens = [num for num in numbers if num % 2 == 0]
```
---

## **TUPLES (`tuple`)**

### 6. **Échange de valeurs entre deux variables**
#### ❌ Non-pythonic :
```python
a = 1
b = 2
temp = a
a = b
b = temp
```
#### ✅ Pythonic :
```python
a, b = b, a
```
---

### 7. **Retourner plusieurs valeurs d'une fonction**
#### ❌ Non-pythonic :
```python
def get_point():
    x = 10
    y = 20
    return [x, y]  # Utilisation d'une liste au lieu d'un tuple
```
#### ✅ Pythonic :
```python
def get_point():
    return 10, 20  # Utilisation d'un tuple
```
---

### 8. **Déballage d'un tuple**
#### ❌ Non-pythonic :
```python
point = (10, 20)
x = point[0]
y = point[1]
```
#### ✅ Pythonic :
```python
x, y = (10, 20)
```
---

## **ENSEMBLES (`set`)**

### 9. **Suppression des doublons d'une liste en boucle**
#### ❌ Non-pythonic :
```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
```
#### ✅ Pythonic :
```python
unique_numbers = list(set(numbers))
```
---

### 10. **Intersection de deux ensembles**
#### ❌ Non-pythonic :
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
common = []
for item in set1:
    if item in set2:
        common.append(item)
```
#### ✅ Pythonic :
```python
common = set1 & set2
```
---

### 11. **Différence entre deux ensembles**
#### ❌ Non-pythonic :
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
difference = []
for item in set1:
    if item not in set2:
        difference.append(item)
```
#### ✅ Pythonic :
```python
difference = set1 - set2
```
---

## **DICTIONNAIRES (`dict`)**

### 12. **Création d'un dictionnaire à partir de deux listes**
#### ❌ Non-pythonic :
```python
keys = ["name", "age", "city"]
values = ["Alice", 25, "Paris"]
d = {}
for i in range(len(keys)):
    d[keys[i]] = values[i]
```
#### ✅ Pythonic :
```python
d = dict(zip(keys, values))
```
---

### 13. **Incrémentation sécurisée d'une clé**
#### ❌ Non-pythonic :
```python
counts = {}
word = "apple"
if word in counts:
    counts[word] += 1
else:
    counts[word] = 1
```
#### ✅ Pythonic :
```python
counts = {}
counts[word] = counts.get(word, 0) + 1
```
---

### 14. **Parcourir un dictionnaire avec `items()`**
#### ❌ Non-pythonic :
```python
d = {"name": "Alice", "age": 25}
for key in d:
    print(f"{key}: {d[key]}")
```
#### ✅ Pythonic :
```python
for key, value in d.items():
    print(f"{key}: {value}")
```
---

### 15. **Fusion de dictionnaires (Python 3.9+)**
#### ❌ Non-pythonic :
```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged = dict1.copy()
merged.update(dict2)
```
#### ✅ Pythonic :
```python
merged = {**dict1, **dict2}  # ou dict1 | dict2 en Python 3.9+
```
---

### 16. **Utilisation de `defaultdict` pour éviter des vérifications inutiles**
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
for word in words:
    counts[word] += 1
```
---

### 17. **Inversion d'un dictionnaire (clés <-> valeurs)**
#### ❌ Non-pythonic :
```python
d = {"a": 1, "b": 2, "c": 3}
inverse = {}
for key, value in d.items():
    inverse[value] = key
```
#### ✅ Pythonic :
```python
inverse = {v: k for k, v in d.items()}
```
