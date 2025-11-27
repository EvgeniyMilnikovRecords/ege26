def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

a = []
for n in range(1, 109209):
    r= convert(n, 3)
    if n % 3 ==0:
        r = r + r[-2:]
    else:
        r = r + convert(n % 3 * 5 , 3)
    r = int(r , 3)
    if r > 133:
        a.append(r)
print(min(a))