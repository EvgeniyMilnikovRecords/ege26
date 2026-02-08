from string import printable as alph


def convert(num, sys):
    res = ''
    while num != 0:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

cnt = 0
num = convert(2 * 729**2014 + 2 * 243**2016 - 2 * 81**2018 + 2 * 27**2020 - 2 * 9**2022 - 2024, 27)
for i in num:
    if not i in '0123456789':
        cnt += 1
print(cnt)


