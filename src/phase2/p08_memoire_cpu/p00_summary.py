import sys


def myfoo():
    # allocation
    a = [ i for i in range(1000)]


myfoo()
del myfoo # efface


class A():
    pass

# del sur une classe
a = A()
del A
print(a)
#  b = A()


c = []
print(sys.getrefcount(c))
d = c
print(sys.getrefcount(c))
