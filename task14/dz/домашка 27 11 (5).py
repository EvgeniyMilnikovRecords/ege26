a = []
for n in range(1 , 100000):
    r = f'{n:b}'
    if n % 2 == 0:
        r += f'{r.count('1'):b}'
    else:
        r = '1' + r + '101'
    if int(r, 2) > 350:
        a.append(n)
print(min(a))


#####
#r += r.count('1')
#TypeError: can only concatenate str (not "int") to str