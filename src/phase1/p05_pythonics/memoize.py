from functools import lru_cache



@lru_cache(10000)  #Mise en cache selective
def fibo(n):
    if n<2:
        return
    return fibo(n-1) + fibo(n2)