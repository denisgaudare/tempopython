# ✅ **10 petits challenges Python ** à compléter, chacun avec :

---

## 🧩 1. Supprimer les doublons tout en gardant l’ordre

```python
def remove_duplicates(seq):
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]    # TODO: Supprimer les doublons tout en conservant l'ordre d'apparition
```
---

## 🧩 2. Trouver l’élément le plus fréquent dans une liste

```python
def most_frequent(lst):
    return Counter(lst)
    # TODO: Retourner l'élément avec la plus haute fréquence
    pass
```
---

## 🧩 3. Calculer la somme des n plus grands éléments d’une liste

```python
def top_n_sum(lst, n):
    # TODO: Retourner la somme des n plus grands éléments
    pass
```
---

## 🧩 4. Vérifier si une chaîne est un palindrome (en ignorant la casse et les espaces)
## TRIVIAL .... (Falculatif)
```python
def is_palindrome(s):
    # TODO: Vérifier si s est un palindrome (ignorer espaces et casse)
    pass
```

---

## 🧩 5. Aplatir une liste de listes de manière récursive

```python
def flatten(lst):
    # TODO: Aplatir une liste contenant potentiellement des listes imbriquées
    pass
```

---

## 🧩 6. Regrouper les mots anagrammes ensemble

```python
from collections import defaultdict

def group_anagrams(words):
    # TODO: Grouper les mots anagrammes ensemble
    pass
```
---

## 🧩 7. Fusionner deux listes triées (comme dans merge sort)

```python
def merge_sorted(l1, l2):
    # TODO: Fusionner deux listes triées sans les trier de nouveau
    pass
```

---

## 🧩 8. Trouver le plus long mot dans une phrase

```python
def longest_word(sentence):
    # TODO: Retourner le mot le plus long d'une phrase
    pass
```

---

## 🧩 9. Créer un histogramme des fréquences de caractères

```python
def char_histogram(s):
    # TODO: Retourner un dictionnaire des fréquences de chaque caractère
    pass
```

---

## 🧩 10. Trouver tous les indices d’un élément dans une liste

```python
def all_indices(lst, value):
    # TODO: Retourner tous les indices de 'value' dans lst
    pass
```

