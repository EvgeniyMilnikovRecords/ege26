def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f =  not((x + 5 < a) <= (y > a)) or (x * y >= 76)
            if not f:
                return False
    return True

for a in range(1, 1000):
    if f(a):
        print(a)
        break