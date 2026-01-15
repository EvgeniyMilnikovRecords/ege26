from itertools import product
from string import printable
cnt = 0
for val in product(printable[:6], repeat = 7):
    val = ''.join(val)
    if val[0] != '0':
        if val.count('2') == 1:
            for i in val:
                if i in '0246':
                    val = val.replace(i, '+')
            if '+2+' not in val:
                cnt += 1
print(cnt)