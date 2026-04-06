from math import log2, ceil

for N in range(1, 100_000):
    L = 377
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 23_155 > 5536 * 2 ** 10:
        print(N)
        break