from itertools import permutations

graph = 'ab bc cf fe he ah ae gb gf'.split()
matrix = '37 356 127 567 24 24 134'.split()

print(*range(1,8))

for i in permutations('abcefgh'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
