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
            #formula = record.get("formula")
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
