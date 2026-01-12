from string import printable as alph

def convert2(num, sys):
    res = ''
    while num != 0:
        res += alph[num % sys]
        num //= sys
    return res[::-1]


for n in range(1, 100000):
    r = convert2(n, 3)
    if r[0] + r[1] + r[2] % 2 == 0:
        r = '1' + r + '2'
    else:
        r = '2' + r + '0'
    r = int(r, 3)
    if r >100:
        print(r)
