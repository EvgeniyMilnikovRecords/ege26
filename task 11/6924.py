from math import log2, ceil
for L in range(1, 100_000):
    N = 4190
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I <= 604 * 2**10/2048:
        print((L))