from itertools import *

def f(w, x, y, z):
    return (x <= y) and z and not w

for i in product((0, 1), repeat = 6):
    table = [
        (0, 1, i[0], i[1]),
        (1, 1, i[2], i[3]),
        (1, i[4], 1, i[5])
    ]

    if len(set(table)) == len(table):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
                print(*p, sep = '')