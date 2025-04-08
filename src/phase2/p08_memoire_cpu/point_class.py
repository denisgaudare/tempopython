class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def initp():
    pass

p = Point(0,0)
p.z = 5
p.a = [1,2,3,4,5]
p.foo = initp
print(p.__dict__)


class PointS:
    __slots__ = ('x', 'y')  # pas de __dict__
    def __init__(self, x, y):
        self.x = x
        self.y = y

ps = PointS(1,1)
print(ps.__slots__)
