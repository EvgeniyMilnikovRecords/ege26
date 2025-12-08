from itertools import *
alph = sorted('дсож')

for val in product(alph, repeat=6):
    val = ''.join(val)