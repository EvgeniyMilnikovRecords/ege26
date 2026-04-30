from string import printable
from itertools import *
cnt = 0
for val in product(printable[:7], repeat = 5):
    val = ''.join(val)
    if val[0] != '0' and val.count('5') == 1:
        for i in '0246':
            val = val.replace(i, '*')
        if '*5' not in val and '5*' not in val:
            cnt += 1

print(cnt)

