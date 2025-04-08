### **Mypy : Vérificateur de types pour Python**

#### **📌 Définition**
Mypy est un **vérificateur de type statique** pour Python. Il analyse le code source pour s'assurer que les types déclarés sont bien respectés, sans exécuter le programme.

📌 **Python est dynamiquement typé**, ce qui signifie que les types ne sont pas strictement imposés à l'exécution. Mypy ajoute une couche de **typage statique optionnel**, permettant d'éviter certaines erreurs courantes.

---

### **📌 Installation de Mypy**
Mypy s'installe facilement avec `pip` :
```sh
pip install mypy
```

---

### **📌 Exemple d'utilisation**
#### **✅ Code correct avec annotations de type**
```python
def addition(a: int, b: int) -> int:
    return a + b

resultat = addition(2, 3)  # OK
```
✔ Mypy valide ce code car les types sont bien respectés.

#### **❌ Exemple de type incorrect**
```python
def addition(a: int, b: int) -> int:
    return a + b

resultat = addition(2, "3")  # Erreur !
```

Si on exécute Mypy sur ce fichier :
```sh
mypy mon_script.py
```
On obtient une erreur :
```
mon_script.py:5: error: Argument 2 to "addition" has incompatible type "str"; expected "int"
```
📌 **Python ne lèvera pas d'erreur à l'exécution**, mais Mypy permet de détecter cette erreur **avant** que le programme ne tourne.

---

### **📌 Typage avancé avec Mypy**
#### **1️⃣ Vérification des listes**
```python
from typing import List

def somme_liste(nombres: List[int]) -> int:
    return sum(nombres)

print(somme_liste([1, 2, 3]))  # OK
print(somme_liste(["a", "b", "c"]))  # Mypy va signaler une erreur
```

#### **2️⃣ Typage optionnel (`Optional`)**
```python
from typing import Optional

def afficher_nom(nom: Optional[str]) -> None:
    if nom:
        print(f"Bonjour, {nom}!")
    else:
        print("Bonjour, inconnu!")

afficher_nom("Alice")  # OK
afficher_nom(None)  # OK
```

#### **3️⃣ Vérification avec les `dataclasses`**
```python
from dataclasses import dataclass

@dataclass
class Personne:
    nom: str
    age: int

p = Personne("Alice", "trente")  # Erreur détectée par Mypy
```
📌 Python acceptera `"trente"` comme `age`, mais Mypy signalera une erreur.

---

### **📌 Pourquoi utiliser Mypy ?**
✅ Détection des erreurs de type **avant l'exécution**  
✅ Meilleure **lisibilité du code**  
✅ Compatible avec **les annotations de type modernes**  
✅ **Facultatif** : Python fonctionne même sans Mypy  

Mypy est particulièrement utile pour :
- **Les projets de grande envergure**
- **Le travail en équipe**
- **Les API robustes**
- **Les codes critiques (finance, médical, etc.)**

📌 **Tu veux essayer sur un projet ?** Tu peux lancer :
```sh
mypy mon_projet/
```
et voir les erreurs potentielles de typage ! 🚀