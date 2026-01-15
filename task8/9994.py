from itertools import product

alph = sorted('школа')

for pos, val in enumerate(product(alph, repeat = 5), start = 1):
    val = ''.join(val)
    if 'шалаш' in val:
        print(pos)
