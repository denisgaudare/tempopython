import math
import random
import time


def simulateur_capteur():
    while True:
        yield random.uniform(20.0, 25.0)
        time.sleep(1)

capteur = simulateur_capteur()
for _ in range(2):
    print(next(capteur))

def lire_f(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        yield f.readline()

def lire_fichier(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:

        yield f.readline().strip() # StopIteration a la fin

def filtrer_by_calc(data,func):
    for n in data:
        if func(n) > 0:
            yield n

def calcul_a_tester(n): # calcul
    return (-500 + n**3)
nombres = range(1,1000) # data
#nombres_ok = filtrer_by_calc(nombres, calcul_a_tester) # au fil de l'eau
nombres_ok = filtrer_by_calc(nombres, lambda x:-100+x/2)
for p in nombres_ok:
    print(p)


def extraire_mots(lignes):
    for ligne in lignes:
        for mot in ligne.split():
            yield mot.lower()

def filtrer_mots_courts(mots):
    for mot in mots:
        if len(mot) > 3:
            yield mot

lignes = [
    "Ceci est une ligne de test",
    "Les générateurs sont puissants en PYTHON"
]

#FLAT RATHER THAN EMBEDDED
mots = extraire_mots(lignes)
mots_filtres = filtrer_mots_courts(mots) # generateur utilise un autre gen

for mot in mots_filtres:
    print(mot)