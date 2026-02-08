from fnmatch import fnmatch

print(12347 %141 )
for n in range(12347 - 12347 % 141,  10**8, 141):
    if fnmatch(str(n), '1234*7'):
        print(n, n// 141)

###########################################################

from itertools import product

for l in range(0, 4):
    for val in product('0123456789', repeat =l):
        val = int('1234' + ''.join(val) + '7')
        if val %141 == 0:
            print(val , val//141)