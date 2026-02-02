def f(a):
    for x in range(0, 1000):
        for y in range(0, 1000):
            f = (x >= 27 ) or (2*x < 3*x) or ((x+2)*(y - 3) <a)
            if not f:
                return False
    return True

for a in range(0 , 1000):
    if f(a):
        print(a)
