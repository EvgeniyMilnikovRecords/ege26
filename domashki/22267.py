def convert(num, sys):
    res = ''
    while num != 0:
        res = str(num%sys)
        num // sys
    return res[::-1]

ans = []
for n in range(1, 100000):
    r = convert(n, 7)
    if r[-1:] == 2:
        for r in '1':
            r.replace('1', '*')
        for r in '3':
            r.replace('3', '1')
        for r in '*':
            r.replace('*', '3')
        r = '21' + r

    else:
        r = r[0].replace('1234567', '1') + '36'
    r = int(r, 7)
    if r < 744:
        ans.append([r, n])
        ans = sorted(ans, key=lambda x: (-x[0], x[1]))
        print(ans[0])
