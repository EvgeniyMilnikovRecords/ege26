a = []
for n in range(0, 100000):
    r = f'{n:b}'
    if n % 3 == 0:
        r = r + r[-3:]
    else:
        r1 = int(n % 3) * 3
        r += f'{r1:b}'
    r = int(r, 2)
    if r > 151:
        a.append(r)
print(min(a))
