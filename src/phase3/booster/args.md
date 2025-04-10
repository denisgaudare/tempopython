---

## 🧰 Les 4 outils principaux

| Lib           | Description                          | Niveau         | Points forts                                       |
|---------------|--------------------------------------|----------------|----------------------------------------------------|
| `sys.argv`    | Basique, liste d'booster bruts     | Débutant       | Simple, sans dépendance                           |
| `argparse`    | Standard Python (lib standard)       | Intermédiaire  | Structuré, doc automatique                        |
| `click`       | Lib externe, ergonomique             | Avancé         | Décorateurs, gestion CLI élégante                 |
| `typer`       | Moderne, basé sur `click` + `typing` | Très avancé    | Super ergonomie, autocomplétion, aide automatique |

---

## ✅ 1. `sys.argv` — la méthode brute

```python
import sys
print("Arguments :", sys.argv)
```

➡️ Pour des scripts très simples.

---

## ✅ 2. `argparse` — la bibliothèque standard

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", required=True)
parser.add_argument("--age", type=int, default=30)
args = parser.parse_args()

print(f"Bonjour {args.name}, vous avez {args.age} ans.")
```

- ✔ Inclus dans Python
- ✔ Génère l’aide automatiquement : `python script.py --help`

---

## ✅ 3. `click` — Ergonomique et lisible

```python
import click

@click.command()
@click.option('--name', prompt='Votre nom', help='Nom à afficher')
@click.option('--age', default=30, help='Âge')
def hello(name, age):
    click.echo(f"Bonjour {name}, vous avez {age} ans.")

if __name__ == '__main__':
    hello()
```

- ✔ Très lisible, coloré, interactions possibles
- ✨ Supporte des commandes imbriquées (`@click.group()`)

```bash
pip install click
```

---

## ✅ 4. `typer` — Le plus moderne (recommandé 🏆)

```python
import typer

def main(name: str, age: int = 30):
    print(f"Bonjour {name}, vous avez {age} ans.")

if __name__ == "__main__":
    typer.run(main)
```

- ✔ Typage natif (`str`, `int`, `Optional`)
- ✔ Génère l’aide automatiquement
- ✔ Très proche de FastAPI dans l’UX

```bash
pip install typer
```

---

## 🔁 Résumé : Quel outil pour quel besoin ?

| Besoin                              | Choix conseillé |
|-------------------------------------|-----------------|
| Script rapide                       | `sys.argv`      |
| CLI simple et maintenable          | `argparse`      |
| CLI user-friendly                   | `click`         |
| CLI typée et moderne                | `typer`         |

---
