from math import log2, ceil
for L in range(1, 100_000):
    N = 10 + 26 + 450
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 708 > 213 * 2**10:
        print(L)
        break