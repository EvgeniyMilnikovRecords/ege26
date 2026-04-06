with open(r'.\filess\17_9748.txt') as file:
    data = [int(i) for i in file]

min_15 = max(i for i in data if i % 100 == 15)
a = []
for num1, num2, num3 in zip(data, data[1:], data[:2]):
    u1 = len(str(num1)) == 4
    u2 = len(str(num2)) == 4
    u3= len(str(num2)) == 4
    if u1 + u2 + u3 == 1 and sum([num1, num2, num3]) >= min_15:
        a.append(num1 + num2 + num3)

print(len(a), max(a))

