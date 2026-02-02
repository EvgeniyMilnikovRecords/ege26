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
            if is_prime(i): d.add(i)
            if is_prime(num // i): d.add(num // i)

    if len(d) >1:
        m = min(d) + max(d)
        if m > 60_000 and str(m) == str(m)[::-1]:
            return m
    return 0
cnt = 0
for i in range(5_400_001, 10**20):
    if m:= f(i):
        print(i, m)
    cnt += 1
    if cnt == 5:
        break



