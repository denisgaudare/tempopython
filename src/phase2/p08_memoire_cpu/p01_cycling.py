import sys

a = []
b = a
print(sys.getrefcount(a))

class Node:
    def __init__(self):
        self.ref = self

a = Node()
print(sys.getrefcount(a))

