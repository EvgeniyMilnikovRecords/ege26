```
from math import log2, ceil

# 1855
L = 101
N = 4090 + 10
i = ceil(log2(N)) # bit
I = ceil(L * i / 8) # всегда округляем в большую # byte
print(I * 2048 / 1024)

# бит > 1 байт = 8 бит = 2 * 3 бит < 1 Кбайт = 1024 байт

# ответ 330

#23270

for L in range(1, 100_000):
    N = 10 + 27
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 3548 * I > 12 * 2 ** 10:
        print(L)
        break
        ```
