res = []

for n in range(1, 30):
    r = bin(n)[2:]

    if r.count('1') % 2 == 0:
        r = '10' + r
        r = r[:-2] + '00'
    else:
        r = '11' + r
        r = r[:-2] + '11'

    res.append(int(r, 2))

print(max(res))