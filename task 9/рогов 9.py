with open(r'.\files\9rogov.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for line in data:
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [3, 3, 3, 1, 1, 1]:
        pov = [line.count(i) for i in line > 1]