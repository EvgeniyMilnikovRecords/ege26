from itertools import combinations

def f(x):
    p = 66 <= x <= 67
    o = 32 <= x <= 125
    t = 30 <= x <= 491
    a = a1 <= x <= a2
    return (not a) <= (p or not o or not t)

line_a =[30, 32, 66, 67, 125, 491]
line_x = [31, 40, 66.5, 100, 300]
a = []
for a1, a2 in combinations(line_a, 2):
    if all(f(x) for x in line_x):
        a.append(a2 -a1)
print(min(a))





