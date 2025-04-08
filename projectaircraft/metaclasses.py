class NoInheritanceMeta(type):
    """Métaclasse empêchant l'héritage de la classe."""

    def __new__(cls, name, bases, class_dict):
        if any(isinstance(base, NoInheritanceMeta) for base in bases):
            raise TypeError(f"❌ La classe '{name}' ne peut pas hériter d'une classe utilisant NoInheritanceMeta.")
        return super().__new__(cls, name, bases, class_dict)