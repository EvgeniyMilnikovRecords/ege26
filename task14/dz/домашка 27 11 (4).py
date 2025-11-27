from string import printable as alph

def convert(num, sys):
    res = ''
    while num:
        res += alph[num % sys]   # почему скобки квадратные?
        num //= sys
    return res[::-1]
for x in range(1 , 3001):
    num = convert(9*11**210 + 8*11**150 - x, 11)
    if num.count('0') == 60:
        print(x)

#2992 НАЙС