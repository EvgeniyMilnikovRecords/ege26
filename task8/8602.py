from itertools import *

alph = sorted('аекнс')

for pos, val in enumerate(product(alph, repeat = 6), start = 1):
    val = ''.join(val)
    if 'сенека' in val:
        print(pos)