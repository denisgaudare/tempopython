# ✅ **10 petits challenges python ** à compléter, chacun avec :

- Un **énoncé clair**  
- Un **squelette de code avec un `# TODO`**
- Une **solution élégante et pythonique** proposée en-dessous

---

## 🧩 1. Supprimer les doublons tout en gardant l’ordre

```python
def remove_duplicates(seq):
    # TODO: Supprimer les doublons tout en conservant l'ordre d'apparition
    pass
```

✅ **Solution élégante** :

```python
def remove_duplicates(seq):
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]
```

---

## 🧩 2. Trouver l’élément le plus fréquent dans une liste

```python
from collections import Counter

def most_frequent(lst):
    # TODO: Retourner l'élément avec la plus haute fréquence
    pass
```

✅ **Solution élégante** :

```python
def most_frequent(lst):
    return Counter(lst).most_common(1)[0][0]
```

---

## 🧩 3. Calculer la somme des n plus grands éléments d’une liste

```python
def top_n_sum(lst, n):
    # TODO: Retourner la somme des n plus grands éléments
    pass
```

✅ **Solution élégante** :

```python
import heapq

def top_n_sum(lst, n):
    return sum(heapq.nlargest(n, lst))
```

---

## 🧩 4. Vérifier si une chaîne est un palindrome (en ignorant la casse et les espaces)

```python
def is_palindrome(s):
    # TODO: Vérifier si s est un palindrome (ignorer espaces et casse)
    pass
```

✅ **Solution élégante** :

```python
def is_palindrome(s):
    s = ''.join(s.lower().split())
    return s == s[::-1]
```

---

## 🧩 5. Aplatir une liste de listes de manière récursive

```python
def flatten(lst):
    # TODO: Aplatir une liste contenant potentiellement des listes imbriquées
    pass
```

✅ **Solution élégante** :

```python
def flatten(lst):
    for x in lst:
        if isinstance(x, list):
            yield from flatten(x)
        else:
            yield x
```

---

## 🧩 6. Regrouper les mots anagrammes ensemble

```python
from collections import defaultdict

def group_anagrams(words):
    # TODO: Grouper les mots anagrammes ensemble
    pass
```

✅ **Solution élégante** :

```python
from collections import defaultdict

def group_anagrams(words):
    d = defaultdict(list)
    for word in words:
        d[''.join(sorted(word))].append(word)
    return list(d.values())
```

---

## 🧩 7. Fusionner deux listes triées (comme dans merge sort)

```python
def merge_sorted(l1, l2):
    # TODO: Fusionner deux listes triées sans les trier de nouveau
    pass
```

✅ **Solution élégante** :

```python
def merge_sorted(l1, l2):
    from heapq import merge
    return list(merge(l1, l2))
```

---

## 🧩 8. Trouver le plus long mot dans une phrase

```python
def longest_word(sentence):
    # TODO: Retourner le mot le plus long d'une phrase
    pass
```

✅ **Solution élégante** :

```python
def longest_word(sentence):
    return max(sentence.split(), key=len)
```

---

## 🧩 9. Créer un histogramme des fréquences de caractères

```python
def char_histogram(s):
    # TODO: Retourner un dictionnaire des fréquences de chaque caractère
    pass
```

✅ **Solution élégante** :

```python
from collections import Counter

def char_histogram(s):
    return dict(Counter(s))
```

---

## 🧩 10. Trouver tous les indices d’un élément dans une liste

```python
def all_indices(lst, value):
    # TODO: Retourner tous les indices de 'value' dans lst
    pass
```

✅ **Solution élégante** :

```python
def all_indices(lst, value):
    return [i for i, x in enumerate(lst) if x == value]
```
