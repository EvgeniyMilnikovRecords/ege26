from itertools import combinations

def f(x):
    p = 25 <= x <= 73
    q = 75 <= x <= 118
    a = a1 <= x <= a1
    return (a and not q) <= (p or q)

line_a = [25, 73, 75, 118]
line_x = [50, 74, 100]
ans = []
for a1, a2 in combinations(line_a, 2):
    if all(f(x) for x in line_x):
        ans.append(a2-a1)
print(max(ans))