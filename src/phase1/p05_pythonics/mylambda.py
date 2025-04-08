

def flong(x):
    return (x+3)**2

fshort = lambda z:(z+3)**2

mots = ["aaaa","bb","dd","cccccccc","d"]
mots.sort()

def selecteur(chaine):
    return len(chaine)

mots.sort(key=lambda x:len(x))
print(mots)


_,prenom, _ = ("Arnaud","Rigolle","12345678")
print(prenom)


def mafct():

    PI = 3.14159
    lmultiple = lambda x,y:(x+y)**2 * PI

    return lmultiple

x = mafct()
print(type(x))

print(x(1,2))