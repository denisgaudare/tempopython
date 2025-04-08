# ✅ Code **CPU plus optimisé**,

## ⚡ Version optimisée en O(n²)

```python
def find_zero_sum_triplets_optimized(arr):
    arr.sort()  # tri initial : O(n log n)
    n = len(arr)
    triplets = set()

    for i in range(n - 2):
        # Évite les doublons
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        a = arr[i]
        left = i + 1
        right = n - 1

        while left < right:
            total = a + arr[left] + arr[right]

            if total == 0:
                triplets.add((a, arr[left], arr[right]))
                left += 1
                right -= 1
                # Skip doublons
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return list(triplets)
```

---

## 🧪 Utilisation avec mesure de temps

```python
import random
import time

data = [random.randint(-100, 100) for _ in range(500)]

start = time.perf_counter()
result = find_zero_sum_triplets_optimized(data)
end = time.perf_counter()

print(f"{len(result)} triplets trouvés en {end - start:.4f} secondes.")
```

---

## ⚙️ Comparaison de complexité

| Version                | Complexité  | Temps estimé (`n = 500`) |
|------------------------|-------------|---------------------------|
| Brute-force `O(n³)`    | Très lent   | ~30s selon la machine     |
| Optimisée `O(n²)`      | Beaucoup + rapide | < 1s                    |

---

## ✅ Pourquoi cette version est meilleure :
- Elle **évite les boucles imbriquées triples**
- Elle **utilise le tri** pour naviguer avec deux pointeurs (`left`, `right`)
- Elle **élimine les doublons** dans les résultats via un `set`

---