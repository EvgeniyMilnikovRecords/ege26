from itertools import *

def f(x, y, z, w):
    return not(y <= (z == x)) and (w <= z)

for i in product((0, 1), repeat = 6):
    table = [
        (i[0], 0, 0, i[1]),
        (i[2], 0, 1, 0),
        (i[3], i[4], i[5], 0)
    ]

    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
                print(*p, sep='')