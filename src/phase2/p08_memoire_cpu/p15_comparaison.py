# pip install pyperf

import random
import pyperf

def generate_data(n=500, seed=42):
    random.seed(seed)
    return [random.randint(-100, 100) for _ in range(n)]

def find_zero_sum_triplets_bruteforce(arr):
    n = len(arr)
    triplets = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplets.append((arr[i], arr[j], arr[k]))
    return triplets

def find_zero_sum_triplets_optimized(arr):
    arr.sort()
    n = len(arr)
    triplets = set()
    for i in range(n - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        a = arr[i]
        left = i + 1
        right = n - 1
        while left < right:
            total = a + arr[left] + arr[right]
            if total == 0:
                triplets.add((a, arr[left], arr[right]))
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return list(triplets)

def bench_bruteforce(loops):
    data = generate_data()
    for _ in range(loops):
        find_zero_sum_triplets_bruteforce(data)
    return True

def bench_optimized(loops):
    data = generate_data()
    for _ in range(loops):
        find_zero_sum_triplets_optimized(data)
    return True

if __name__ == "__main__":
    runner = pyperf.Runner()
    runner.bench_func("triplets_bruteforce", bench_bruteforce,5)
    runner.bench_func("triplets_optimized", bench_optimized,5)

### 3. **Lancer le benchmark**
"""
 🧠 Astuces supplémentaires

  python bench_triplets.py --filter optimized
  python bench_triplets.py --output optimized.json
  python bench_triplets.py --output brute.json
  
  pyperf compare_to optimized.json brute.json
"""