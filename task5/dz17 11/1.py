
def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]
for N in range(1, 100000):
    R = convert(N, 3)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += str(convert(R.count('1') + R.count('2') * 2, 3))
    if int(R, 3) % 2 == 0 and int(R, 3) > 220:
        print(int(R, 3))
        break