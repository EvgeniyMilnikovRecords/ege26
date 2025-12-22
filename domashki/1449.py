from itertools import permutations
graph = 'аб бв вд де ек кг ге вг ав ве'.split()
matrix = '24 146 56 1267 36 23457 46'.split()
print(*range(1, 8))
for i in permutations('абвгдек'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
