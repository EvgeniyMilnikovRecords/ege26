def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# 1. Заранее находим простые числа, содержащие '5'
# Т.к. произведение 5 множителей > 13.4 млн, множители не будут огромными
primes_with_5 = [i for i in range(2, 10000) if is_prime(i) and '5' in str(i)]

results = []
# 2. Перебираем числа от 13 475 125 и ищем их простые множители
for n in range(13475124 + 1, 20000000):
    temp_n = n
    factors = []

    # Пытаемся разложить число только на те простые, где есть '5'
    for p in primes_with_5:
        while temp_n % p == 0:
            factors.append(p)
            temp_n //= p
        if temp_n == 1: break
        if len(factors) > 5: break  # Сразу выходим, если множителей уже больше 5

    # 3. Если число разложилось ровно на 5 подходящих простых множителей
    if temp_n == 1 and len(factors) == 5:
        results.append((n, max(factors)))

    if len(results) == 5:  # Нашли первые 5 чисел
        break

# Вывод ответа
for res in results:
    print(res[0], res[1])
