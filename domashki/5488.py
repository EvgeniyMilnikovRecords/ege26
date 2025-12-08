from itertools import product

alph = sorted('полина')
cnt = 0
for val in product(alph, repeat= 8):
    val = ''.join(val)
    if val.count('о') + val.count('и') + val.count('а') < val.count('п') + val.count('л') + val.count('н'):
        cnt += 1
    print(cnt)


#610173