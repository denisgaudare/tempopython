import os
import pandas as pd

from commontools.consoles import pause


# Fonction pour afficher le DataFrame en entier à chaque étape
def print_full(df, titre=""):
    print(f"\n🟢 {titre}")
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df)

# 1. Création du DataFrame de départ
data = {
    "nom": ["Alice", "Bob", "Charlie", "David", "Eva","David"],
    "age": [25, 30, 35, 40, 45, 25],
    "ville": ["Paris", "Lyon", "Marseille", "Paris", "Lyon","Toulouse"],
    "revenu": [3000, 2500, 4000, 3500, 2700, 5000],
}

df = pd.DataFrame(data)
print_full(df, "1️⃣ DataFrame initial")

pause()

# 2. Renommer des colonnes
df = df.rename(columns={"nom": "prenom", "ville": "localisation"})
print_full(df, "2️⃣ Renommage des colonnes")
pause()

# 3. Ajouter une colonne calculée
df["revenu_annuel"] = df["revenu"] * 12
print_full(df, "3️⃣ Ajout de la colonne 'revenu_annuel'")
pause()

# 4. Supprimer une colonne
df = df.drop(columns=["revenu"])
print_full(df, "4️⃣ Suppression de la colonne 'revenu'")
pause()

# 5. Modifier une cellule précise
df.loc[df["prenom"] == "Eva", "age"] = 46
df["csp"] = ""
df.loc[df["revenu_annuel"] > 40000 , "csp"] = "A"
print_full(df, "5️⃣ Correction de l’âge d’Eva")
pause()

# 6. Trier par revenu annuel
df = df.sort_values(by="revenu_annuel", ascending=False)
print_full(df, "6️⃣ Tri décroissant par revenu annuel")
pause()

# 7. Agrégation : revenu moyen par ville
revenu_par_ville = df.groupby("localisation")["revenu_annuel"].mean()
print_full(revenu_par_ville, "7️⃣ Moyenne du revenu annuel par ville")
pause()

# 8. Jointure avec un autre DataFrame
infos_villes = pd.DataFrame({
    "localisation": ["Paris", "Lyon", "Marseille"],
    "population": [2200000, 500000, 870000]
})

df = df.merge(infos_villes, on="localisation", how="left")
print_full(df, "8️⃣ Ajout des populations des villes")
pause()

# 9. Application d’une fonction avec apply()
df["categorie_age"] = df["age"].apply(lambda x: "jeune" if x < 35 else "senior")
print_full(df, "9️⃣ Catégorisation des âges")
pause()

# 10. Remplir les valeurs manquantes (ici fictif)
df["revenu_annuel"] = df["revenu_annuel"].fillna(0)
print_full(df, "🔟 Vérification/remplissage des valeurs manquantes")
pause()

# 11. Filtrage avec query
df_jeunes_riches = df.query("categorie_age == 'jeune' and revenu_annuel > 30000")
print_full(df_jeunes_riches, "1️⃣1️⃣ Filtrage des jeunes avec revenu annuel > 30 000")
pause()
