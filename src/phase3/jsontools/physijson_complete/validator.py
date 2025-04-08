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
