

r = range(10)
print(type(r))


def monrange(limite):
    i = 0
    while i<limite:
        yield i
        i+=1

def fibo():
    a,b = 0,1
    while True:
        yield a
        a,b=b,a+b

"""
mr = monrange(5)
for i in mr:
    print(i)
"""
mr = monrange(5)
print(next(mr))
print("----")
print(next(mr))
print("----")
print(next(mr))

fib = fibo()
for i in range(100):
    print(">>>>",next(fib))