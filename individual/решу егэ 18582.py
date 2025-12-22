a =[]
for n in range(1, 100000):
    r = f'{n:b}'
    if r.count('1') > r.count('0'):
        r += '1'
    if r.count('0') > r.count('1') and r.count('0') == r.count('1'):
        r += '0'
    r = int(r, 2)
    if r > 100:
        a.append(r)
        print(min(a))