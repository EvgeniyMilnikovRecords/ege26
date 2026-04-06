from string import printable
from itertools import *
cnt = 0
for val in product(printable[:7], repeat = 7):
    if val[0] != 0 and val[0] != 3 and val[0] != 5:
        if '2244' not in val and '4422' not in val:
            cnt += 1

print(cnt)