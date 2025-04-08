import os


def fauxcontext(param):
    return "HELLO "+param

class MonContext():

    def __init__(self, prenom):
        self.msg = prenom

    def __enter__(self):
        if self.msg is None:
            self.msg = "Bonjour tout le monde"
        print("ENTER")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # nettoyage et controle
        if exc_tb:
            print("Sortie en erreur")
        print(exc_type, exc_val, exc_tb)

with MonContext(None) as texte:
    #raise TypeError()
    print(texte.msg)



from contextlib import ContextDecorator # hybride

class ForceConfig(ContextDecorator):

    def __init__(self,rep):
        self.exist_avant = True
        self.rep = rep
    def __enter__(self):
        if not os.path.isfile("config.txt"):
            f = open("config.txt",mode="wt")
            f.write("DATA")
            f.close()
            self.exist_avant = False
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if not self.exist_avant:
            os.remove("config.txt")

with ForceConfig("../data") as force:
    print(force.exist_avant)
    print(force.rep)


