
import sys
from pathlib import Path
import nbformat
import pandas as pd
import numpy as np
import pandasgui as pgui

def print_full(x,message=None):
    if message:
        tirets = "-" * len(message)
        print(tirets + "\n"+message+"\n"+tirets)
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')

# Contenu du notebook structuré
"""🐼 Pandas pour développeurs Python
Ce notebook présente les fonctions principales 
de Pandas à travers des exemples concrets."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Simuler un petit jeu de données
data = {
    'id': np.arange(1, 11),
    'date': pd.date_range(start='2023-01-01', periods=10),
    'value': np.random.randint(50, 200, size=10)
    }

df = pd.DataFrame(data)

# 1. Chargement & exploration
#pgui.show(df)
print(df.head())

df.info()

df.describe()

# 2. Filtrage & sélection

df_filtre = df[df['value'] > 100]
with pd.option_context('display.max_rows', None,
                       'display.max_columns', None):
    # more options can be specified also
    print(df_filtre)


df_loc = df.loc[df['date'] > '2023-01-05', ['id', 'value']]
print(df_loc.to_string())

# 3. Transformation & colonnes calculées
df['ratio'] = df['value'] / df['value'].sum()
df['label'] = df['value'].apply(lambda x: 'High' if x > 100 else 'Low')
print_full(df,"Transform & Calc")

# 4. GroupBy & agrégation
df_mean = df.groupby('label')['value'].agg(['mean', 'sum'])
print_full(df_mean, "GroupBy & Agr")

# 5. Pivot & reshape
df_pivot = df.pivot_table(index='id', columns='label', values='value', aggfunc='sum')
print_full(df_pivot,"Pivot & Reshape")

# 6. Visualisation simple
df['value'].plot(kind='hist', bins=10, title='Distribution des valeurs')
plt.xlabel('valeur')
plt.show()

# 7. Bonus : tri et top 5
df_sort = df.sort_values('value', ascending=False).head()
print_full(df_sort,"Tri externe")

