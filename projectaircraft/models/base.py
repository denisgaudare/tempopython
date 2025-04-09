class AutoReprMeta(type):
    def __new__(cls, name, bases, dct):
        # TODO : rajouter la fonction __repr__
            if '__repr__' not in dct:
                """def myrepr():
                    pass
                    #return str avec les attributs et les valeurs d'un objet'
                dct['__repr__'] = myrepr
                """
                print("Merci d'implementer REPR pour "+name)
            return super().__new__(cls, name, bases, dct)


class NoInheritanceMeta(type):
    """Métaclasse empêchant l'héritage de la classe."""

    def __new__(cls, name, bases, class_dict):
        if any(isinstance(base, NoInheritanceMeta) for base in bases):
            raise TypeError(f"❌ La classe '{name}' ne peut pas hériter d'une classe utilisant NoInheritanceMeta.")
        return super().__new__(cls, name, bases, class_dict)


class BaseModel(metaclass=AutoReprMeta):
    pass