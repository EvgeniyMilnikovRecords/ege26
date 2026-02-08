from itertools import *

alph = 'масло'
cnt = 0
for val in product(alph, repeat = 6):
    val = ''.join(val)
    for i in val:
        if i in 'ао':
            val = val.replace(i, '&')
    if val.count('&') == 1:
        cnt += 1
print(cnt)