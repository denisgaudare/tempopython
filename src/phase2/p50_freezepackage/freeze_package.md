**Transformer du code Python en un exécutable autonome** pour **Windows et/ou Linux**, tu as deux familles d’outils :

---

## 🧊 1. **Freezers** (créent un exécutable standalone)
👉 Emballent **Python + ton script + les dépendances** dans un exécutable

| Outil | Plateformes | Format de sortie | Notes |
|------|-------------|------------------|-------|
| **PyInstaller** | Windows, Linux, macOS | `.exe` (Windows), binaire (Linux) | Ultra populaire, simple à utiliser |
| **cx_Freeze** | Windows, Linux, macOS | Dossier ou exécutable | Plus orienté projets classiques |
| **Nuitka** | Windows, Linux, macOS | Compilé en C → exécutable | Très rapide, bon pour l’obfuscation/perf |
| **py2exe** | Windows uniquement | `.exe` | Vieux mais fonctionne encore |
| **shiv** | Linux/macOS | `.pyz` (zippé, exécutable avec Python) | Moins pour le desktop, utile pour CLIs |
| **Briefcase** (via BeeWare) | Windows, Linux, macOS, mobile, etc. | Application native | Idéal pour GUI multiplateforme |

---

### 🔧 Exemple PyInstaller

```bash
pip install pyinstaller
pyinstaller --onefile monscript.py
```

Ça crée un exécutable dans `dist/monscript.exe` (ou sans extension sous Linux).

---

## 📦 2. **Packagers / Builders** (créent des installeurs ou environnements)

| Outil | Rôle | Notes |
|-------|------|-------|
| **setuptools** / `setup.py` | Emballer ton projet Python pour distribution PyPI | Standard |
| **pipx** / **venv** | Créer un environnement isolé exécutable | Pratique pour CLIs |
| **Pex** | Crée un `.pex` (Python EXecutable zip) | Similaire à `.jar` en Java |
| **Conda / conda-pack** | Crée un environnement portatif | Plus lourd mais cross-platform |
| **Docker** | Emballer tout dans un conteneur Linux | Idéal pour Linux server/cloud

---

## 🛡 Bonus : Obfuscation & Protection

Si tu veux **protéger ton code source** :

| Outil | Usage |
|-------|-------|
| **Nuitka** | Compile en C, bonne protection |
| **Cython** | Compile en `.pyd` ou `.so` |
| **pyarmor** | Obfuscation + license management |
| **UPX** | Compresser les exécutables générés |

---

## 📌 Recommandations par cas

| Cas d’usage | Outil recommandé |
|-------------|------------------|
| Petit script CLI pour Windows/Linux | PyInstaller `--onefile` |
| Application GUI multiplateforme | PyInstaller ou Briefcase |
| Performance + protection | Nuitka |
| Conteneur pour cloud / serveur | Docker |
| Distribution sur PyPI | setuptools + wheel |
| Script réutilisable sans Python installé | PyInstaller ou cx_Freeze |

---
