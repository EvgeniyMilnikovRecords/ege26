a = []
for n in range(1, 100_000):
    r = f'{n:b}'
    m = r[:2][::-1]
    r += m
    r = int(r, 2)
    if r > 90:
        a.append(n)
print(min(a))






