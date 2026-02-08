from fnmatch import fnmatch


# Функция для подсчета количества и суммы делителей
def get_divs_info(n):
    divs = set()
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            divs.add(d)
            divs.add(n // d)
    return len(divs), sum(divs)


# Начинаем с первого числа, кратного 53
start = 53
results = []

# Перебираем числа до 10^7 с шагом 53
for i in range(start, 10 ** 7 + 1, 53):
    s = str(i)

    # 1. Проверяем на палиндром (читается одинаково в обе стороны)
    if s == s[::-1]:

        # 2. Проверяем соответствие маске *2?2*
        if fnmatch(s, '*2?2*'):

            # 3. Считаем количество и сумму делителей
            count_divs, sum_divs = get_divs_info(i)

            # 4. Проверяем условие на количество делителей (> 30)
            if count_divs > 30:
                results.append((i, sum_divs))

# Вывод результата в порядке возрастания
for res in sorted(results):
    print(res[0], res[1])
