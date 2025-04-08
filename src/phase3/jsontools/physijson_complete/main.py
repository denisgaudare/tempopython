import os

import typer
from validator import validate_file
from analyzer import analyze_experiments

app = typer.Typer()

@app.command()
def validate(input_file: str, schema_file: str):
    validate_file(input_file, schema_file)

@app.command()
def analyze(input_file: str):
    analyze_experiments(input_file)

if __name__ == "__main__":
    app()