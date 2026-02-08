from fnmatch import fnmatch

for n in range(124605 - 124605 % 161, 10**8, 161):
    if fnmatch(str(n), '12*4?65'):
        print(n , n // 161)


########################################################
from itertools import product
from string import printable

a = []
for v in printable[:10]:
    for l in range(0 , 3):
        for m in product(printable[:10], repeat = l):
            num = int(f'12{''.join(m)}4{v}65')
            if num % 161:
                a.append([num, num//161])

for i in sorted(a):
    print(*i)