from itertools import *
from string import printable
cnt = 0
for val in product(printable[8:], repeat = 5):
    val = ''.join(val)
    if val[0] != '0' and val.count('1') == 0:
        for i in val:
            if i in '02468':
                val = val.replace(i , '*')
            if i in '1357':
                val = val.replace(i, '&')
        if '**' not in val and '&&' not in val:
            cnt += 1
print(cnt)
