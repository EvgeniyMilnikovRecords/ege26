from itertools import permutations

for val in permutations('росомаха'):
    val = ''.join(val)
    for i in 'рсмх':
        val = val.replace(i , '*')