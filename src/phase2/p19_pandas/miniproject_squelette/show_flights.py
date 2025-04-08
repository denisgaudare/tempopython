
import pandas as pd
from pandasgui import show

from commontools.consoles import pause
from distances import karney_distance

df = pd.read_csv('flights.csv')
show(df)

pause()

df = pd.read_json('flights_full.json', orient="split")
show(df)