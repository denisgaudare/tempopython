import time
from process_pandas import process_flights_pandas
from process_polars import process_flights_polars

def benchmark(name, func):
    t0 = time.time()
    result = func()
    duration = time.time() - t0
    print(f"{name} → {duration:.3f} sec")
    return result

if __name__ == "__main__":
    pandas_result = benchmark("Pandas", process_flights_pandas)
    polars_result = benchmark("Polars", process_flights_polars)

    print("\nRésultat Pandas:\n", pandas_result.head())
    print("\nRésultat Polars:\n", polars_result.head())
