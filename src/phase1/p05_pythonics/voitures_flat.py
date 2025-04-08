

class Voiture:
    def __init__(self,id,name,type,cv,color):
        self.id = id
        self.color = color
        self.name = name

    def fonction_erronne(self):
        raise NotImplementedError()

v1= Voiture(1,"clio","urbaine",4,"ROUGE")
v2= Voiture(1,"ferrari","sportive",40,"rouge")
v3= Voiture(1,"honda","berline",20,"bleu")
voitures = {v1,v3,v2}
print(type(voitures))

def dosomething():
    print("Je fais qque chose")

v3.fonction_erronne = dosomething # monkey patch
v3.fonction_erronne()

#NESTED
red_only = []
for v in voitures:
    if v.color=="rouge":
        red_only.append(v)
        print(v.name.upper(), v.color)

# FLAT (plus de flexibilite, lisibilite -> main
it1 = filter(lambda v:v.color=="rouge", voitures)
it2 = map(lambda v:(v.name.upper(), v.color), it1)
red_only = list(it2)
print(red_only)