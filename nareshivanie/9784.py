def f(a):
    for x in range(0, 1000):
        for y in range(0, 1000):
            f = (x * y < a) or (x < y) or (9 < x)



for a in range(-1000, 1000):
    if f(a):
        print(a)
