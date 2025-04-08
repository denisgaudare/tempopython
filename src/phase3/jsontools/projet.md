## 🧪 Projet complet : **PhysiJSON** – Analyse multi-niveau de résultats expérimentaux en physique

### 🧠 Thème
Une base de données en **NDJSON** contient des **résultats expérimentaux bruts** de laboratoires (physique quantique, mécanique, optique, etc.). Chaque enregistrement représente une série d’expériences numériques avec :
- une équation du phénomène simulé (en LaTeX ou string),
- un contexte d’exécution (paramètres, temps de calcul, précision numérique),
- une série de résultats (`x`, `y`, `erreur`),
- un identifiant de simulation,
- des métadonnées (auteur, date, domaine).

---

## 📦 Contenu typique d’un fichier `.ndjson`

```json
{"id": "exp001", "domain": "optics", "formula": "E=hf", "parameters": {"f": [4.5e14, 5e14]}, "results": [{"x": 4.5e14, "y": 2.98e-19, "error": 1e-21}, ...], "metadata": {"author": "Dr. Light", "timestamp": "2024-11-01T13:45:00"}}
{"id": "exp002", "domain": "mechanics", "formula": "F=ma", "parameters": {"m": [1,2,3], "a": [9.8]}, ...}
```

---

## 🧩 Étapes du projet (progression en difficulté)

### 🔹 Étape 1 – **Chargement et validation**
- Parser le NDJSON (fichier de plusieurs centaines de Mo).
- Valider chaque bloc avec un **JSON Schema**.
- Compter les enregistrements valides / invalides, générer un fichier NDJSON d'erreurs.

👉 Challenge : faire tourner la validation en **streaming** (`ijson`) ou par batch.

---

### 🔹 Étape 2 – **Transformations mathématiques**
- Évaluer les formules (`sympy` ou parsing maison) et comparer avec les résultats.
- Calculer les **écarts relatifs**, détecter les anomalies > seuil.
- Générer une table enrichie pour chaque expérience.

👉 Challenge : parsing d’expressions LaTeX ou mathématiques, utilisation de `sympy` pour simplifier et comparer.

---

### 🔹 Étape 3 – **Enrichissement**
- Enrichir les enregistrements avec des calculs externes :
  - incertitude combinée,
  - calcul énergétique (ex. intégrale numérique sur les points `x`, `y`),
  - durée estimée de l'expérience via heuristique.

👉 Challenge : programmation scientifique + précision numérique (usage de `decimal` ?).

---

### 🔹 Étape 4 – **Agrégation multi-domaine**
- Regrouper les expériences par domaine (`optics`, `quantum`, etc.).
- Générer :
  - Moyennes, écarts-types sur les erreurs,
  - Histogrammes (par domaine),
  - Top 5 anomalies par domaine.

👉 Challenge : modélisation hiérarchique des résultats, fusion multi-fichiers NDJSON.

---

### 🔹 Étape 5 – **Export & reporting**
- Exporter :
  - un fichier CSV synthétique (expérience + anomalie + score),
  - un `report.json` avec tous les indicateurs globaux,
  - un dashboard HTML (`jinja2`),
  - un rapport PDF (`weasyprint`).

👉 Challenge : génération dynamique avec `Jinja2`, styles, graphes `matplotlib`/`plotly`.

---

### 🔹 Étape 6 – **Performance et structuration logicielle**
- Utiliser :
  - `orjson` pour le parsing rapide,
  - `pydantic` ou `dataclasses` pour le typage structuré,
  - `typer` pour la CLI,
  - `concurrent.futures` ou `asyncio` pour le parsing massif.

👉 Challenge : structuration modulaire, CLI robuste, performances.

---

## 🛠️ Stack technique recommandée

| Besoin                      | Libs recommandées                        |
|----------------------------|------------------------------------------|
| Parsing NDJSON             | `ijson`, `ndjson`, `orjson`              |
| Validation JSON Schema     | `jsonschema`                             |
| Maths / Physique           | `sympy`, `numpy`, `scipy`, `decimal`     |
| Structuration              | `pydantic`, `dataclasses`                |
| Transformation / analyse   | `pandas`, `polars`, `matplotlib`         |
| Exports                    | `csv`, `jinja2`, `weasyprint`            |
| CLI                        | `typer`, `argparse`                      |
| Concurrence / perf         | `concurrent.futures`, `asyncio`          |

---

## 🧪 Bonus : idées d'exercices

| Exercice | Description |
|---------|-------------|
| 🧠 1 | Implémenter un `json-validator` NDJSON en streaming |
| 🔍 2 | Parser une formule en LaTeX et la comparer à des valeurs |
| 📊 3 | Générer des métriques statistiques multi-domaines |
| ⚡ 4 | Optimiser le traitement d’un gros NDJSON en `asyncio` |
| 📄 5 | Générer un PDF scientifique lisible avec annexes de graphes |
| 🧪 6 | Créer une simulation de nouvelle expérience à injecter dans la base |

---
