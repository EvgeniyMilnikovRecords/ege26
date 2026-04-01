from math import log2, ceil
for N in range(1, 100_000):
    L = 105
    i = ceil(log2(N))
    I = ceil(L *i / 8)
    if I * 65_536 >= 7 * 2**20:
        print(N)
        break
