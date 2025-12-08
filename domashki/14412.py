from itertools import product

alph = sorted('алгоритм')
alph_1 = 'лгртм'
cnt = 0
for pos, val in enumerate(product(alph, repeat=6), start = 1):
    if val[0] !=  'р' and val[-1] not in  alph_1 and val.count('л') <= 1:
        cnt += 1
        print(cnt)