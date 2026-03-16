a = []
for n in range(1, 100_000):
    r = f'{n:b}'
    if n % 3 == 0:
        r += r[-3:]
    else:
        r += f'{(n % 3) * 3:b}'
    r = int(r, 2)
    if r < 130:
        print(max(a))