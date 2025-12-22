ans =[]
def convert (num , sys ):
    res = ''
    while num != 0:
        res = res + str(num % sys)
        num = num // sys
    return res[::-1]

for n in range(1, 100000):
    r = convert(n , 3)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r = r + convert(sum(map(int, r ))*3, 3)
    r = int(r , 3)
    if r % 2 == 1 and r > 208:
        ans.append(r)
print(min(ans))





