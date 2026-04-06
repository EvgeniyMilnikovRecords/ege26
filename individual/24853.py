from string import printable

def convert(num, sys):
    res = ''
    while num != 0:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

a = []
for n in range(1, 100_000):
    r = convert(n, 12)
    if n % 4 == 0:
        r ='A' + str(r) + 'B'
    else:
        r = '1' + str(r) + '0'
    r = int(r, 12)
    if r >2025:
        a.append(r)

print(min(a))


