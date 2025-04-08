import streamlit as st
import subprocess
import os
import pandas as pd

st.title("✈️ Aircraft Scraper GUI")

method = st.selectbox("Choisissez la méthode de scraping :", [
    "Static HTML (BeautifulSoup)",
    "Structured HTML (lxml/XPath)",
    "JavaScript Dynamic (Playwright)"
])

url = st.text_input("URL de la page à scraper", "https://example.com/flights")

if st.button("Lancer le scraping"):
    st.info(f"Lancement du scraping avec la méthode : {method}")
    if method == "Static HTML (BeautifulSoup)":
        command = f"python scraper_static_bs4.py"
        filename = "flights_bs4.csv"
    elif method == "Structured HTML (lxml/XPath)":
        command = f"python scraper_xpath_lxml.py"
        filename = "flights_xpath.csv"
    else:
        command = f"python scraper_playwright.py"
        filename = "flights_playwright.parquet"

    # Remplacer l'URL dans les scripts (temporairement)
    for script in ["scraper_static_bs4.py", "scraper_xpath_lxml.py", "scraper_playwright.py"]:
        with open(script, "r") as file:
            content = file.read()
        content = content.replace("https://example.com/flights", url).replace("https://example.com/flights-today", url)
        with open(script, "w") as file:
            file.write(content)

    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        st.success("Scraping terminé !")
        # Affiche un aperçu du fichier
        if filename.endswith(".csv"):
            df = pd.read_csv(filename)
        else:
            df = pd.read_parquet(filename)
        st.dataframe(df.head())
    else:
        st.error("Erreur lors de l'exécution du script :")
        st.code(result.stderr)
