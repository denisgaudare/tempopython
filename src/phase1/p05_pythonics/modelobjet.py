from  datetime import *

textf = open('../../../data/kitten.jpg', 'rb')
print(type(textf))
textf.close()

print(type(datetime))


class Occurence:
    def __init__(self,mo,oc):
        self.mot = mo
        self.occurence = oc

    def increment(self):
        pass

    def __str__(self):
        return f"{self.mot} apparait {self.occurence} fois"

