from  itertools import product

alph = sorted('теория')
for pos, val in enumerate(product(alph, repeat = 6), start =1):
    val = ''.join(val)
    if  val[0] != 'р' and val[0] != 'т' and val[0] != 'я':
        if val.count('и') >= 2:
            print(pos)
