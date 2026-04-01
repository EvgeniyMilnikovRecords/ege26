from sys import setrecursionlimit
from functools import lru_cache

# 1. Увеличиваем лимит, так как 1000 нам явно мало
setrecursionlimit(15000)

@lru_cache(None)
def F(n):
    if n < 43: return G(n + 4)
    return 2 * F(n - 2) - F(n - 4) + 2

@lru_cache(None)
def G(n):
    if n < 11_240: return G(n + 3) + 2
    return Q(n)

@lru_cache(None)
def Q(n):
    if n < 21: return n + 4
    return Q(n - 4) + 2

# Прогреваем Q (идем снизу вверх)
for i in range(10, 11_245):
    Q(i)

# Прогреваем G (идем СВЕРХУ ВНИЗ, так как G(n) вызывает G(n+3))
for i in range(11245, 30, -1):
    G(i)

# 2. Прогреваем F (идем снизу вверх, чтобы F(n) уже знала F(n-2))
for i in range(1, 2027):
    F(i)

print(F(2026))
