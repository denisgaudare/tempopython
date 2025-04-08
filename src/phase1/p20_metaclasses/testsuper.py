class A():
    def __init__(self):
        self.val = 100

    def do_it(self):
        print("DOIT")

class B(A):
    def __init__(self):
        self.prog = "XYZ"
        super().__init__(self)

    def do_it_too(self):
        print("")
        super().do_it(self)


