def DEL(n, m):
    return n%m == 0

def f(x):
    return DEL(x , a) or (DEL(x, 23) <= (x not in range(50 , 71)))

for a in range(0 , 1000)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break