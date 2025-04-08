### **Les Métaclasses en Python : Ancien Mode vs Nouveau Mode**
Les **métaclasses** sont des classes dont le rôle est de créer des classes. Elles permettent de **modifier dynamiquement la création d'une classe** avant son instanciation.

---

## **1. Ancien Mode (`__metaclass__` dans Python 2)**
En Python 2, on définissait une **métaclasse** avec l’attribut spécial `__metaclass__` au niveau de la classe :

```python
class Meta(type):
    """Une métaclasse qui modifie dynamiquement les classes"""
    def __new__(cls, name, bases, class_dict):
        print(f"Création de la classe : {name}")
        return super().__new__(cls, name, bases, class_dict)

class MyClass(metaclass=Meta):  # Python 3
    __metaclass__ = Meta  # Python 2
    def method(self):
        return "Méthode de MyClass"

print(MyClass())  # Affiche un message à la création
```

### **🛑 Problèmes de l'ancien mode (`__metaclass__`) :**
1. **Moins explicite** : L'utilisation de `__metaclass__` pouvait être confuse.
2. **Non supporté en Python 3** : Cette approche est obsolète et a été remplacée.

---

## **2. Nouveau Mode (`metaclass=` en Python 3)**
Depuis Python 3, on utilise **l'argument `metaclass=` directement dans la définition de la classe**.

```python
class Meta(type):
    """Métaclasse qui affiche un message lors de la création de classe"""
    def __new__(cls, name, bases, class_dict):
        print(f"Création de la classe : {name}")
        return super().__new__(cls, name, bases, class_dict)

# Utilisation en Python 3
class MyClass(metaclass=Meta):
    def method(self):
        return "Méthode de MyClass"

print(MyClass())  # Affiche "Création de la classe : MyClass"
```

✅ **Pourquoi le nouveau mode est meilleur ?**
- **Plus explicite** : On voit immédiatement que `MyClass` utilise `Meta` comme métaclasse.
- **Plus flexible** : Compatible avec l’héritage multiple et les nouvelles fonctionnalités de Python 3.

---

## **3. Différence entre `__new__` et `__init__` dans une métaclasse**
Dans une métaclasse, `__new__` et `__init__` jouent un rôle clé :

| Méthode | Quand est-elle appelée ? | Rôle |
|---------|-------------------------|------|
| `__new__(cls, name, bases, dct)` | Avant la création de la classe | Crée la classe et peut modifier son dictionnaire |
| `__init__(self, name, bases, dct)` | Après la création de la classe | Initialise la classe (comme pour les objets) |

### **Exemple pour illustrer `__new__` et `__init__`**
```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"__new__ : Création de {name}")
        dct["new_attribute"] = "Ajouté par Meta"
        return super().__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print(f"__init__ : Initialisation de {name}")
        super().__init__(name, bases, dct)

class MyClass(metaclass=Meta):
    pass

print(MyClass.new_attribute)  # Vérifie que l'attribut a bien été ajouté
```

✅ **Pourquoi utiliser `__new__` ?**
- Permet de **modifier la classe avant sa création** (ex. ajouter dynamiquement des attributs).
- Contrairement à `__init__`, il peut **remplacer** complètement la classe retournée.

---

## **4. Cas Pratiques des Métaclasses**
### **🔹 Vérifier qu’une classe respecte certaines contraintes**
On peut imposer que **toutes les classes dérivées aient un attribut spécifique** :

```python
class MetaCheckAttributes(type):
    def __new__(cls, name, bases, dct):
        if "required_attribute" not in dct:
            raise TypeError(f"La classe {name} doit avoir 'required_attribute'")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MetaCheckAttributes):
    required_attribute = "Présent"

# class MyInvalidClass(metaclass=MetaCheckAttributes):  # Déclenche une erreur
#     pass
```

✅ **Pourquoi c'est utile ?**
- Permet d'appliquer des **règles de conception** à toutes les classes enfants.
- **Évite les erreurs** en forçant l’implémentation de certaines propriétés.

---

### **🔹 Transformer toutes les méthodes en méthodes statiques**
Une métaclasse peut modifier **toutes les méthodes d’une classe** pour qu’elles deviennent statiques :

```python
class AutoStaticMeta(type):
    def __new__(cls, name, bases, dct):
        for key, value in dct.items():
            if callable(value):
                dct[key] = staticmethod(value)  # Transforme chaque méthode en statique
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=AutoStaticMeta):
    def say_hello():
        return "Hello, je suis statique !"

print(MyClass.say_hello())  # Appel direct sans instance
```

✅ **Pourquoi utiliser cette métaclasse ?**
- Évite d’écrire `@staticmethod` partout si **toutes** les méthodes doivent être statiques.

---

## **📌 Comparatif Ancien vs Nouveau Mode**
| Méthode | Ancien Mode (`__metaclass__`) | Nouveau Mode (`metaclass=`) |
|---------|----------------|--------------|
| **Syntaxe** | `__metaclass__ = Meta` dans la classe | `metaclass=Meta` dans la définition |
| **Clarté** | Moins explicite, caché dans l'attribut | Clair et immédiatement visible |
| **Compatibilité** | Seulement Python 2 | Python 3 et compatible avec Python 2.7+ |
| **Flexibilité** | Peut être déroutant à l’usage | Plus lisible et plus extensible |

---

### **📌 Conclusion**
- **Ancien Mode (`__metaclass__`)** : Déprécié en Python 3, moins lisible.
- **Nouveau Mode (`metaclass=`)** : Plus clair, plus puissant et recommandé.
- **Utiliser une métaclasse** pour :
  - **Imposer des contraintes** sur les classes.
  - **Modifier dynamiquement** les classes au moment de leur création.
  - **Automatiser certaines structures** (ex. forcer les méthodes statiques, ajouter des attributs…).
