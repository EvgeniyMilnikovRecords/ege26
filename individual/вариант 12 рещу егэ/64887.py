from itertools import product, permutations
def f(x, y, z, w):
    return ((x == y) <= ((not z) or w)) == (not((w <= x) or (y <= z)))
for i in product((0, 1), repeat=5):
    table = [
        (0, 1, i[0], i[1]),
        (i[2], i[3], 1, 0),
        (0, i[4], 0, 0)
    ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
                print(''.join(p))
