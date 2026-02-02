from itertools import *
alph = sorted('катер')

for pos, val in enumerate(product(alph, repeat = 6), start = 1):
    val = ''.join(val)
    if 'карета' in val:
        print(pos)

#9671
#6671 №ответ 3000