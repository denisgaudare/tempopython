
import pandas as pd
from pandasgui import show

df = pd.read_json('flights_full.json', orient="split")
show(df)