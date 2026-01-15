from itertools import product
from string import printable

for val in (product(printable[25:], repeat = 4)):
    val = ''.join(val)
    if val[0] != '0' and val.count('13579BDFHJLNP') == 1 and val.count('12345') <= 2:
        print(val)
