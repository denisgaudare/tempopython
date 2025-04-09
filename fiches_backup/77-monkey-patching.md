### **Monkey Patching**

Le **monkey patching** est une technique qui consiste à modifier le comportement d'un module, d'une classe ou d'une fonction existante **à l'exécution**, sans modifier son code source d'origine. Cela permet de corriger un bug, d'ajouter des fonctionnalités ou de modifier un comportement temporairement.

#### **Exemple en Python**
Prenons un exemple simple où nous modifions la méthode `speak` d'une classe `Animal` après sa définition :

```python
class Animal:
    def speak(self):
        return "Je fais un bruit générique."

# Instanciation de la classe
animal = Animal()
print(animal.speak())  # Sortie : "Je fais un bruit générique."

# Monkey patching : on modifie la méthode speak
def new_speak(self):
    return "Je suis un animal qui parle différemment !"

Animal.speak = new_speak  # Remplacement de la méthode originale

# Test après le patch
print(animal.speak())  # Sortie : "Je suis un animal qui parle différemment !"
```
Ici, nous avons **dynamiquement remplacé** la méthode `speak()` sans modifier la classe d'origine.

---

### **Avantages du Monkey Patching**
✅ **Flexibilité** : Permet d'ajouter ou modifier des fonctionnalités **sans toucher au code source**.  
✅ **Utile pour corriger des bugs** dans des bibliothèques tierces sans attendre une mise à jour.  
✅ **Personnalisation rapide** : Adapte des comportements en fonction des besoins d'un projet spécifique.

---

### **Inconvénients du Monkey Patching**
❌ **Fragilité** : Si la bibliothèque évolue, le patch peut devenir obsolète et provoquer des erreurs.  
❌ **Difficulté de maintenance** : Le code devient difficile à comprendre et à déboguer.  
❌ **Effet de bord imprévisible** : Modifier une classe ou une fonction globale peut impacter d'autres parties du programme.  
❌ **Risque de conflit** : Si plusieurs modules effectuent des monkey patchs sur la même méthode, le comportement final est imprévisible.

---

### **Quand utiliser le Monkey Patching ?**
- **Cas d'urgence** : Pour corriger un bug critique dans une bibliothèque tierce en attendant un correctif officiel.
- **Prototypage rapide** : Tester un nouveau comportement sans modifier directement le code source.
- **Mocking en tests unitaires** : Simuler des comportements sans modifier l'implémentation originale.

💡 **Alternative recommandée** : Si possible, privilégiez l'héritage ou les décorateurs plutôt que le monkey patching pour éviter des effets de bord.


# **Exemple complexe de Monkey Patching dans un projet Aircraft*

Imaginons que nous travaillons sur un **simulateur de vol** et que nous utilisons une bibliothèque tierce qui gère les capteurs d’un avion (`AircraftSensors`). Cependant, cette bibliothèque contient un bug qui renvoie des valeurs erronées pour l’altitude. En attendant une mise à jour officielle, nous allons **corriger ce bug via le Monkey Patching**.

---

### **Contexte**
Nous avons une classe `AircraftSensors` qui récupère l’altitude actuelle d’un avion à partir d’un capteur, mais elle renvoie parfois une valeur incorrecte (ex. une altitude négative). Nous allons patcher cette méthode pour nous assurer que l’altitude est toujours **positive et réaliste**.

---

### **Code Avant Monkey Patching**
```python
import random

class AircraftSensors:
    """Classe simulant des capteurs d'un avion"""
    
    def get_altitude(self):
        """Simule une lecture de l'altitude depuis un capteur"""
        return random.uniform(-500, 10000)  # BUG : Peut renvoyer une altitude négative

# Simulation d'un avion
sensors = AircraftSensors()
print(f"Altitude avant patch: {sensors.get_altitude()} mètres")  # Peut être négatif !
```

#### **Problème** :
Le capteur peut parfois retourner une altitude **négative**, ce qui est **irréaliste**.

---

### **Solution avec Monkey Patching**
Nous allons corriger la méthode `get_altitude()` en **interceptant son appel** et en forçant un minimum de `0` mètres.

```python
# Fonction qui corrigera la méthode get_altitude
def patched_get_altitude(self):
    """Correction du bug : assure que l'altitude est toujours >= 0 mètres"""
    raw_altitude = original_get_altitude(self)  # Appel de la méthode originale
    return max(0, raw_altitude)  # Empêche une altitude négative

# On sauvegarde la méthode originale
original_get_altitude = AircraftSensors.get_altitude

# Application du Monkey Patching
AircraftSensors.get_altitude = patched_get_altitude

# Vérification après patch
print(f"Altitude après patch: {sensors.get_altitude()} mètres")  # Toujours >= 0 !
```

---

### **Explication du Monkey Patching**
1. **On sauvegarde** la méthode originale `get_altitude` pour pouvoir l’appeler dans notre patch.
2. **On redéfinit `patched_get_altitude`** qui intercepte l’appel et empêche les valeurs négatives.
3. **On remplace dynamiquement `AircraftSensors.get_altitude`** par notre version corrigée.

---

### **Avantages dans ce cas précis**
✅ **Correction rapide d’un bug critique sans modifier le code source** de la bibliothèque.  
✅ **Aucune attente d’une mise à jour officielle** du fournisseur du capteur.  
✅ **Peut être facilement révoqué** (restaurer `original_get_altitude` si nécessaire).  

---

### **Inconvénients**
❌ **Si la bibliothèque évolue, le patch peut devenir obsolète**.  
❌ **Peut entraîner des comportements imprévus** si d’autres parties du programme dépendent de la méthode d’origine.  
❌ **Difficile à déboguer** si le patch est appliqué de manière silencieuse sans documentation.

---

### **Conclusion**
Le Monkey Patching est un **outil puissant mais risqué**. Dans un projet aéronautique, il peut **éviter un crash logiciel** (ou même physique) en corrigeant des bugs critiques **sans modifier directement la bibliothèque**. Cependant, il doit être utilisé **avec précaution**, idéalement **temporairement**, en attendant une solution officielle. 🚀✈️

