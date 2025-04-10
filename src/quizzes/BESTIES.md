# ✅ **Quelques problèmes classiques** 

---

## 🐌 VS ⚡️ 1. Fibonacci (récursif)

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
    pass
```

✅ **Optimiser en ajouter au maximum 2 lignes** :

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

---

## 🐌 VS ⚡️ 2. Somme des paires qui font une cible (two-sum)

```python
def has_pair_with_sum(lst, target):
    # TODO: Vérifier s'il existe une paire d'entiers dont la somme vaut target
    pass
```

✅ **Optimisé ** :

```python
def has_pair_with_sum(lst, target):
    seen = set()
    for x in lst:
        if target - x in seen:
            return True
        seen.add(x)
    return False
```

---

## 🐌 VS ⚡️ 3. Intersection de deux listes très longues

```python
def intersection(a, b):
    # TODO: Retourner les éléments communs aux deux listes
    pass
```

✅ **Optimisé** :

```python
def intersection(a, b):
    return list(set(a) & set(b))
```

---

## 🐌 VS ⚡️ 4. Trouver tous les doublons dans une très grande liste

```python
def find_duplicates(lst):
    # TODO: Retourner les éléments apparaissant plus d'une fois
    pass
```

✅ **Optimisé (Counter)** :

```python
from collections import Counter

def find_duplicates(lst):
    return [item for item, count in Counter(lst).items() if count > 1]
```

---

## 🐌 VS ⚡️ 5. Produit de tous les éléments sauf le courant (sans division)

```python
def product_except_self(nums):
    # TODO: Retourner la liste des produits sauf à l’indice i
    pass
```

✅ **Optimisé (pré-calcul)** :

```python
def product_except_self(nums):
    n = len(nums)
    left, right = [1]*n, [1]*n
    for i in range(1, n):
        left[i] = left[i-1] * nums[i-1]
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]
    return [l*r for l, r in zip(left, right)]
```

---

## 🐌 VS ⚡️ 6. Détecter un cycle dans une liste chaînée (sans `set`)

```python
def has_cycle(head):
    # TODO: Détection d’un cycle dans une liste chaînée
    pass
```

✅ **Optimisé (Tortoise & Hare)** :

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

---

## 🐌 VS ⚡️ 7. Calculer la puissance d’un nombre (xⁿ) sans boucle naïve

```python
def power(x, n):
    # TODO: Implémenter x^n efficacement
    pass
```

✅ **Optimisé (exponentiation rapide)** :

```python
def power(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return power(x * x, n // 2)
    return x * power(x, n - 1)
```

---

## 🐌 VS ⚡️ 8. Plus grand rectangle dans un histogramme (naïf = O(n²))

```python
def largest_rectangle(hist):
    # TODO: Trouver la plus grande aire dans un histogramme
    pass
```

✅ **Optimisé (stack, O(n))** :

```python
def largest_rectangle(hist):
    stack, max_area = [], 0
    hist.append(0)
    for i, h in enumerate(hist):
        while stack and hist[stack[-1]] > h:
            height = hist[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area
```

---

## 🐌 VS ⚡️ 9. Longest substring without repeating characters

```python
def longest_unique_substring(s):
    # TODO: Trouver la plus longue sous-chaîne sans répétition
    pass
```

✅ **Optimisé (sliding window)** :

```python
def longest_unique_substring(s):
    seen = {}
    start = max_len = 0
    for i, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = i
        max_len = max(max_len, i - start + 1)
    return max_len
```

---

## 🐌 VS ⚡️ 10. Trier presque trié (chaque élément à ±k de sa place)

```python
def sort_nearly_sorted(arr, k):
    # TODO: Trier un tableau presque trié (k-disorder)
    pass
```

✅ **Optimisé (heap)** :

```python
import heapq

def sort_nearly_sorted(arr, k):
    heap, result = [], []
    for i in range(len(arr)):
        if i > k:
            result.append(heapq.heappop(heap))
        heapq.heappush(heap, arr[i])
    while heap:
        result.append(heapq.heappop(heap))
    return result
```

---
