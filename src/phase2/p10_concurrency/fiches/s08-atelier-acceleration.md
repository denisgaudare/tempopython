### **Atelier : Accélération de Calcul Intensif avec Modèle Objet en Python**

🚀 **Objectif :** Comparer l'exécution **séquentielle, multithread, multiprocessing et optimisée (Numba)** sur un problème de calcul CPU-intensif.  
📌 **Concepts abordés :**  
✅ Modèle Objet Python (`class`)  
✅ Différents modèles d'exécution (`threading`, `multiprocessing`, `numba`)  
✅ Mesure de performance (`time.time()`)  

---

## **🔹 Sujet du TD : Simulation de croissance d’une population bactérienne**
Nous allons créer une classe `PopulationBacterienne` qui :  
1. Simule la croissance d’une colonie de bactéries sur `N` itérations.  
2. Calcule l'évolution avec une fonction de croissance exponentielle.  
3. Compare **différentes méthodes d'exécution**.

---

## **1️⃣ Partie 1 : Version Séquentielle (Non Optimisée)**
### **💡 Objectif : Faire le calcul avec une seule boucle Python**
```python
import time

class PopulationBacterienne:
    def __init__(self, taille_initiale, facteur_croissance, iterations):
        self.taille = taille_initiale
        self.facteur = facteur_croissance
        self.iterations = iterations

    def calculer_croissance(self):
        """Calcule la croissance bactérienne séquentiellement"""
        population = self.taille
        for _ in range(self.iterations):
            population *= self.facteur  # Croissance exponentielle
        return population

# TEST - Exécution séquentielle
pop = PopulationBacterienne(1000, 1.01, 10**7)
start = time.time()
resultat = pop.calculer_croissance()
end = time.time()

print(f"Résultat : {resultat:.2f}")
print(f"Temps séquentiel : {end - start:.2f} secondes")
```
📌 **Problème :** Cette version est **lente** car tout est exécuté **séquentiellement** dans une seule boucle.

---

## **2️⃣ Partie 2 : Version avec `Threading` (Inefficace pour le CPU)**
### **💡 Objectif : Lancer plusieurs threads pour faire les calculs**
```python
import threading

class PopulationThread(threading.Thread):
    def __init__(self, taille, facteur, iterations):
        threading.Thread.__init__(self)
        self.taille = taille
        self.facteur = facteur
        self.iterations = iterations
        self.resultat = None

    def run(self):
        population = self.taille
        for _ in range(self.iterations):
            population *= self.facteur
        self.resultat = population

# TEST - Exécution avec threads
start = time.time()
threads = [PopulationThread(1000, 1.01, 10**7) for _ in range(2)]

for t in threads:
    t.start()
for t in threads:
    t.join()

end = time.time()
print(f"Temps avec threading : {end - start:.2f} secondes")
```
📌 **Résultat :** Pas d’accélération car **le GIL bloque les threads Python sur un seul cœur**.

---

## **3️⃣ Partie 3 : Version `Multiprocessing` (Optimisée pour CPU)**
### **💡 Objectif : Exécuter les calculs en parallèle sur plusieurs cœurs du CPU**
```python
import multiprocessing

class PopulationProcess(multiprocessing.Process):
    def __init__(self, taille, facteur, iterations, queue):
        multiprocessing.Process.__init__(self)
        self.taille = taille
        self.facteur = facteur
        self.iterations = iterations
        self.queue = queue  # Permet de récupérer les résultats

    def run(self):
        population = self.taille
        for _ in range(self.iterations):
            population *= self.facteur
        self.queue.put(population)  # Envoie le résultat au processus principal

# TEST - Exécution en parallèle
if __name__ == "__main__":
    start = time.time()
    queue = multiprocessing.Queue()
    processes = [PopulationProcess(1000, 1.01, 10**7, queue) for _ in range(2)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    results = [queue.get() for _ in processes]  # Récupération des résultats
    end = time.time()
    
    print(f"Temps avec multiprocessing : {end - start:.2f} secondes")
```
📌 **Résultat :** 🚀 **Beaucoup plus rapide** car **chaque processus utilise un cœur différent du CPU**.

---

## **4️⃣ Partie 4 : Version `Numba` (Optimisation Ultime)**
### **💡 Objectif : Compiler le calcul en C pour éviter le GIL**
```python
from numba import jit, prange

class PopulationBacterienneOptimisee:
    def __init__(self, taille_initiale, facteur_croissance, iterations):
        self.taille = taille_initiale
        self.facteur = facteur_croissance
        self.iterations = iterations

    @jit(nopython=True, parallel=True)  # Compilation en C
    def calculer_croissance(self):
        population = self.taille
        for _ in prange(self.iterations):  # Exécution optimisée sur plusieurs cœurs
            population *= self.facteur
        return population

# TEST - Exécution avec Numba
pop = PopulationBacterienneOptimisee(1000, 1.01, 10**7)
start = time.time()
resultat = pop.calculer_croissance()
end = time.time()

print(f"Temps avec Numba : {end - start:.2f} secondes")
```
📌 **Résultat :** 🚀 **Encore plus rapide** car **Numba compile le code en C et utilise plusieurs cœurs**.

---

## **🔹 Comparaison des performances**
| Version | Temps d'exécution | Accélération |
|---------|-----------------|--------------|
| **Séquentielle (non optimisée)** | ~5-10 sec | 🚫 Aucune |
| **Threading** | ~5-10 sec | 🚫 Bloqué par le GIL |
| **Multiprocessing** | ~2-5 sec | ✅ Multi-cœurs |
| **Numba (compilation en C)** | ~0.5-1 sec | 🚀 **Ultra rapide !** |

---

## **🔹 Conclusion**
🚀 **Comment accélérer du calcul intensif ?**  
1️⃣ **Ne pas utiliser `threading` pour les tâches CPU** (car bloqué par le GIL).  
2️⃣ **Utiliser `multiprocessing`** si on veut exécuter sur **plusieurs cœurs du CPU**.  
3️⃣ **Utiliser `Numba`** pour **compiler le code en C et exploiter le multi-threading natif**.  

**🎯 Exercices pour s'entraîner :**
1. Modifier les classes pour gérer **4 processus au lieu de 2**.
2. Tester avec une **valeur de croissance plus faible** (`1.001` au lieu de `1.01`).
3. Modifier `Numba` pour **retourner un tableau d’évolution** et non une seule valeur.