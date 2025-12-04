from itertools import product

alph = sorted('зеркало')
cnt = 0
for val in product(alph, repeat = 6):
    if 1 <= val.count('к') <= 4:
        