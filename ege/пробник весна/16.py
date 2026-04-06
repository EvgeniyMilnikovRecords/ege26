from functools import lru_cache

@lru_cache(None)
def g(n):
    if n < 8: return 3 * n
    return g(n - 3) + 2

for i in range(-10_000, 12_345):
    g(i)

def f(n):
    return 3 * (g(n - 2) + 5)

print(f(12345))

