Les **métaclasses** en Python permettent de personnaliser la création des classes, en modifiant leur comportement avant leur instanciation. 

---

## **1. Métaclasse pour imposer un préfixe aux attributs**
### *Cas d’usage* : s’assurer que toutes les variables de classe commencent par un préfixe donné.

```python
class PrefixAttributesMeta(type):
    PREFIX = "attr_"

    def __new__(cls, name, bases, class_dict):
        new_class_dict = {}
        for key, value in class_dict.items():
            if not key.startswith("__"):  # Ne pas modifier les attributs spéciaux
                new_class_dict[cls.PREFIX + key] = value
            else:
                new_class_dict[key] = value
        return super().__new__(cls, name, bases, new_class_dict)

class MyClass(metaclass=PrefixAttributesMeta):
    valeur = 10
    status = "actif"

obj = MyClass()
print(hasattr(obj, "valeur"))  # False
print(hasattr(obj, "attr_valeur"))  # True
print(obj.attr_status)  # "actif"
```
🔹 *Utilité* : Garantir une convention de nommage des attributs (ex. pour éviter les conflits).

---

## **2. Métaclasse pour interdire l’héritage**
### *Cas d’usage* : empêcher qu’une classe soit héritée.

```python
class FinalMeta(type):
    def __new__(cls, name, bases, class_dict):
        if any(isinstance(base, FinalMeta) for base in bases):
            raise TypeError(f"La classe {name} ne peut pas hériter de {bases[0].__name__}")
        return super().__new__(cls, name, bases, class_dict)

class BaseFinal(metaclass=FinalMeta):
    pass

# class Derived(BaseFinal):  # Erreur !
#     pass
```
🔹 *Utilité* : Garantir qu’une classe reste "finale" et ne puisse pas être dérivée.

---

## **3. Métaclasse pour s’assurer que toutes les méthodes sont documentées**
### *Cas d’usage* : imposer une documentation (`docstring`) pour chaque méthode.

```python
class DocstringEnforcerMeta(type):
    def __new__(cls, name, bases, class_dict):
        for attr_name, attr_value in class_dict.items():
            if callable(attr_value) and attr_name != "__init__":
                if not attr_value.__doc__:
                    raise TypeError(f"La méthode '{attr_name}' de la classe '{name}' doit avoir une docstring.")
        return super().__new__(cls, name, bases, class_dict)

class MyDocumentedClass(metaclass=DocstringEnforcerMeta):
    def method1(self):
        """Ceci est une méthode documentée."""
        pass

    # def method2(self):  # Erreur si décommenté
    #     pass
```
🔹 *Utilité* : Forcer les développeurs à documenter toutes les méthodes pour améliorer la maintenabilité.

---

## **4. Métaclasse pour convertir les attributs de classe en majuscules**
### *Cas d’usage* : garantir que toutes les constantes soient en majuscules.

```python
class UpperCaseAttributesMeta(type):
    def __new__(cls, name, bases, class_dict):
        new_class_dict = {}
        for key, value in class_dict.items():
            if not key.startswith("__") and isinstance(value, str):
                new_class_dict[key.upper()] = value  # Convertir en majuscules
            else:
                new_class_dict[key] = value
        return super().__new__(cls, name, bases, new_class_dict)

class Config(metaclass=UpperCaseAttributesMeta):
    debug = "on"
    mode = "development"

print(Config.DEBUG)  # "on"
print(Config.MODE)  # "development"
# print(Config.debug)  # Erreur, l'attribut n'existe pas sous ce nom
```
🔹 *Utilité* : Appliquer un standard aux attributs d'une classe pour assurer leur cohérence.

---

### **Conclusion**
Ces quatre métaclasses permettent de :
✅ **Modifier dynamiquement les attributs des classes**  
✅ **Faire respecter des règles strictes**  
✅ **Garantir une convention de programmation**  

Les métaclasses sont très puissantes, mais doivent être utilisées avec précaution car elles complexifient le code. 🚀