import pandas as pd

# Lecture
df = pd.read_parquet("data.parquet", engine="pyarrow")  # ou "fastparquet"

# Écriture
df.to_parquet("out.parquet", engine="pyarrow")