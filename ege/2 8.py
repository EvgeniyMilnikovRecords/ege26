from itertools import *
alph = sorted('парус')
for pos, val in enumerate(product(alph, repeat = 3), start = 1):
    val = ''.join(val)
    if val[0] == 'с':
        print(pos)
        break


#76