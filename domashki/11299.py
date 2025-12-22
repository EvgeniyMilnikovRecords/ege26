from itertools import product

alph = sorted('бмюрн')

for pos, val in enumerate(product(alph, repeat = 6), start = 1):
    val = ''.join(val)
    if val[0] != 'м' and val.count('р') >= 2 and val.count('ю') == 0:
        print([pos , val])

#11719