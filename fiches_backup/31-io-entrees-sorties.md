# **Entrées/Sorties (I/O) en Python : Synchrone, avec Threads, et Asynchrone**
---
## **1. Introduction aux I/O en Python**
Les entrées/sorties (**I/O**) en Python concernent :
- **Lecture et écriture dans des fichiers**
- **Réseau (HTTP, WebSockets, Bases de données, etc.)**
- **Accès à des périphériques externes (clavier, écran, disque, etc.)**

### **Types d'I/O en Python**
| Type d'I/O | Explication | Avantages | Inconvénients |
|------------|------------|-----------|--------------|
| **Synchrone (bloquant)** | Chaque opération attend la fin de la précédente | Simple à comprendre | Ralentit l'exécution en cas d'attente longue |
| **Threading (I/O parallèle avec plusieurs threads)** | Plusieurs tâches peuvent avancer en parallèle | Utilise plusieurs threads | Problèmes de concurrence et gestion complexe |
| **Asynchrone (avec `asyncio`)** | Les opérations I/O sont gérées via une boucle d’événements | Très efficace pour de nombreuses requêtes I/O | Nécessite une nouvelle approche de programmation |

---

## **2. I/O Synchrone en Python (Bloquant)**
C'est l'approche **classique** : chaque tâche attend la fin de l'opération précédente.

### **Exemple : Lecture et écriture de fichier**
```python
import time

def lecture_fichier():
    print("Lecture du fichier en cours...")
    time.sleep(2)  # Simule un I/O bloquant
    with open("exemple.txt", "r") as f:
        return f.read()

def ecriture_fichier(contenu):
    print("Écriture dans le fichier...")
    time.sleep(2)  # Simule un I/O bloquant
    with open("exemple.txt", "w") as f:
        f.write(contenu)

# Exécution séquentielle (bloquante)
print("Début...")
ecriture_fichier("Bonjour")
contenu = lecture_fichier()
print("Contenu :", contenu)
print("Fin.")
```
### **Problèmes**
- **Attente longue** : Si une opération dure 2 secondes, on doit attendre avant de passer à la suivante.
- **Peu efficace pour des tâches multiples**.

---

## **3. I/O avec Threads (Parallélisme)**
L’utilisation de **`threading`** permet de **ne pas bloquer le programme principal**, en exécutant des opérations en parallèle.

### **Exemple : Threading pour l’I/O**
```python
import threading
import time

def lecture_fichier():
    print("Lecture du fichier en cours...")
    time.sleep(2)
    with open("exemple.txt", "r") as f:
        print("Contenu lu :", f.read())

def ecriture_fichier():
    print("Écriture dans le fichier...")
    time.sleep(2)
    with open("exemple.txt", "w") as f:
        f.write("Bonjour")

# Création de threads
thread1 = threading.Thread(target=ecriture_fichier)
thread2 = threading.Thread(target=lecture_fichier)

print("Début...")
thread1.start()  # Démarrer l'écriture
thread2.start()  # Démarrer la lecture en parallèle

thread1.join()  # Attendre la fin du thread 1
thread2.join()  # Attendre la fin du thread 2
print("Fin.")
```
### **Pourquoi c’est mieux ?**
✅ **Les opérations ne bloquent pas tout le programme**  
✅ **Utile si on a plusieurs fichiers ou requêtes réseau à traiter**  
❌ **Pas adapté pour du calcul lourd (GIL de Python)**  
❌ **Complexité accrue avec la synchronisation des threads (risques de race conditions)**  

---

## **4. I/O Asynchrone avec `asyncio`**
L’approche **asynchrone** repose sur une **boucle d’événements** qui exécute des tâches sans bloquer le programme.

### **Exemple : Utilisation d'`asyncio` pour des I/O**
```python
import asyncio

async def lecture_fichier():
    print("Lecture en cours...")
    await asyncio.sleep(2)  # Simule un I/O asynchrone
    with open("exemple.txt", "r") as f:
        print("Contenu lu :", f.read())

async def ecriture_fichier():
    print("Écriture en cours...")
    await asyncio.sleep(2)  # Simule un I/O asynchrone
    with open("exemple.txt", "w") as f:
        f.write("Bonjour")

async def main():
    task1 = asyncio.create_task(ecriture_fichier())  # Démarrer l'écriture
    task2 = asyncio.create_task(lecture_fichier())  # Démarrer la lecture

    await task1  # Attendre la fin de l'écriture
    await task2  # Attendre la fin de la lecture

print("Début...")
asyncio.run(main())  # Exécute la boucle d'événements asyncio
print("Fin.")
```
### **Pourquoi c’est mieux ?**
✅ **Les tâches ne bloquent pas le programme**  
✅ **Optimisé pour les I/O lourds (réseau, base de données, fichiers, etc.)**  
❌ **Pas naturel pour les débutants (différent des threads traditionnels)**  
❌ **Nécessite une bibliothèque compatible async (ex: `aiohttp` pour HTTP)**  

---

## **5. Comparaison entre les trois méthodes**
| Méthode | Adapté pour | Bloquant ? | Complexité |
|---------|------------|------------|------------|
| **I/O Synchrone** | Petites tâches I/O (fichiers, simple HTTP) | Oui | Faible |
| **I/O avec Threads** | Paralléliser des tâches sans blocage (fichiers multiples) | Non | Moyenne |
| **I/O Asynchrone (`asyncio`)** | Réseau, API, WebSockets, Base de données | Non | Élevée |

---

## **6. Exemple complet avec une API HTTP**
### **1️⃣ Version Synchrone (Bloquante)**
```python
import requests
import time

def fetch_data():
    print("Requête en cours...")
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print("Réponse reçue :", response.json())

print("Début...")
fetch_data()
print("Fin.")
```
**Problème** : Chaque requête HTTP bloque tout le programme.

---

### **2️⃣ Version avec Threading**
```python
import requests
import threading

def fetch_data():
    print("Requête en cours...")
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print("Réponse reçue :", response.json())

thread = threading.Thread(target=fetch_data)
print("Début...")
thread.start()
thread.join()  # Attendre la fin du thread
print("Fin.")
```
**Avantage** : D'autres tâches peuvent continuer pendant que la requête est en cours.

---

### **3️⃣ Version Asynchrone avec `aiohttp`**
```python
import aiohttp
import asyncio

async def fetch_data():
    print("Requête en cours...")
    async with aiohttp.ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/todos/1") as response:
            data = await response.json()
            print("Réponse reçue :", data)

async def main():
    await fetch_data()

print("Début...")
asyncio.run(main())
print("Fin.")
```
**Avantage** : Peut gérer **des centaines de requêtes HTTP en parallèle** sans bloquer le programme.

---

## **Conclusion**
1. **I/O Synchrone** = Simple mais bloquant.  
2. **Threading** = Permet le parallèle, mais plus complexe.  
3. **Asyncio** = Parfait pour les I/O lourds (réseau, API, DB).  

**🚀 Conseil** : Utilise `asyncio` pour les I/O modernes comme les requêtes API, bases de données, WebSockets !