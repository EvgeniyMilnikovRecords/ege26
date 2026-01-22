def f(a):
    for x in range(0, 1000):
        for y in range(0, 1000):
            f = (2*y + 3*x != 135) or (y> a) or (x > a)
            if not f:
                return False
    return True

for a in range(0,1000):
    if f(a):
        print(a)
