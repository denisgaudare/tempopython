
class Occurence:
    def __init__(self,mo,oc=0):
        self.mot = mo
        self.occurence = oc

    def increment(self):
        self.occurence+=1

    def __str__(self):
        return f"{self.mot} apparait {self.occurence} fois"

    def __lt__(self, occu):
        return self.occurence < occu.occurence

    def __eq__(self, occu):
        return self.occurence == occu.occurence

    def __iadd__(self, value):
        if isinstance(value,int):
            self.occurence+=value
        elif isinstance(value,Occurence):
            self.occurence += value.occurence
        else:
            raise ArithmeticError("Erreur de type de donnnees")
        return self

    def __add__(self, value):
        newocc = Occurence(self.mot,self.occurence)
        if isinstance(value, int):
            newocc.occurence += value
        elif isinstance(value, Occurence):
            newocc.occurence += value.occurence
        else:
            raise ArithmeticError("Erreur de type de donnnees")
        return newocc

    def __int__(self):
        return self.occurence

class Stats(Occurence):

    def __str__(self):
        return f"{self.mot}:{self.occurence}"

    def __repr__(self):
        return f"{self.mot if self.mot else "N/A"}:{self.occurence}"
