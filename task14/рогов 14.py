from string import printable
a = []
for x in printable[:18]:
    num1 = int(f'451{x}', 18)
    num2 = int(f'79{x}2', 18)
    num = num1 + num2
    if num % 27 == 0:
        a.append(x)

print(min(a))