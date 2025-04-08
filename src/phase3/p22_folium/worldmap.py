
# import the library
import folium
import pandas as pd

# Make an empty map
m = folium.Map(location=[20,0], tiles="OpenStreetMap", zoom_start=2)

"""
jfile = "..\\p19_pandas\\miniproject\\flights_full.json"
flights = pd.read_json(jfile,orient="split")
"""
cfile = "..\\p19_pandas\\miniproject\\airports.csv"
airports = pd.read_csv(cfile)

for index, info in airports.iterrows():
    folium.Marker([info["latitude"], info["longitude"]], popup=info["airport_name"]).add_to(m)

m.show_in_browser()