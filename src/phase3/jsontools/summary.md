**JSON** et du **NDJSON**, avec des exemples progressifs pour chaque cas d’usage courant : lecture, écriture, transformation, validation, conversion, streaming, etc.

---

## 🔧 **Outils courants pour JSON/NDJSON**

### 1. **json** (standard library)
- 📦 Inclus de base avec Python
- ✅ Lecture/écriture JSON classique
```python
import json

# Lire un fichier JSON
with open("data.json") as f:
    data = json.load(f)

# Écrire dans un fichier JSON
with open("output.json", "w") as f:
    json.dump(data, f, indent=2)

# Transformer une string JSON
data = json.loads('{"name": "Alice"}')
json_str = json.dumps(data, indent=2)
```

---

### 2. **pandas**
- 🧮 Très pratique pour NDJSON ou objets plats
- ✅ Lit/écrit JSON lignes (`lines=True`)
```python
import pandas as pd

# Lire un fichier NDJSON
df = pd.read_json("data.ndjson", lines=True)

# Écrire un NDJSON à partir d’un DataFrame
df.to_json("out.ndjson", lines=True, orient="records")
```

---

### 3. **ndjson**
- 📦 `pip install ndjson`
- ✅ Lecture/écriture directe en NDJSON
```python
import ndjson

with open("data.ndjson") as f:
    data = ndjson.load(f)  # Liste de dicts

# Transformation
for item in data:
    item["processed"] = True

# Écriture
with open("output.ndjson", "w") as f:
    ndjson.dump(data, f)
```

---

### 4. **orjson**
- 📦 `pip install orjson`
- ⚡ Ultra rapide, compatible numpy, dataclasses, etc.
- ⚠️ Retourne des `bytes`, à décoder
```python
import orjson

data = {"a": 1, "b": [1, 2, 3]}
json_bytes = orjson.dumps(data)
print(json_bytes.decode())  # '{"a":1,"b":[1,2,3]}'

# Lecture
data = orjson.loads(json_bytes)
```

---

### 5. **ujson (UltraJSON)**
- 📦 `pip install ujson`
- ⚡ Très rapide (moins que orjson, mais plus souple)
```python
import ujson

with open("data.json") as f:
    data = ujson.load(f)

json_str = ujson.dumps(data)
```

---

### 6. **jsonlines**
- 📦 `pip install jsonlines`
- ✅ Lecture/écriture de NDJSON ligne par ligne
```python
import jsonlines

with jsonlines.open("data.ndjson") as reader:
    for obj in reader:
        print(obj)

with jsonlines.open("output.ndjson", mode="w") as writer:
    writer.write_all([{"a": 1}, {"b": 2}])
```

---

### 7. **jsonschema**
- 📦 `pip install jsonschema`
- ✅ Validation contre un schéma JSON Schema
```python
from jsonschema import validate, ValidationError

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
    },
    "required": ["name"]
}

data = {"name": "Alice", "age": 30}

try:
    validate(instance=data, schema=schema)
    print("Valide !")
except ValidationError as e:
    print("Erreur :", e.message)
```

---

### 8. **ijson**
- 📦 `pip install ijson`
- ✅ Parsing **streaming** (JSON énormes)
```python
import ijson

with open("large.json") as f:
    for item in ijson.items(f, "items.item"):
        print(item)  # Lit chaque élément d’un tableau "items"
```

---

### 9. **jsonpath-ng**
- 📦 `pip install jsonpath-ng`
- 🔎 Extraction avancée de données avec expressions JSONPath
```python
from jsonpath_ng import jsonpath, parse

data = {
    "store": {
        "book": [
            {"title": "Book A", "price": 10},
            {"title": "Book B", "price": 15},
        ]
    }
}

jsonpath_expr = parse("$.store.book[*].title")
for match in jsonpath_expr.find(data):
    print(match.value)
```

---

### 10. **marshmallow**
- 📦 `pip install marshmallow`
- ✅ Sérialisation, validation, transformation de schémas complexes
```python
from marshmallow import Schema, fields

class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer()

user_data = {"name": "Alice", "age": 30}
schema = UserSchema()
result = schema.dump(user_data)
print(result)  # -> {'name': 'Alice', 'age': 30}
```

---

### Bonus : Conversion CSV ↔ JSON
```python
import csv
import json

# CSV → JSON
with open("data.csv") as f:
    reader = csv.DictReader(f)
    data = list(reader)

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# JSON → CSV
with open("data.json") as f:
    data = json.load(f)

with open("output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
```

---
