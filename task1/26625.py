from itertools import permutations

graph = 'ae ec cd df fb bg ga eb cf'.split()
matrix = '456 37 25 16 137 147 256'.split()

print(*range(1, 8))

for i in permutations('abcdefg'):
    if all(str(i.index(x) + 1 ) in matrix[i.index(y)] for x, y in graph):
        print(*i)