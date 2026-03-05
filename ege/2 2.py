from itertools import *

def f(x, y, z, w):
    return (x ==(y <= z)) and (y == (not(z <= w)))

for i in product((0,1), repeat = 5):
    table = [
        (0, 0, i[0], 0),
        (i[1], 0, i[2], 0),
        (1, 0, 1, i[3])
    ]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [1,1,0]:
                print(*p, sep = '')