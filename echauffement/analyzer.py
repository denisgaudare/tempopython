from collections import Counter

from echauffement.decorateurs import timing_val


def read_lines_from_file(filename: str) -> list[str]:
    """
    :param filename:
    :return:
    """
    # risque starvation/affamer les ressources
    try:
        file = open(filename, mode="rt", encoding="utf-8")  # DEBUT
        lines = file.read().splitlines()  # plutot que readlines()
    finally:
        if file:
            file.close()  # END

    return lines

    # TRANSFORMATION
    # choix de la structure !!!



@timing_val
def compute_occurences(lines: list[str]) -> dict:
    mots = []
    for l in lines:
        mots.extend(l.split(" "))
        #mots = mots + l.split(" ")
        #mots = [*mots , *list.split(" ")]

    return Counter(mots)

def compute_occurences_old(lines: list[str]) -> dict:
    occurences = dict()
    for l in lines:
        # normalizer .....
        mots = l.split(" ")  # ameliorer (plus large)
        for m in mots:
            if m in occurences:
                occurences[m] += 1
            else:
                occurences[m] = 1
    return occurences
def affiche_resultat(occurences: dict, maxsize=100):
    # RESTITUTION
    # changer à nouveau la structure
    sorted_occurrences = list(occurences.items())
    sorted_occurrences.sort(key=lambda kv: kv[1], reverse=True)
    for o in sorted_occurrences[:maxsize]:
        print(o)
