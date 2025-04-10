## 🛠️ Outils pour explorer une DLL en détail

| Outil                   | Fonction principale                         | Où le trouver                          |
|------------------------|---------------------------------------------|----------------------------------------|
| **`dumpbin`**          | Liste les symboles/exportations (CLI)       | 📦 Inclus avec [Visual Studio](https://visualstudio.microsoft.com/fr/) (Developer Command Prompt) |
| **Dependency Walker**  | Visualise les dépendances d’une DLL         | 📥 [http://www.dependencywalker.com/](http://www.dependencywalker.com/) |
| **DLL Export Viewer**  | Liste simple des fonctions exportées        | 📥 [https://www.nirsoft.net/utils/dll_export_viewer.html](https://www.nirsoft.net/utils/dll_export_viewer.html) |
| **Ghidra**             | Reverse engineering binaire open-source     | 🛡️ [https://ghidra-sre.org/](https://ghidra-sre.org/) |
| **IDA Free**           | Analyse de code machine/désassemblage       | 🧠 [https://hex-rays.com/ida-free/](https://hex-rays.com/ida-free/) |
| **PE Explorer**        | Analyse graphique de fichiers PE (exe/dll)  | 🧰 [https://www.heaventools.com/overview.htm](https://www.heaventools.com/overview.htm) (payant, essai gratuit) |
| **x64dbg**             | Débogueur et explorateur de code natif      | 🧪 [https://x64dbg.com/](https://x64dbg.com/) |

---

## 🔍 Pour commencer simplement

### ✅ Méthode rapide avec `dumpbin`
```bash
dumpbin /exports C:\Windows\System32\user32.dll
```
➡️ À lancer dans le **Developer Command Prompt for VS** (disponible avec Visual Studio Build Tools).

---

## 💡 Recommandations selon ton usage

| Besoin                           | Outil conseillé                     |
|----------------------------------|-------------------------------------|
| Liste des fonctions exportées    | `dumpbin`, DLL Export Viewer        |
| Voir les DLL dépendantes         | Dependency Walker                   |
| Explorer le code natif en détail | Ghidra, IDA Free, x64dbg            |
| Rechercher chaînes, structures   | PE Explorer, Ghidra                 |
| Débogage dynamique               | x64dbg, WinDbg                      |

---
