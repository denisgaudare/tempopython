# Python tout est un objet
from echauffement.modeles import Occurence, Stats


# list : sequence ordonnee (index)  et modifiable
# tuple : sequence ordonnee et NON modifiable
# set : sequence NON ordonnee et modifiable
# dict : sequence NON ordonnee et modifiable , struct Cle Valeur
    #set->set


# EXTRACTION
def charge_fichier(filename:str) -> list[str]:
    """
    :param filename:
    :return:
    """
    # mieux faire : fonctionnel ET algorithmique
    with open(filename, mode="rt", encoding="utf-8") as file:
        lines = file.read().splitlines() # plutot que readlines()
        # close automatique (enter/exit)
        # nettoyage ?? peut etre si bcp facile
    return lines

# TRANSFORMATION
# choix de la structure !!!
def compute_occurences(lines:list[str]) -> dict:
    occurences = dict() # plutot ue le sugar coding {}
    # defaultdict() est une solution a KeyError

    # amelioration fonctionnelle et algorithmique
    for l in lines:

        # normalizer .....
        # min/majuscule ... accents, caracteres bizarres
        mots = l.split(" ") # ameliorer regex (plus large, plus )
        # normalisation finale
        #qualite de la donnée : echantillon est utile
            # DEBUT FIN DU TEXTE
            # STOP WORDS (LANGUE ??)
        for m in mots:
            if m not in occurences:
                occurences[m] = Stats(m) # fonctionnellement
            occurences[m]+=1


    return occurences # dict


def affiche_resultat(occurences:dict, maxsize=-1):
    # RESTITUTION
    # changer a nouveau la structure
    sorted_occurrences = list(occurences.values()) # triée
    # ('nemo',751)
    sorted_occurrences.sort(reverse=True)
    for occurence in sorted_occurrences[:maxsize]:
        print(occurence)

# actif
if __name__=="__main__": # namespace
    phrases = charge_fichier("../data/pg54873_20000lieues.txt")
    compteur = compute_occurences(phrases)
    affiche_resultat(compteur, -1)

# PEP8 , PEP20

