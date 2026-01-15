from itertools import product
alph = 'кайф'
cnt = 0
for val in product(alph, repeat = 4):
    val = ''.join(val)
    if val[-1] != 'й' and 'кф' not in val and val.count('к') ==1 and val.count('а') ==1 and val.count('й') ==1 and val.count('ф') ==1:
        cnt += 1
print(cnt)

#ответ 14
