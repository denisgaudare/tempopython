import json

import typer
from jsonschema import validate, ValidationError

app =typer.Typer()

@app.command()
def validate(file_path:str, schema_path:str):
    pass


@app.command()
def analyze(file_path:str):
    pass

if __name__ == "__main__":
    app()
