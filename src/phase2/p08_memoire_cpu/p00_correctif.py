# CORRECTIF car __add__ et __iadd__ different dans
# un objet mutable

# ici on utilise __add__()
a = [2,4,6]
b = [1,3,5]
print(id(a))
a = a + b
print(id(a))

print("-"*20)

# ici on utilise __iadd__()
a = [2,4,6]
b = [1,3,5]
print(id(a))
a+= b
print(id(a))
