class Info:

    def __init__(self, desc:str):
        self.__description = desc
    @property
    def description(self):
        if self.__description:
            return self.__description
        else:
            return "N/A"

class Celsius:
    def __init__(self, temperature=0):
        self.__temperature = None
        self.__tmp(temperature)
        if not self.__temperature:
            raise ValueError(str(temperature))
    @property
    def temperature(self):
        print("Récupération de la température")
        return self.__temperature

    @temperature.setter
    def temperature(self,t):
        self.__tmp(t)

    def __tmp(self,t):
        if t >= 0:
            self.__temperature = t
        else:
            print("Impossible modifier si<0")


i = Info(None)
print(i.description)

# Utilisation
c = Celsius(-25)
print(c.temperature)
print(type(c.temperature))
print(c.temperature)  # Récupération de la température
c.temperature = -30    # Mise à jour de la température
print(c.temperature)