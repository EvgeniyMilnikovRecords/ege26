def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

a = []
for n in range(1, 100000):
    r = convert(n, 3)

    if n % 2 == 0:
        r += r[-2:]
    else:
        new_r = r.count('1')  + r.count('2') * 2
        new_r_2 = convert(new_r, 3)
        r = r + new_r_2
    r = (int , 3)
    if n >9:
        a.append([r, n])
print(min(a))



