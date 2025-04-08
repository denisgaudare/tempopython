prenom1 = "Bruno"
prenom2 = "Arnaud"
prenom3 = "Bruno"

print(id(prenom1))
print(id(prenom3))

prenom3 = "Gabriel"
print(prenom1)

bm = prenom1.upper()
print(prenom1,bm)

del prenom1


# non mutable
t = (1,2,3)



from functools import reduce

help(reduce)


numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)  # 10

