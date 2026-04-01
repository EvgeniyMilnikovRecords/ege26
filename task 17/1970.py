with open(r'.\files\17_1970 (1).txt') as file:
    data = [int(i) for i in file]

maxx = (i for i in data if i % 3 == 0)

a = []

for num1, num2 in zip(data, data[1:]):
    u1 = num1 % 3 == 0
    u2 = num2 % 3 == 0
    if u1 + u2 >= 1:
        a.append(num1 + num2)

print(len(a), max(a))