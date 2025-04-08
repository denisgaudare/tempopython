## C# vs Python
---

## **1. Déclaration de variables**
### **C#**
```csharp
int x = 10;
string name = "Alice";
double pi = 3.14;
bool isActive = true;
```
### **Python**
```python
x = 10
name = "Alice"
pi = 3.14
is_active = True
```

---

## **2. Affichage de texte**
### **C#**
```csharp
Console.WriteLine("Hello, World!");
```
### **Python**
```python
print("Hello, World!")
```

---

## **3. Structures conditionnelles (`if` statements)**
### **C#**
```csharp
int age = 18;
if (age >= 18)
{
    Console.WriteLine("Adulte");
}
else
{
    Console.WriteLine("Mineur");
}
```
### **Python**
```python
age = 18
if age >= 18:
    print("Adulte")
else:
    print("Mineur")
```

---

## **4. Boucles `for`**
### **C#**
```csharp
for (int i = 0; i < 5; i++)
{
    Console.WriteLine(i);
}
```
### **Python**
```python
for i in range(5):
    print(i)
```

---

## **5. Boucles `while`**
### **C#**
```csharp
int i = 0;
while (i < 5)
{
    Console.WriteLine(i);
    i++;
}
```
### **Python**
```python
i = 0
while i < 5:
    print(i)
    i += 1
```

---

## **6. Listes et Tableaux**
### **C#**
```csharp
int[] numbers = {1, 2, 3, 4, 5};
```
### **Python**
```python
numbers = [1, 2, 3, 4, 5]
```

---

## **7. Dictionnaires**
### **C#**
```csharp
Dictionary<string, int> ages = new Dictionary<string, int>();
ages["Alice"] = 25;
ages["Bob"] = 30;
```
### **Python**
```python
ages = {"Alice": 25, "Bob": 30}
```

---

## **8. Fonctions**
### **C#**
```csharp
int Add(int a, int b)
{
    return a + b;
}
Console.WriteLine(Add(2, 3));
```
### **Python**
```python
def add(a, b):
    return a + b

print(add(2, 3))
```

---

## **9. Classes et objets**
### **C#**
```csharp
class Person
{
    public string Name;
    public int Age;

    public Person(string name, int age)
    {
        Name = name;
        Age = age;
    }

    public void SayHello()
    {
        Console.WriteLine($"Hello, my name is {Name}");
    }
}

Person p = new Person("Alice", 25);
p.SayHello();
```
### **Python**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name}")

p = Person("Alice", 25)
p.say_hello()
```

---

## **10. Lecture de l'entrée utilisateur**
### **C#**
```csharp
Console.Write("Entrez votre nom: ");
string name = Console.ReadLine();
Console.WriteLine($"Bonjour, {name}!");
```
### **Python**
```python
name = input("Entrez votre nom: ")
print(f"Bonjour, {name}!")
```

---

## **11. Manipulation des fichiers**
### **C#**
```csharp
using System.IO;

File.WriteAllText("test.txt", "Hello, World!");
string content = File.ReadAllText("test.txt");
Console.WriteLine(content);
```
### **Python**
```python
with open("test.txt", "w") as f:
    f.write("Hello, World!")

with open("test.txt", "r") as f:
    content = f.read()
    print(content)
```

---

## **12. Gestion des exceptions**
### **C#**
```csharp
try
{
    int x = int.Parse("abc");
}
catch (Exception ex)
{
    Console.WriteLine($"Erreur: {ex.Message}");
}
```
### **Python**
```python
try:
    x = int("abc")
except Exception as e:
    print(f"Erreur: {e}")
```

---

## **13. Génération de nombres aléatoires**
### **C#**
```csharp
using System;

Random rand = new Random();
int randomNumber = rand.Next(1, 100);
Console.WriteLine(randomNumber);
```
### **Python**
```python
import random

random_number = random.randint(1, 100)
print(random_number)
```

---

## **14. Vérifier si une clé existe dans un dictionnaire**
### **C#**
```csharp
if (ages.ContainsKey("Alice"))
{
    Console.WriteLine("Alice est présente");
}
```
### **Python**
```python
if "Alice" in ages:
    print("Alice est présente")
```

---

## **15. Parcourir un dictionnaire**
### **C#**
```csharp
foreach (var kvp in ages)
{
    Console.WriteLine($"{kvp.Key} a {kvp.Value} ans");
}
```
### **Python**
```python
for key, value in ages.items():
    print(f"{key} a {value} ans")
```

---

## **16. Filtrer une liste**
### **C#**
```csharp
using System.Linq;

List<int> numbers = new List<int> {1, 2, 3, 4, 5};
List<int> evens = numbers.Where(n => n % 2 == 0).ToList();
```
### **Python**
```python
numbers = [1, 2, 3, 4, 5]
evens = [n for n in numbers if n % 2 == 0]
```

---

## **17. Mesurer le temps d'exécution**
### **C#**
```csharp
using System.Diagnostics;

Stopwatch stopwatch = Stopwatch.StartNew();
// Code à mesurer
stopwatch.Stop();
Console.WriteLine($"Temps écoulé: {stopwatch.ElapsedMilliseconds} ms");
```
### **Python**
```python
import time

start_time = time.time()
# Code à mesurer
elapsed_time = time.time() - start_time
print(f"Temps écoulé: {elapsed_time:.3f} s")
```

---

## **18. Multithreading**
### **C#**
```csharp
using System;
using System.Threading;

Thread thread = new Thread(() => Console.WriteLine("Thread en cours"));
thread.Start();
```
### **Python**
```python
import threading

thread = threading.Thread(target=lambda: print("Thread en cours"))
thread.start()
```
