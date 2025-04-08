import cupy as cp
import time

N = 1000
iterations = 200

T = cp.zeros((N, N))
T[N//2 - 50:N//2 + 50, N//2 - 50:N//2 + 50] = 100.0

start = time.time()

for _ in range(iterations):
    T[1:-1, 1:-1] = 0.25 * (
        T[2:, 1:-1] + T[:-2, 1:-1] + T[1:-1, 2:] + T[1:-1, :-2]
    )

cp.cuda.Stream.null.synchronize()
end = time.time()

print(f"🔥 CuPy (GPU) : {end - start:.3f} s")
