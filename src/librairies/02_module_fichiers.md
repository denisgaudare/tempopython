Pour la **gestion des fichiers** en Python, voici les modules et fonctions les plus couramment utilisées :

---

### 📂 **Module `os`** (Interaction avec le système d'exploitation)
- `os.getcwd()` – Obtenir le répertoire de travail actuel
- `os.listdir(path)` – Lister les fichiers et dossiers d'un répertoire
- `os.makedirs(path, exist_ok=True)` – Créer un répertoire (et sous-dossiers si nécessaire)
- `os.remove(path)` – Supprimer un fichier
- `os.rmdir(path)` – Supprimer un dossier vide
- `os.rename(src, dst)` – Renommer ou déplacer un fichier/dossier
- `os.path.exists(path)` – Vérifier si un fichier/dossier existe
- `os.path.isfile(path)` – Vérifier si un chemin est un fichier
- `os.path.isdir(path)` – Vérifier si un chemin est un dossier
- `os.path.join(path1, path2, ...)` – Construire un chemin de fichier portable

---

### 📌 **Module `shutil`** (Manipulation avancée des fichiers et dossiers)
- `shutil.copy(src, dst)` – Copier un fichier
- `shutil.copy2(src, dst)` – Copier un fichier en conservant les métadonnées
- `shutil.copytree(src, dst)` – Copier récursivement un dossier
- `shutil.move(src, dst)` – Déplacer un fichier ou un dossier
- `shutil.rmtree(path)` – Supprimer un dossier et son contenu

---

### 🛠 **Module `pathlib`** (Manipulation de fichiers en mode objet)
#### Remplacement moderne de `os` et `shutil`
- `Path(path).exists()` – Vérifier l'existence d'un fichier/dossier
- `Path(path).is_file()` – Vérifier si c'est un fichier
- `Path(path).is_dir()` – Vérifier si c'est un dossier
- `Path(path).mkdir(parents=True, exist_ok=True)` – Créer un dossier récursivement
- `Path(path).unlink(missing_ok=True)` – Supprimer un fichier
- `Path(path).rename(new_path)` – Renommer un fichier/dossier
- `Path(path).iterdir()` – Lister les fichiers/dossiers d'un répertoire
- `Path(path).rmdir()` – Supprimer un dossier vide
- `Path(path).read_text()` – Lire un fichier texte
- `Path(path).write_text(content)` – Écrire dans un fichier texte

---

### 📜 **Module `tempfile`** (Fichiers temporaires)
- `tempfile.TemporaryFile()` – Créer un fichier temporaire
- `tempfile.NamedTemporaryFile()` – Fichier temporaire avec un nom accessible
- `tempfile.TemporaryDirectory()` – Créer un dossier temporaire

---

### 📑 **Lecture / Écriture de fichiers**
#### Mode classique avec `open()`
```python
# Lecture d'un fichier texte
with open("exemple.txt", "r", encoding="utf-8") as f:
    contenu = f.read()

# Écriture dans un fichier (écrase le contenu existant)
with open("exemple.txt", "w", encoding="utf-8") as f:
    f.write("Bonjour, monde!")

# Ajout de contenu (sans écraser)
with open("exemple.txt", "a", encoding="utf-8") as f:
    f.write("\nNouvelle ligne ajoutée!")
```

#### Mode binaire pour les fichiers non-textuels
```python
with open("image.jpg", "rb") as f:
    data = f.read()

with open("image_copy.jpg", "wb") as f:
    f.write(data)
```

---

### 📊 **Module `csv`** (Fichiers CSV)
```python
import csv

# Lecture d'un fichier CSV
with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Écriture d'un fichier CSV
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Nom", "Âge"])
    writer.writerow(["Alice", 25])
    writer.writerow(["Bob", 30])
```

---

### 🛠 **Meilleures pratiques**
✅ **Utiliser `with open()`** : Ferme automatiquement le fichier après utilisation.  
✅ **Privilégier `pathlib`** : Plus moderne et lisible que `os`.  
✅ **Utiliser `shutil` pour les copies/mouvements** : Plus fiable que `os.rename()`.  
✅ **Gérer les erreurs (`try-except`)** : Empêche les plantages en cas de fichier inexistant.  
Traitement des données et collections