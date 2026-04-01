with open(r'.\filesdz\17_1970.txt')as file:
    data = [int(i) for i in file]

minn = min(data)

a = []
for num1, num2 in zip(data, data[:1]):
    x1 = num1 % 3 == minn
    x2 = num2 % 3 == minn
    if x1 or x2 >= 1:
        a.append(num1 + num2)

print(len(a), max(a))