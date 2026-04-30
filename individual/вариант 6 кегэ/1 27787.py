from itertools import *

graph = 'ac cf fg ge eb ab bc ef bd dc ed df'.split()
matrix = '2345 14 1456 1236 1367 3457 56'.split()

print(*range(1, 8))

for i in permutations('abcdefg'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)