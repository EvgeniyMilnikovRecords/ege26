from string import printable as alph


def convert(num, sys):
    res = ''
    while num != 0:
        res += alph[num % sys]
        num //= sys
    return res[::-1]


for x in range(1, 100000):
    num = convert(7**666 + 7**333 + 49**x - 343, 7)
    if num.count('6') ==49:
        print(x)
        break

