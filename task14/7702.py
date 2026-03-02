# x in [0, 17]
# y in [0, y - 1]

# y in [9, 17]
ans = []
from string import printable as p
for y in range(9, 18):
    for x in range(y):
        num1 = int(f'5{p[x]}{p[y]}A', 18)
        num2 = int(f'18{p[x]}7', y)
        num = num1 + num2
        ans.append(num)
print(len(set(ans)))
