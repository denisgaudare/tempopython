class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"__new__ : Création de {name}")
        dct["new_attribute"] = "Ajouté par Meta"
        return super().__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print(f"__init__ : Initialisation de {name}")
        super().__init__(name, bases, dct)

class MyClass(metaclass=Meta):
    pass

print(MyClass.new_attribute)



class MetaCheckAttributes(type):
    def __new__(cls, name, bases, dct):
        if "id" not in dct:
            raise TypeError(f"La classe {name} doit avoir 'id'")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MetaCheckAttributes):
    id = "Présent"


# Vérifie que l'attribut a bien été ajouté

c = MyClass()


class SingletonMeta(type):
    """Métaclasse pour implémenter le pattern Singleton"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """S'assure qu'une seule instance est créée"""
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Quelconque(metaclass=SingletonMeta):
    pass

    def __init__(self,q=None):
        self.que = q

q1 = Quelconque("QUELCONQUE")
q1.val = 10
q2 = Quelconque()
print(id(q1),id(q2))
print(q2.val, q1.que, q2.que)



class DoNotInheritMeta(type):
    def __new__(cls, name, bases, class_dict):
        if any(isinstance(base, DoNotInheritMeta) for base in bases):
            raise TypeError(f"La classe {name} ne peut pas hériter de {bases[0].__name__}")
        return super().__new__(cls, name, bases, class_dict)

class FinalClasse(metaclass=DoNotInheritMeta):
    pass

class Derived(FinalClasse):  # Erreur !
     pass

class A():

    def calcA(self):
        pass

class B():

    def calcB(self):
        pass

class C():

    def __init__(self):
        self.a = A()
        self.b = B()
    def calcA(self):
        return self.a.calcA()

    def calcB(self):
        return self.b.calcB()
