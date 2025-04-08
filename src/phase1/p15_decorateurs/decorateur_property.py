"""
a = 10
def geta():
    global a
    return a
def seta(x):
    global a
    if x>=0:
        a=x

class X:
    def __init__(self):
        self.a = 5
        self._b = 10
        self.__c = 20
    def get_b(self):
        return self._b
    def get_c(self):
        return self.__c

x = X()
x.__c = 5  # creer une autre variable
print(x.__c, x.get_b(),x.get_c())

class C(object):

    def __init__(self):
        self.x = property()
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        if value>=0:
            self.__x = value
    @x.deleter
    def x(self):
        raise NotImplemented()
        del self.__x

    @property
    def secret(self):
        if 0 == self.__x:
            return "12345678"
        else:
            return "********"
c = C()
c.x = 10
c.x = 0
del c.x

a = 10
del a
print(a)

"""
def intercal(func):
    def wrapper():   # fct interne (a la fois closure)
        print("INTER")
        func()
    return wrapper


def foo(n=5):
    print("FOO"+str(n))

def fct_base(a,b,c):
    pass

fct_base(1,2,3) # positionnel
fct_base(c=3,a=1,b=2) # keyword
fct_base(1, c=3,b=2) # keyword

def fct_arguments1(a,b, *args): #
    print(args)

fct_arguments1(1,2)
fct_arguments1(1,2,5,8,7)
def affiche_infos(**kvargs):
    for k,v in kvargs.items():
        print("Variable %s vaut  %s " % (k,v))

affiche_infos(nom="Grebil",prenom="Nathalie", societe="Ansys")
affiche_infos(heure=9,minute=45)


def fct(*args,**dargs):
    print(args)
    print(dargs)

fct(1,2, nom="ivan", dep="hl")