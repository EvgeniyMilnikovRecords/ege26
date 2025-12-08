def convert(num , sys):
    res = ''
    while num != 0:
         res += str(num%sys)
         num = num//sys
    return res [::-1]
a=[]
for n in range(1 , 100000):
    r = convert(n , 5)
    if r [-1] == '0':
        r = '33' + r.replace('1', '*')
        r = r.replace('4', '1')
        r = r.replace('*', '4')
    if r[-1] != '0':
        r = '3' + r[1:] + '42'

    if int(r, 5) < 1922:
        a.append([int(r, 5),  n])
print(sorted(a))
