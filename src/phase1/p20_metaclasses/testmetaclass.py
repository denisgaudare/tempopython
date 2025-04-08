# metaclass
#

ty = type(5)
print(ty)
print(type(ty))

def hello():
    print("Hello "*3)

# creer une class dynamiquement
P = type('Personne', (), {"a":1, "coucou":hello}) # creer
print(P, P.a)
P.coucou()
print(P.__class__.__name__)
print(type(P)) # info

class MetaCheckAttributes(type):
    def __new__(cls, name, bases, dct):
        if "active" not in dct:
            raise TypeError(f"La classe {name} doit avoir 'active'")
        return super().__new__(cls, name, bases, dct)


def estunefoo():
    pass

print(type(estunefoo))


class Conforme(metaclass=MetaCheckAttributes):
    active = "Présent"


"""class PasConforme(metaclass=MetaCheckAttributes):
    data = "Présent"""""


class SingletonMeta(type):
    """Métaclasse pour implémenter le pattern Singleton"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """S'assure qu'une seule instance est créée"""
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

# Classe utilisant la métaclasse Singleton
class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

class Test(metaclass=SingletonMeta):
    pass

# Test du singleton
obj1 = SingletonClass("Premier")
obj2 = SingletonClass("Deuxième")
obj3 = Test()
obj4 = Test()

print(obj1.value)  # Affiche "Premier"
print(obj2.value)  # Affiche "Premier"
print(obj1 is obj2)
print(obj3 is obj4)# True, c'est bien la même instance !

