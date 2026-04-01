with open(r'files/17_4597.txt') as file:
    data = [int(i) for i in file]

minn = min(data)

ans = []
for i in range(len(data) - 1):
    num1, num2 = data[i:i+2]
    x1 = num1 % 117 == minn
    x2 = num2 % 117 == minn
    if (x1 or x2) and any([x1, x2]) and x1 + x2 >= 1:  #разные варианты проверки
        ans.append(num1 + num2)

print(len(ans), max(ans))


'######################################################################'

with open(r'files/17_4597.txt') as file:
    data = [int(i) for i in file]


minn = min(data)


print(minn)
ans = []
for num1, num2 in zip(data, data[1:]):
    x1 = num1 % 117 == minn
    x2 = num2 % 117 == minn
    if (x1 or x2) and any([x1, x2]) and x1 + x2 >= 1:  #разные варианты проверки
        ans.append(num1 + num2)

print(len(ans), max(ans))