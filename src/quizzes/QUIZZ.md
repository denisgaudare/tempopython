# ✅ **20 questions , 4 propositions chacune**

---

## 🧠 QCM Python Avancé – 20 Questions

### 1. Que se passe-t-il lorsqu’on modifie un objet mutable passé à une fonction ?
A. L’objet original est copié  
B. L’objet original est modifié  
C. L’objet devient immutable  
D. Python crée un nouvel objet automatiquement  

---

### 2. Quelle est la différence entre `is` et `==` ?
A. `is` compare les valeurs, `==` les identités  
B. `is` compare les identités, `==` les valeurs  
C. Aucun  
D. Les deux sont interchangeables  

---

### 3. À quoi sert `@staticmethod` ?
A. À créer une fonction privée  
B. À créer une méthode d’instance  
C. À définir une méthode indépendante de l'instance  
D. À créer une méthode liée à la classe  

---

### 4. Comment fonctionne le ramasse-miettes (garbage collector) ?
A. Il détruit les objets dès leur non-utilisation  
B. Il utilise uniquement le comptage de références  
C. Il combine comptage de références et détection de cycles  
D. Il est désactivé par défaut  

---

### 5. Que fait ce code : `def f(x=[]): ...` ?
A. Rien d’anormal  
B. Crée une nouvelle liste à chaque appel  
C. Réutilise la même liste à chaque appel  
D. Lève une exception  

---

### 6. Quel outil pour profiler la mémoire ?
A. `timeit`  
B. `gc.collect()`  
C. `tracemalloc`  
D. `line_profiler`  

---

### 7. Complexité de recherche dans un `set` ?
A. O(n)  
B. O(1)  
C. O(log n)  
D. O(n log n)  

---

### 8. Différence entre liste en compréhension et générateur ?
A. Aucun  
B. Le générateur est plus rapide mais plus gourmand  
C. Le générateur ne calcule les valeurs qu’à la demande  
D. Le générateur retourne toujours une liste  

---

### 9. Pourquoi `list.remove()` est lent sur de grandes listes ?
A. C’est une opération O(1)  
B. Il supprime plusieurs éléments à la fois  
C. Il recherche d’abord la valeur, puis déplace les éléments  
D. Ce n’est pas lent  

---

### 10. Que fait `a = a + b` avec deux listes ?
A. Modifie `a` en place  
B. Alloue une nouvelle liste  
C. Lance une erreur  
D. Applique `append` sur `b`  

---

### 11. Que sont les descripteurs ?
A. Des décorateurs spéciaux  
B. Des objets qui contrôlent l’accès aux attributs  
C. Des fonctions cachées  
D. Des méthodes d’importation  

---

### 12. Qu’est-ce qu’une *metaclass* ?
A. Une classe qui hérite d’une autre classe  
B. Une classe utilisée pour créer des modules  
C. Une classe qui fabrique des classes  
D. Un type d’attribut  

---

### 13. Que retourne `dir()` ?
A. Les attributs définis par l’utilisateur  
B. Les attributs accessibles de l’objet  
C. La mémoire de l’objet  
D. L'arborescence du système de fichiers  

---

### 14. À quoi sert l’opérateur `:=` (walrus operator) ?
A. À définir une fonction anonyme  
B. À imbriquer des assignations  
C. À faire une affectation dans une expression  
D. À concaténer des chaînes  

---

### 15. Différence entre `yield` et `yield from` ?
A. `yield from` permet de déléguer à un sous-générateur  
B. `yield from` est synonyme de `return`  
C. Aucune  
D. `yield from` boucle automatiquement  

---

### 16. Différence entre `threading`, `multiprocessing`, `asyncio` ?
A. Tous utilisent le même modèle  
B. `threading` pour CPU, `multiprocessing` pour I/O  
C. `threading` partage la mémoire, `multiprocessing` non  
D. `asyncio` est basé sur le multithreading  

---

### 17. Qu’est-ce que le GIL ?
A. Un verrou logiciel de fichiers  
B. Une structure mémoire pour les objets globaux  
C. Un verrou global empêchant l’exécution parallèle de threads  
D. Une base de registre  

---

### 18. Quand utiliser `asyncio` ?
A. Pour tâches fortement parallélisées CPU  
B. Pour I/O non bloquantes comme sockets, HTTP  
C. Pour le rendu graphique  
D. Pour le calcul scientifique  

---

### 19. Que se passe-t-il si on utilise `time.sleep()` dans une coroutine ?
A. La coroutine continue  
B. Le scheduler est bloqué  
C. Une erreur est levée  
D. Elle devient plus rapide  

---

### 20. Quel est le risque d’un `threading.Lock` mal utilisé ?
A. Aucun  
B. Deadlock  
C. Stack overflow  
D. Le thread devient un processus  

---

## ✅ Réponses

|  Q | Rép |
|---:|:---:|
|  1 |  B  | 
|  2 |  B  |
|  3 |  C  |
|  4 |  C  |
|  5 |  C  |
|  6 |  C  |
|  7 |  B  |
|  8 |  C  |
|  9 |  C  |
| 10 |  B  |
| 11 |  B  |
| 12 |  C  |
| 13 |  B  |
| 14 |  C  |
| 15 |  A  |
| 16 |  C  |
| 17 |  C  |
| 18 |  B  |
| 19 |  B  |
| 20 |  B  |
