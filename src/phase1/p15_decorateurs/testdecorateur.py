import inspect

from phase1.p15_decorateurs.decorators import debuglogger, check_types, checkarguments


@debuglogger
def foo(a=1,b=2):
    """
    Je fais pas grand chose
    :param a:
    :param b:
    :return:
    """
    print("FOO est dans la place")

@checkarguments
def plusfoo(a:int,b:str,cTrue):
    return "Hello"

plusfoo("A",1)
