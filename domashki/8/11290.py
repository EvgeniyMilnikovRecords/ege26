from itertools import product
from string import printable
cnt = 0
for val in product(printable[:16], repeat = 4):
    val = ''.join(val)
    if val[0] != '0':
        if val.count('9') == 1:
            for i in val:
                if i in '02468ACEG':
                    val = val.replace(i, '&')
                if i in '13579BDF':
                    VAL = val.replace(i , '*')
            if '**' not in val and '&&' not in val:
                cnt +=1
print(cnt)

#ABCDEFGH A = 10, B =11, C= 12, D = 13, E = 14, F = 15, G = 16