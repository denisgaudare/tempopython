from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import textwrap

# Préparation des données
periods = [
    {
        "title": "Médiévale (env. 500–1400)",
        "carac": "Monodie (chant grégorien), premières polyphonies (organum, motet).",
        "solfege": "Utilisation des modes grégoriens (dorien, phrygien...), absence de mesure régulière, notation neumatique.",
        "ex": "Exemple : Kyrie de la Messe de Notre-Dame – Guillaume de Machaut.\n- Mode : souvent dorien.\n- Ambitus étroit, mélismes.",
    },
    {
        "title": "Renaissance (env. 1400–1600)",
        "carac": "Polyphonie vocale imitative, recherche d'équilibre et d'expression.",
        "solfege": "Contrepoint strict, encore basé sur les modes, mesures régulières.",
        "ex": "Exemple : Ave Maria – Josquin des Prez.\n- Imitation entre voix.\n- Cadences modales (souvent plagales).",
    },
    {
        "title": "Baroque (1600–1750)",
        "carac": "Naissance de la tonalité, basse continue, stylus fantasticus.",
        "solfege": "Tonalité (majeur/mineur), cadences parfaites, ornementation.",
        "ex": "Exemple : Toccata en ré mineur – J.S. Bach.\n- Liberté formelle.\n- Cadences V-I claires, séquences.",
    },
    {
        "title": "Classique (1750–1820)",
        "carac": "Clarté formelle, équilibre, forme sonate.",
        "solfege": "Périodes régulières (4+4 mesures), tonalité fonctionnelle, modulation vers dominante.",
        "ex": "Exemple : Sonate K545 – Mozart.\n- Forme sonate.\n- Modulation I → V → I.",
    },
    {
        "title": "Romantique (1820–1900)",
        "carac": "Expression individuelle, élargissement harmonique.",
        "solfege": "Modulations fréquentes, accords enrichis (7e, 9e, napolitaine), rubato.",
        "ex": "Exemple : Prélude en mi mineur – Chopin.\n- Harmonies chromatiques.\n- Liberté rythmique.",
    },
    {
        "title": "Moderne (1900–1945)",
        "carac": "Exploration (atonalité, modes nouveaux, polytonalité).",
        "solfege": "Gammes par tons, modes à transposition limitée, série dodécaphonique.",
        "ex": "Exemple : Voiles – Debussy.\n- Gamme par tons.\n- Ambiguïté tonale.",
    },
    {
        "title": "Contemporaine (1945–...)",
        "carac": "Expérimentation (musique électronique, aléatoire, minimalisme).",
        "solfege": "Graphismes libres, absence de pulsation, polyrythmies.",
        "ex": "Exemple : Clapping Music – Steve Reich.\n- Phase rythmique.\n- Pas de mélodie traditionnelle.",
    }
]

# Création du PDF sans emojis
pdf_path = "Frise_musique_et_solfege_sans_emoji.pdf"
pdf = PdfPages(pdf_path)

for period in periods:
    plt.figure(figsize=(11, 8.5))
    plt.axis("off")

    title = period["title"]
    carac = textwrap.fill(f"Caractéristiques : {period['carac']}", width=90)
    solfege = textwrap.fill(f"Solfège : {period['solfege']}", width=90)
    example = textwrap.fill(f"Exemple d’analyse :\n{period['ex']}", width=90)

    plt.text(0.5, 0.95, title, fontsize=18, ha='center', va='top', weight='bold')
    plt.text(0.05, 0.85, carac, fontsize=12)
    plt.text(0.05, 0.70, solfege, fontsize=12)
    plt.text(0.05, 0.45, example, fontsize=12)

    pdf.savefig()
    plt.close()

pdf.close()
