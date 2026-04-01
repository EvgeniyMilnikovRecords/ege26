# with open(r'.\files\27629.txt') as file:
#     data = [int(i) for i in file]
#
# max43 = max(i for i in data if 1000 <= abs(i) <= 9999 and abs(i) % 100 == 43
# a = []
# for num1, num2 in zip(data, data[1:]):
#     u1 = 1000 <= abs(num1) <= 9999
#     u2 = 1000 <= abs(num2) <= 9999
#     if u1 + u2 >= 1 and (num1 + num2) **2 < max43** 2:
#         a.append((num1 + num2)**2)
#
# print(len(a), max(a))

###############################################################

with open(r'.\files\27629.txt') as file:
    data = [int(i) for i in file]

candidates = [i for i in data if 1000 <= abs(i) <= 9999 and abs(i) % 100 == 43]

# Если список не пустой — берем макс, если пустой — выводим ошибку и стопаем
if not candidates:
    print("В файле нет четырехзначных чисел, оканчивающихся на 43!")
else:
    max43 = max(candidates)
    max43_sq = max43 ** 2

res = []
for i in range(len(data) - 1):
    n1, n2 = data[i], data[i + 1]

# Условие 1: Хотя бы одно число четырехзначное
u1 = 1000 <= abs(n1) <= 9999
u2 = 1000 <= abs(n2) <= 9999

sum_sq = (n1 + n2) ** 2

# Условие 2: Квадрат суммы < квадрата максимального 43
if (u1 or u2) and sum_sq < max43_sq:
    res.append(sum_sq)

# В ответе: количество и МАКСИМАЛЬНЫЙ ИЗ КВАДРАТОВ сумм
print(len(res), max(res))


