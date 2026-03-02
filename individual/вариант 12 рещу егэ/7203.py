from itertools import *
alph = 'гепард'
cnt =0
for val  in product(alph, repeat = 5):
    val = ''.join(val)
    if val.count('г') == 1 and val[0] != 'а' and val[-1] != 'е':
        cnt += 1

print(cnt)

