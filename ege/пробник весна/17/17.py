with open(r'.\files\17.txt') as file:
    data = [int(i) for i in file]

max2 = max(i for i in data if len(str(i)) == 2)
a = []
for num1, num2 in zip(data, data[1:]):
    u1 = len(str(num1)) == 2
    u2 = len(str(num2)) == 2
    if u1 + u2 == 1 and (num1 + num2) % max2 == 0:
        a.append(num1 + num2)

print(len(a), max(a))