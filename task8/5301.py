from itertools import product

alph = ' леся'
cnt = 0
for val in product(alph, repeat = 5):
    val = ''.join(val)
    if val[-1] not in ' ' and val[0] not in ' ' and val.count(' ') == 1:
        for i in val:
            if i in 'ея':
                val = val.replace(i , '&')
            if i in 'лс':
                val = val.replace(i , '#')
        if '##' not in val and '&&' not in val:
            cnt += 1
print(cnt)