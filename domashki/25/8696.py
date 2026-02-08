# Функция для проверки, является ли число простым
def is_prime(n):
    if n < 2: return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


# Функция для поиска суммы делителей M (без 1 и самого числа)
def get_M(n):
    divs_sum = 0
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            if d * d == n:
                divs_sum += d
            else:
                divs_sum += d + (n // d)
    return divs_sum


count = 0
num = 1273547 + 1  # Начинаем с чисел, больших 1 273 547

while count < 5:
    M = get_M(num)

    if M > 0:  # Если число не простое (у простых M=0 по условию)
        remainder = M % 100000
        if is_prime(remainder):
            print(num, M)
            count += 1

    num += 1
