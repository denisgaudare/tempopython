### **📌 Le Duck Typing en Python**
Le **duck typing** est un concept de typage **dynamique** utilisé en Python. Il permet à un objet d’être utilisé dans un contexte donné **s’il se comporte comme attendu**, sans se soucier de son type exact.

📜 **Principe :**  
*"Si ça marche comme un canard, nage comme un canard et cancane comme un canard, alors c'est un canard."*

En Python, cela signifie qu’on **ne vérifie pas** explicitement le type d’un objet, mais on s’assure qu’il **possède les méthodes et attributs attendus**.

---

## **🔹 Exemple 1 : Sans duck typing (vérification explicite du type)**
🚫 **Mauvaise approche** en Python (style rigide, à la C# ou Java) :

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def make_sound(animal):
    if isinstance(animal, Dog):
        print(animal.speak())
    elif isinstance(animal, Cat):
        print(animal.speak())
    else:
        raise TypeError("L'objet doit être un Dog ou un Cat")

make_sound(Dog())  # "Woof!"
make_sound(Cat())  # "Meow!"
```
❌ **Problème** : Cette approche **limite la flexibilité**, obligeant à vérifier explicitement chaque type.

---

## **🔹 Exemple 2 : Avec duck typing (Pythonic)**
✅ **Bonne approche** en Python :

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Robot:
    def speak(self):
        return "Beep Boop!"

def make_sound(entity):
    print(entity.speak())  # On ne vérifie pas le type, on suppose juste qu'il a .speak()

make_sound(Dog())  # "Woof!"
make_sound(Cat())  # "Meow!"
make_sound(Robot())  # "Beep Boop!" (fonctionne sans changement !)
```
✅ **Avantages** :
- **Aucune vérification explicite** du type (`isinstance()` ou `type()` est inutile).
- **Plus flexible** : tout objet ayant une méthode `speak()` fonctionne.
- **Extensible** : on peut ajouter de nouveaux objets sans modifier `make_sound()`.

---

## **🔹 Comparaison avec C#**
En **C#**, le duck typing **n’existe pas** directement, car le langage est statiquement typé.  
On doit utiliser des **interfaces** (`interface`) pour obtenir un comportement similaire.

```csharp
using System;

interface ISpeaker
{
    string Speak();
}

class Dog : ISpeaker
{
    public string Speak() => "Woof!";
}

class Cat : ISpeaker
{
    public string Speak() => "Meow!";
}

void MakeSound(ISpeaker speaker) // Oblige à implémenter l'interface
{
    Console.WriteLine(speaker.Speak());
}

MakeSound(new Dog()); // "Woof!"
MakeSound(new Cat()); // "Meow!"
```
❌ **Problème en C#** : Chaque classe doit **implémenter explicitement l'interface**.  
✅ **Avantage** de Python : Pas besoin d’interface, **juste une méthode du bon nom suffit**.

---

## **🔹 Quand éviter le Duck Typing ?**
🔻 **Cas où le duck typing peut être risqué** :
- Si un objet **n’a pas** la méthode attendue, on obtient une **erreur à l’exécution** :
  ```python
  class Table:
      pass

  make_sound(Table())  # AttributeError: 'Table' object has no attribute 'speak'
  ```
- Solution : **Utiliser `hasattr()`** avant d’appeler une méthode :
  ```python
  def make_sound(entity):
      if hasattr(entity, "speak"):
          print(entity.speak())
      else:
          print("Cet objet ne sait pas parler !")
  ```

- Ou utiliser **`@abstractmethod`** (classes abstraites) pour forcer une méthode dans les sous-classes.

---

## **🔎 Conclusion**
✅ **Le duck typing permet une flexibilité maximale** en Python.  
✅ **Il évite les interfaces et rend le code plus générique et réutilisable**.  
❌ **Mais il peut causer des erreurs à l’exécution si un objet ne possède pas l’attribut attendu**.  

🔥 **En résumé :**  
- **Python (duck typing)** → "Si ça ressemble à un canard, alors c’est un canard !"  
- **C# (interfaces, typage strict)** → "Si ça ne déclare pas officiellement être un canard, alors ce n'est pas un canard."

🔹 **À privilégier pour :** Développement rapide, flexibilité.  
🔹 **À éviter pour :** Code critique nécessitant un contrôle strict des types. 🚀