from itertools import permutations

graph = 'еа аб бж жи ив вд ди жд дб гж гб аг ге'.split()
matrix = '56 4568 78 2578 1246 125 348 2347'.split()

print(*range(1, 9))
for i in permutations('абвгдежи'):
    if all(str(i.index(x) + 1 ) in matrix[i.index(y)] for x , y in graph):
        print(*i)