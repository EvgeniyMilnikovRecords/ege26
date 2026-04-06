from string import printable as alph

def convert(num, sys):
    res = ''
    while num != 0:
        res += alph[num % sys]
        num //= sys
    return res[::-1]
a = []
for n in range(1, 100_000):
    r = convert(n, 4)
    if n % 4:
        r += r[:2]
    else:
        t = convert(((n % 4) * 4), 4)
        r += t

    r = int(r, 4)
    if r > 291:
        a.append(r)

print(min(a))