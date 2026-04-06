from itertools import permutations


from itertools import permutations

def f(x):
    p = 15 <= x <= 40
    q = 21 <= x <= 63
    a = a1 <= x <= a2
    return p <= ((q and not a) <= (not p))

line = [x+eps for x in range(15, 63) for eps in(0, 0.1, 0.9)]

a = []
for a1, a2, in permutations(line, 2):
    if all(f(x) for x in line):
        a.append(a2 - a1)

print(min(a))