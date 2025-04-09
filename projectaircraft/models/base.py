class AutoReprMeta(type):
    def __new__(cls, name, bases, dct):
        if '__repr__' not in dct:
            def __repr__(self):
                attrs = ', '.join(
                    f"{key}={getattr(self, key)!r}" for key in self.__dict__
                )
                return f"**{self.__class__.__name__}({attrs})"
            dct['__repr__'] = __repr__
        return super().__new__(cls, name, bases, dct) #!!!!


class NoInheritanceMeta(type):
    """Métaclasse empêchant l'héritage de la classe."""

    def __new__(cls, name, bases, class_dict):
        if any(isinstance(base, NoInheritanceMeta) for base in bases):
            raise TypeError(f"❌ La classe '{name}' ne peut pas hériter d'une classe utilisant NoInheritanceMeta.")
        return super().__new__(cls, name, bases, class_dict)


class BaseModel(metaclass=AutoReprMeta):
    pass