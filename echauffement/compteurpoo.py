from dataclasses import dataclass
import bisect

from echauffement.analyzer import (read_lines_from_file, compute_occurences, affiche_resultat)


@dataclass
class Statistiques():  # dico
    mot: str = None
    compteur: int = 0

    """ Stats represente un donnee de statistiques"""

    def __eq__(self, other): # lower than
        return not self.__gt__(other) and not self.__lt__(other)

    def __gt__(self, other): # lower than
        if isinstance(other,Statistiques):
            return self.compteur > other.compteur
        if isinstance(other,(int,float)):
            return self.compteur > other
        raise ValueError(other)

    def __lt__(self, other): # lower than
        if isinstance(other,Statistiques):
            return self.compteur < other.compteur
        if isinstance(other,(int,float)):
            return self.compteur < other
        raise ValueError(other)


class Collecteur:
    def __init__(self, iterable=None):
        """Initialise avec une eventuelle liste triée"""
        self._data = sorted(iterable) if iterable else []

    def append(self, value:Statistiques):
        """Ajoute un élément à sa position correcte
        grace a un system de tri automatique"""
        bisect.insort(self._data ,value)
    def extend(self, iterable):
        """Ajoute plusieurs éléments de manière optimisée"""
        bisect.bisect(self._data , iterable)
    def __getitem__(self, index):
        return self._data[index]
    def __len__(self):
        return  len(self._data)
    def __repr__(self):
        return f"Ce collecteur contient {len(self._data):05d}"
    def __str__(self):
        return self.__repr__()


class Export():

    def __init__(self):
        pass

    def export(self,destination):
        pass


class ExportExcel(Export):

    def export(self, destination):
        pass


if __name__=="__main__": # namespace
    phrases = read_lines_from_file("../data/pg17989_comte.txt")
    compteur = compute_occurences(phrases)
    affiche_resultat(compteur)
