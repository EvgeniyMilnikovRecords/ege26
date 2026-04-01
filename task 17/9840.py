with open(r'files/17_9840.txt') as file:
    data = [int(i) for i in file]

max39 = (i for i in data if abs(i) % 100 == 39)

for num1, num2 in zip(data, data[1:]):
    u1 = num1