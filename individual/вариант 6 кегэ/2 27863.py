from itertools import *


def f(w, x, y, z):
    # Приоритет операций в Python: not > <= > or.
    # Это соответствует логике: (not y) <= (x or w)
    return (x and y <= z) and ((not (y)) <= x or w)


# Используем множество, чтобы убрать дубликаты ответов
found_orders = set()

for i in product((0, 1), repeat=6):
    table = [
        (i[0], 0, 1, i[1]),
        (0, 1, 1, 0),
        (i[2], i[3], 1, 0)
    ]

    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            # Сверяем значения функции с вектором [i[4], 0, i[5]]
            if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
                found_orders.add("".join(p))

# Печатаем только уникальные результаты
for res in found_orders:
    print(res)


