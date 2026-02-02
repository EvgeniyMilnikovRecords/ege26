for n in range(1, 100_000):
    r = f'{2+n:b}'
    r1 = int(r.count('1') % 2)
    r += str(r1)
    r = int(r, 2)
    if r < 61:
        print(n)

        #28