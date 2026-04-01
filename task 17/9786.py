with open(r'files/17_9786.txt') as file:
    data = [int(i) for i in file]

max_25 = max(i for i in data if abs(i) % 100 == 25)

a = []

for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = len(str(num1)) ==4
    u2 = len(str(num1)) ==4
    u3 = len(str(num1)) ==4
    if u1 + u2 + u3 <= 2 and num1 + num2 + num3 <= max_25:
        a.append(num1 + num2 + num3)

print(len(a), max(a))