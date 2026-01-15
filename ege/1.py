from itertools import permutations

graph = 'ag gf fe ed da ab gb bc cd'.split()
matrix = '26 147 456 236 37 134 25'.split()

print(*range(1, 8))
for i in permutations('abcdefg'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
