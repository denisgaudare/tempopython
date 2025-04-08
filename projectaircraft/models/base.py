class AutoReprMeta(type):
    def __new__(cls, name, bases, dct):
        # TODO : rajouter la fonction __repr__
            if '__repr__' not in dct:
                def myrepr():
                    #return str avec les attributs et les valeurs d'un objet'


                dct=["__repr__"] = myrepr

class Q(metaclass=AutoReprMeta):
    def __repr__(self): # oriente debug dev
        return f"{self.a} , {self.a}"


class R(metaclass=AutoReprMeta):
    pass

r = R()
print(r)
