with open(r'.\files\23193.txt') as file:
    data= [list(map(int, i.split())) for i in file]

for line in data:
    amount = sorted([line.count(i) for i in set(line)])