with open(r'.\files\17.txt') as file:
    data = [int(i) for i in file]

max10 = max(int(i) for i in data if i % 100 == 10)
a = []
for num1, num2 in zip(data, data[1:]):
    u = (num1 % 2023) * (num2 % 2023)
    if u >= max10:
        a.append(num1 + num2)
print(len(a), min(a))