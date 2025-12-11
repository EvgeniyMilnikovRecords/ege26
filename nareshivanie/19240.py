from itertools import product

alph = sorted('январь')
cnt = 0
for pos, val in enumerate(product(alph, repeat = 5), start = 1):
    val = ''.join(val)
    if val