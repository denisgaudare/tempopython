class MetaA(type):
    def __new__(cls, name, bases, class_dict):
        print("MetaA is applied")
        return super().__new__(cls, name, bases, class_dict)

# Métaclasse 2
class MetaB(type):
    def __new__(cls, name, bases, class_dict):
        print("MetaB is applied")
        return super().__new__(cls, name, bases, class_dict)

# Métaclasse combinée héritant des deux
class CombinedMeta(MetaA, MetaB):
    pass

# Classe utilisant la métaclasse combinée
class MyClass(metaclass=CombinedMeta):
    pass


MyClass()

class Aa:
    def __init__(self):
        super().__init__()

class Bb(Aa):
    def __init__(self):
        super().__init__()
class Cc(Aa):
    def __init__(self):
        super().__init__()
class D(B, C):  # ⚠️ Héritage multiple
    def __init__(self):
        print("Init D")
        #super().__init__()  # Appelle B, puis C, puis A
        Aa.__init__(self)