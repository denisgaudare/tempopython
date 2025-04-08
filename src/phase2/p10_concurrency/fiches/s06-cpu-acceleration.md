### **Optimiser un programme pour le CPU en Python**

Lorsqu’on veut **accélérer un programme**, on doit comprendre les **différentes approches d’optimisation CPU** en Python :
- **CPU synchrone** (exécution séquentielle)
- **CPU avec threading** (exécution pseudo-concurrente avec le GIL)
- **CPU asynchrone** (exécution non-bloquante avec `asyncio`)
- **Multiprocessing** (vrai parallélisme en contournant le GIL)

---

# **1. CPU Synchrone : Exécution Séquentielle**
C’est la méthode de base en Python : une seule tâche s’exécute à la fois sur un seul cœur du CPU.

### **Exemple : Calcul intensif (sans optimisation)**
```python
import time

def calcul_intensif(n):
    print(f"Calcul en cours pour {n}...")
    total = sum(i * i for i in range(n))
    print(f"Fin du calcul pour {n}")
    return total

start = time.time()
calcul_intensif(10**7)
calcul_intensif(10**7)
end = time.time()

print(f"Temps total : {end - start:.2f} secondes")
```
📌 **Problème** : Chaque tâche est exécutée l’une après l’autre, ce qui est lent.

---

# **2. CPU avec Threading : Exécution concurrente (pseudo-parallélisme)**
Python utilise le **GIL (Global Interpreter Lock)**, qui empêche les threads d’utiliser plusieurs cœurs **en parallèle** pour les tâches CPU-intensives.

👉 **Threading est utile pour les opérations d’E/S (ex: téléchargements, requêtes réseau)** mais pas pour **les calculs lourds**.

### **Exemple : Threading inefficace pour le CPU**
```python
import threading
import time

def calcul_intensif(n):
    print(f"Thread {threading.current_thread().name} en cours...")
    total = sum(i * i for i in range(n))
    print(f"Thread {threading.current_thread().name} terminé")
    return total

start = time.time()
t1 = threading.Thread(target=calcul_intensif, args=(10**7,))
t2 = threading.Thread(target=calcul_intensif, args=(10**7,))

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()
print(f"Temps total avec threads : {end - start:.2f} secondes")
```
📌 **Résultat :** Pas d’accélération, car **les threads sont bloqués par le GIL**.

### **Quand utiliser `threading` ?**
✅ Pour les **opérations d’E/S** (lecture/écriture de fichiers, appels API)  
❌ Pas efficace pour les **calculs lourds en CPU**

---

# **3. CPU Asynchrone : Exécution non bloquante (`asyncio`)**
L'**asynchronisme** en Python repose sur **un seul thread** qui gère plusieurs tâches sans bloquer l’exécution.

👉 **Efficace pour les tâches d’E/S, mais pas pour le CPU !**

### **Exemple : Asynchronisme inutile pour le CPU**
```python
import asyncio
import time

async def calcul_intensif(n):
    print(f"Tâche {n} démarrée...")
    total = sum(i * i for i in range(n))
    print(f"Tâche {n} terminée")
    return total

async def main():
    start = time.time()
    await asyncio.gather(calcul_intensif(10**7), calcul_intensif(10**7))
    end = time.time()
    print(f"Temps total avec asyncio : {end - start:.2f} secondes")

asyncio.run(main())
```
📌 **Résultat :** Aucune accélération car **`asyncio` ne contourne pas le GIL**.

### **Quand utiliser `asyncio` ?**
✅ Pour les **opérations d’E/S** (appels API, téléchargements, requêtes DB)  
❌ Pas efficace pour les **calculs lourds en CPU**  

---

# **4. Multiprocessing : Vrai parallélisme CPU**
La **solution pour accélérer un programme CPU-intensif en Python** est d’utiliser **`multiprocessing`**, qui **crée plusieurs processus** (chacun avec son propre GIL).

👉 **Permet d’utiliser plusieurs cœurs du CPU en parallèle.**

### **Exemple : Accélération avec `multiprocessing`**
```python
import multiprocessing
import time

def calcul_intensif(n):
    print(f"Process {multiprocessing.current_process().name} en cours...")
    total = sum(i * i for i in range(n))
    print(f"Process {multiprocessing.current_process().name} terminé")
    return total

if __name__ == "__main__":
    start = time.time()

    with multiprocessing.Pool(processes=2) as pool:
        pool.map(calcul_intensif, [10**7, 10**7])  # Exécute en parallèle

    end = time.time()
    print(f"Temps total avec multiprocessing : {end - start:.2f} secondes")
```
📌 **Résultat :** Temps réduit presque de moitié car **les calculs sont répartis sur plusieurs cœurs**.

### **Quand utiliser `multiprocessing` ?**
✅ Pour les **calculs lourds** nécessitant plusieurs cœurs  
❌ Moins efficace pour les **tâches I/O** (car chaque processus a sa propre mémoire)  

---

# **5. Comparaison des performances**
| Approche | Utilisation principale | Accélération pour le CPU ? | Quand l'utiliser ? |
|----------|--------------------|--------------------|----------------|
| **Synchrone** | Séquentiel, simple | ❌ Lent | Code simple sans besoin d'optimisation |
| **Threading** | Tâches d’E/S (réseau, fichiers) | ❌ Bloqué par le GIL | Appels API, lecture/écriture de fichiers |
| **Asyncio** | Tâches d’E/S (non bloquantes) | ❌ Pas pour le CPU | Web scraping, téléchargements |
| **Multiprocessing** | Calculs lourds (multi-cœurs) | ✅ Parallélisme réel | Machine Learning, calcul scientifique |

---

# **6. Cas pratique : Optimiser un programme réel**
**Problème** : Supposons que nous devons calculer la somme de carrés pour **4 grands nombres**.  
💡 **Objectif** : Comparer **synchrone vs multiprocessing**.

### **Code test avec `multiprocessing`**
```python
import multiprocessing
import time

def calcul_intensif(n):
    total = sum(i * i for i in range(n))
    return total

if __name__ == "__main__":
    n_values = [10**7, 10**7, 10**7, 10**7]

    start = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(calcul_intensif, n_values)  # Parallélisme

    end = time.time()
    print(f"Temps total multiprocessing : {end - start:.2f} secondes")
```
### **Code test synchrone (lenteur)**
```python
start = time.time()
for n in [10**7, 10**7, 10**7, 10**7]:
    calcul_intensif(n)
end = time.time()

print(f"Temps total séquentiel : {end - start:.2f} secondes")
```
📌 **Résultat attendu :**  
- **Multiprocessing** : ~2× plus rapide sur un CPU à 4 cœurs.  
- **Synchrone** : Temps total **beaucoup plus long**.

---

# **Conclusion**
- **Threading** et **asyncio** sont **inutiles pour les calculs CPU**.
- **Multiprocessing** est **la meilleure solution** pour exploiter **tous les cœurs du CPU**.
- **Toujours choisir la bonne approche selon la nature du programme**.

