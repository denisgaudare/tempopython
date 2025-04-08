import random

import bigO

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


nombres = [i for i in range(1,100)]
random.shuffle(nombres)

def main():
    for _ in range(30):
        test_list = nombres.copy()
        bubble_sort(test_list)

if __name__=="__main__":
    main()



