# ✅ Code **CPU-intensif**,

### 🧩 **Recherche de triplets dans un tableau qui satisfont une condition**

Ce code recherche tous les **triplets `(a, b, c)`** dans un tableau tel que :  
```a + b + c == 0```

C'est un problème classique (sous-optimal ici volontairement) qui peut rapidement devenir **coûteux en CPU** à cause de sa complexité en **O(n³)**.

---

### 🧠 Code (volontairement non optimisé)

```python
import random

def find_zero_sum_triplets(arr):
    n = len(arr)
    triplets = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplets.append((arr[i], arr[j], arr[k]))
    return triplets

# Génère un tableau de 500 éléments aléatoires entre -100 et 100
data = [random.randint(-100, 100) for _ in range(500)]

result = find_zero_sum_triplets(data)
print(f"{len(result)} triplets trouvés.")
```

---

### 🔥 Pourquoi ce code est bien pour tester le CPU :

- Il a une **complexité cubique** → explosion des boucles
- La logique n’est **pas triviale** (comparaison, arithmétique)
- Tu peux jouer sur `range(500)` → intensité contrôlable
- Tu peux ensuite l’optimiser via :
  - utilisation de `set` pour éviter des doublons
  - réduction à O(n²) avec tri préalable
  - parallélisation (`multiprocessing`)

---

### 💡 Bonus : Mesure du temps d'exécution

Ajoute ce bloc pour mesurer la durée :

```python
import time

start = time.perf_counter()
result = find_zero_sum_triplets(data)
end = time.perf_counter()

print(f"{len(result)} triplets trouvés en {end - start:.2f} secondes.")
```

---
