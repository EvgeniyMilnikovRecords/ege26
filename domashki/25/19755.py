def f(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True
for n in range(1_200_001, 100000000000):
    sp =[]
    for x in range(2, n//2 + 1):
        if n % x == 0:
            if f(x):
