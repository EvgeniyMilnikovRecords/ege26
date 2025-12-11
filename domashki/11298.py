from itertools import product

alph = sorted('жопазю')
cnt = 0
for pos, val in enumerate(product(alph, repeat = 6), start=1):
    val = ''.join(val)
    if val[0] == 'а' and val.count('з') >= 2 and pos % 2 == 0:
        cnt += 1
        print(cnt)

#513