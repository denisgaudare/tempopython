# Création du code complet du projet PhysiJSON (sans génération de données) dans une nouvelle structure
import json
import os
import zipfile


complete_dir = "physijson_complete"
os.makedirs(os.path.join(complete_dir, "src/physijson"), exist_ok=True)
os.makedirs(os.path.join(complete_dir, "tests"), exist_ok=True)
os.makedirs(os.path.join(complete_dir, "schemas"), exist_ok=True)
os.makedirs(os.path.join(complete_dir, "exports"), exist_ok=True)

# main.py : point d'entrée CLI avec typer
main_py = """\
import typer
from .validator import validate_file
from .analyzer import analyze_experiments

app = typer.Typer()

@app.command()
def validate(input_file: str, schema_file: str):
    validate_file(input_file, schema_file)

@app.command()
def analyze(input_file: str):
    analyze_experiments(input_file)

if __name__ == "__main__":
    app()
"""

# validator.py : validation JSON Schema
validator_py = """\
import json
from jsonschema import validate, ValidationError

def validate_file(input_file, schema_file):
    with open(schema_file) as sf:
        schema = json.load(sf)

    valid = 0
    invalid = 0
    with open(input_file) as f:
        for line in f:
            try:
                record = json.loads(line)
                validate(instance=record, schema=schema)
                valid += 1
            except ValidationError as e:
                print(f"✘ Invalid: {e.message}")
                invalid += 1

    print(f"✔ Valid records: {valid}")
    print(f"✘ Invalid records: {invalid}")
"""

# analyzer.py : analyse scientifique simple
analyzer_py = """\
import json
import sympy
from sympy.parsing.sympy_parser import parse_expr

def safe_eval(expr, local_dict):
    try:
        return float(eval(expr, {"__builtins__": None}, local_dict))
    except Exception:
        return None

def analyze_experiments(input_file):
    with open(input_file) as f:
        for line in f:
            record = json.loads(line)
            domain = record.get("domain")
            formula = record.get("formula")
            results = record.get("results", [])
            parameters = record.get("parameters", {})

            # Simple case: E = h * f
            try:
                if domain == "optics" and "f" in parameters:
                    h = 6.626e-34
                    for res in results:
                        f_val = res["x"]
                        expected = h * f_val
                        actual = res["y"]
                        error = abs(expected - actual)
                        print(f"[{record['id']}] Δ={error:.2e}")
            except Exception as e:
                print(f"[{record['id']}] Erreur analyse: {e}")
"""

# experiment.schema.json
schema_json = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": ["id", "domain", "formula", "parameters", "results", "metadata"],
    "properties": {
        "id": {"type": "string"},
        "domain": {"type": "string"},
        "formula": {"type": "string"},
        "parameters": {"type": "object"},
        "results": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["x", "y", "error"],
                "properties": {
                    "x": {"type": "number"},
                    "y": {"type": "number"},
                    "error": {"type": "number"}
                }
            }
        },
        "metadata": {
            "type": "object",
            "required": ["author", "timestamp"],
            "properties": {
                "author": {"type": "string"},
                "timestamp": {"type": "string", "format": "date-time"}
            }
        }
    }
}

# requirements.txt
requirements_txt = """\
typer
jsonschema
sympy
"""

def saveme(file,data, is_json=False):
    if is_json:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    else:
        with open(file, "w",encoding="utf-8") as f:
            f.write(data)

# Écriture des fichiers
saveme(os.path.join(complete_dir, "src/physijson/main.py"),main_py)
saveme(os.path.join(complete_dir, "src/physijson/validator.py"),validator_py)
saveme(os.path.join(complete_dir, "src/physijson/analyzer.py"),analyzer_py)
saveme(os.path.join(complete_dir, "schemas/experiment.schema.json"),schema_json,True)
saveme(os.path.join(complete_dir, "requirements.txt"),requirements_txt)
rm = "# PhysiJSON – Analyse Scientifique NDJSON\n\nVoir `src/physijson/` pour le code source.\n"
saveme(os.path.join(complete_dir, "README.00_pythontips.md"),rm)

# Création de l'archive ZIP
zip_complete_path = "physijson_solution.zip"
with zipfile.ZipFile(zip_complete_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, _, files in os.walk(complete_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, complete_dir)
            zipf.write(full_path, arcname=os.path.join("physijson_complete", rel_path))