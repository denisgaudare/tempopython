listA = ["FORD","renault","peugeot","Fiat","ferrari","citroen", "lamborghini"]

# afficher en majuscule les marques commencant par f et ensuite tries


marques = []
for m in listA:
    if m.startswith("F") or m.startswith("f"):
        marques.append(m.upper())

marques.sort()
for m in marques:
    print(m)

# ------------------------
maj = lambda s: s.upper()
only_f = lambda s : s.startswith("F")
plus_4 = lambda s : len(s)>4
tri_taille = lambda marque: -1*len(marque)

def tri_f(marque):
    if marque[0] > "F":
        return "0"+marque
    return "ZZZZZZZ" + marque

# STEP1
m =list(map(maj, listA))
# STEP2
f = list(filter(plus_4,m))
# STEP3
s = sorted(f, key=tri_f)
# STEP4
print(s)

