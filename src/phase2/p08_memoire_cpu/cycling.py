import objgraph # necessite graphviz

class A:
    pass

class B:
    pass

class C:
    pass


a = A()
b = B()
c = C()
a.b = b
b.a = a  # cycle de référence
c.a = a
b.c = c

# Montre les objets les plus nombreux
objgraph.show_most_common_types()


# Trace les références à l'objet `a`
objgraph.show_backrefs([b],filename="cycling.png")
