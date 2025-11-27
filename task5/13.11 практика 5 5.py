def convert (num , sus):
    res = ''
    while num != 0:
        res += str(num % sus)
        num //= sus
    return res[::-1]

a = []
for n in range(1 , 1000000):
    r =  convert(n , 3)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        r = r + convert(n % 3 * 4, 3)
    r = int(r, 3)
    if r < 199:
        print(n)

