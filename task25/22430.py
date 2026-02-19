def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            if is_prime(i): d |= {i}
            if is_prime(num // i): d |= {num // i}
    if len(d) >= 4:
        d = sorted(d)
        m = d[0] + d[1] + d[-1] + d[-2]
        return m
    return 0

for n in range(456_789+ 1, 10**20):
    m = f(n)
    if m and m % 114 == 39:

