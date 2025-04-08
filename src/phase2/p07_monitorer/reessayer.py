
from retry import retry
from retry.api import retry_call

nombre = 0
@retry(ZeroDivisionError, tries=3, delay=2)
def make_trouble(*args):
    global nombre
    print("try")
    1/nombre
    nombre-=1


def what_is_my_ip(approach=None):
    if approach == "optimistic":
        tries = 1
    elif approach == "conservative":
        tries = 3
    else:
        tries = 2
    result = retry_call(make_trouble,
                    tries=tries, delay=2)

make_trouble()