from itertools import *

def f(w, x, y, z):
    return not(w <= x) or (y <= z) or not y


for i in product((0, 1), repeat = 7):
    table = [
        (0, 1, i[0], i[1]),
        (i[2], 0, i[3], 1),
        (i[4], i[5], i[6], 0)
    ]
    if len(set(table)) == len(table):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
                print(*p, sep='')