a = []
for n in range(1,100_000):#(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    r = f'{n:b}'
    if sum(map(int, r)) % 2 == 0:
        r = '10' + r[2:] + '1'
    else:
        r = '1' + r[2:] + '11'
    r = int(r, 2)
    if r >= 100:
        a.append(n)
print(min(a))
