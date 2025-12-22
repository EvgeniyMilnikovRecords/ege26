from itertools import product
from string import printable
cnt = 0
for val in product(printable[:12], repeat=7):
    val = ''.join(val)
    if 'B' == 2 and val[0] != '0' :
        for i in '013579B':
            val = val.replace(i, '*')
        for i in '02468AC':
            val = val.replace(i, '@')
        if '@*' in val:
            cnt += 1
print(cnt)



