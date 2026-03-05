from math import *


L = 60
N = 260
i = ceil(log2(N))
I = ceil(L * i / 8)
print((I * 65536) / 2 ** 10)

