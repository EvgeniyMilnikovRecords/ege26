from itertools import combinations
def f(x):
    p = 5 <= x <= 280
    q = 295 <= x <= 400
    r = 375 <= x <= 450
    a = a1 <= x <= a2
    return (q <= p) or ((not a) <= r)

line_x = [5, 280, 295, 375, 400, 450]
line_a = [6, 281, 296, 376, 401, 451]
a = []
for a1, a2 in combinations(line_a, 2):
    if all(f(x) for x in line_x):
        a.append(a2 - a1)
print(min(a))
