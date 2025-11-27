# Системы счисления

# Двоичная система
N = 25
# bin() - переводит десятичное число в двоичную систему.
# Принимает на вход int, возвращает str.
# [2:] - срез, убирающий первые два символа '0b'
print(bin(N)[2:])
# f'' - форматируемая строка, которая позволяет вставлять в себя переменные
print(f'{N:b}')

# Восьмеричная система
print(oct(N)[2:])
print(f'{N:o}')

# Шестнадцатеричная система
print(hex(N)[2:])
print(f'{N:x}')


# Перевод в любую систему (2 <= sys <= 9)
def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]


# Перевод в любую систему (2 <= sys <= 36)
from string import printable as alph


def convert2(num, sys):
    res = ''
    while num != 0:
        res += alph[num % sys]
        num //= sys
    return res[::-1]


# Перевод в 10 систему
num_bin = '101'
num_tri = '121'
num_hex = 'fa8'

print(int(num_bin, 2))
print(int(num_tri, 3))
print(int(num_hex, 16))

# Срезы
test = 'Hello world!'
# Извлечение первых двух символов
print(test[:2])
# Строка без первых двух символов
print(test[2:])
# Извлечение последних двух символов
print(test[-2:])
# Строка без последних двух символов
print(test[:-2])

# Сумма цифр числа
# Двоичное число
num_1 = '1010'
print(num_1.count('1'))

# Системы до 10 включительно
num_2 = '823'
print(sum(map(int, num_2)))

# Системы до 36 включительно
num_3 = 'AF5'
print(sum(map(lambda x: int(x, 36), 'AF5')))

print(*map(lambda lol: lol + 10, [3 , 4, 5]))