from itertools import product

alph = sorted('нормалье')
norm = 0
nenorm = 0

for pos , val in enumerate(product(alph, repeat = 6), start = 1):
    val = ''.join(val)
    if val == 'ненорм':
        nenorm = pos
    if val[:4] == 'норм':
        norm = pos
        break

print(norm - nenorm -1)

#ответ 17228
