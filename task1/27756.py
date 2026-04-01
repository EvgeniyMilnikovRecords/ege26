from itertools import permutations

graph = 'ah hb bf fg ge ea ed dg hc fc ac'.split()
matrix = '247 148 467 123 68 358 13 256'.split()

print(*range(1, 9))

for i in permutations('abcdefgh'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
