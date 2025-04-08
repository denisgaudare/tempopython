import random

import bigO

@bigO.track(lambda x: len(x))
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
"""

Essayer aussi 
@bigO.bounds(lambda x: len(x),
             time="O(n*log(n))",
             mem="O(n)")
"""
nombres = [i for i in range(1,100)]
random.shuffle(nombres)

def main():
    for _ in range(30):
        test_list = nombres.copy()
        bubble_sort(test_list)

#https://blog.teclado.com/time-complexity-big-o-notation-python/#2whatisbigo
"""
essaye aussi scalene
https://pypi.org/project/scalene/0.9.15/
deja installé sur cette machine
"""

from pyinstrument import Profiler
# https://pypi.org/project/pyinstrument/
profiler = Profiler()
profiler.start()
main()
profiler.stop()
print(profiler.output_text(unicode=True, color=True))


