from itertools import permutations

alph = 'хочунабюджет'
cnt = 0
for val in permutations(alph, r = 12):
    val = ''.join(val)
    for i in val:
        if i in 'оуаюе':
            val = val.replace(i , '&')
    if '&&&&&' not in val:
        cnt += 1
print(cnt)
