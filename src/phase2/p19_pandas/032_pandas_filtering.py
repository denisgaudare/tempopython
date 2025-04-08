### ✈️ Exemple de DataFrame : `df_airports`

df_airports = pd.DataFrame(data)

### 🔍 Exemples de **filtrage**

#### 1. Aéroports situés dans l'hémisphère nord
df_airports[df_airports['latitude'] > 0]


#### 2. Aéroports à l'ouest du méridien de Greenwich (longitude négative)
df_airports[df_airports['longitude'] < 0]

#### 3. Aéroports dont le nom contient "Intl"
df_airports[df_airports['airport_name'].str.contains("Intl")]

#### 4. Aéroports dont le code est soit CDG soit LHR
df_airports[df_airports['airport_code'].isin(['CDG', 'LHR'])]

#### 5. Aéroports entre 30° et 50° de latitude
df_airports[df_airports['latitude'].between(30, 50)]

#### 6. Aéroports à l'est de 50° de longitude ET au sud de 40° de latitude
df_airports[(df_airports['longitude'] > 50) & (df_airports['latitude'] < 40)]

#### 7. Avec `query()` : aéroports situés à l’ouest (longitude < 0)
df_airports.query("longitude < 0")

