a = []
for n in range(1, 100_000):
    r = f'{n:b}'
    if r[0] == '1':
        r = r.replace('1', '*')
        r = r.replace('0', '1')
        r = r.replace('*', '0')
    r = int(r, 2)
    if n - r  == 999:
        print(n)
        break


