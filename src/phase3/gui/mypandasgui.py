import pandas as pd
from pandasgui import show

# Create some example data
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Paris', 'London', 'Berlin']
})

df2 = pd.DataFrame({
    'Product': ['Widget', 'Gadget', 'Thingy'],
    'Price': [19.99, 29.99, 9.99]
})

# Launch the GUI with both dataframes
gui = show(df1=df1, df2=df2)

# This line is necessary to keep the GUI open when not in a notebook
gui.app.exec_()