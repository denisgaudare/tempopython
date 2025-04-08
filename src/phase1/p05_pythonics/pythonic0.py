from pathlib import Path

a = 10
a = a * 5


b = "A"
b = b * 5

c = [1,2,3]
c = c * 10
print(c)


p = Path("C:/Windows")
p =p / "System32"
print(p)


seta= {1,2,3,4,5}
setb = {4,5,6,7,8}

s1 = seta.difference(setb)
s2 = setb.difference(seta)
print(s1)

print(s2)

print(seta - setb)