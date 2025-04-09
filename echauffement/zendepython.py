import this #easter egg

#1
def foo(a:str,b:list,c:int) -> int:
    pass

foo("",[],5) # positionnel
foo(c=5,b=[2,2],a=None) # passage par motcle

# 2 Simple
# En plusieurs lignes, variables explicites

# Flat on va une ligne de prod automobile
# -> Neg : plus verbeux, plus de API
# -> Pos : evolutif, flexible

voitures = ("Ferrari","RoveR","Peugeot","Renault","Rolls-royce", "Fiat")
# toutes les marques qui commence par R
# dans l'ordre alphabetique en MAJ

# CONFIG
def maj(s:str):
    return s.upper()
def R_only(s:str):
    return s.startswith("R")

it_voitures = filter(R_only,voitures )
it_voitures = map(maj, it_voitures)

print(list(it_voitures))

a = 10
print(type(maj))
print(type(a))
