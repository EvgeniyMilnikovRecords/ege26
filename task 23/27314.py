```
def f(start, end, flag):
    # 1. Отмечаем, если попали в нужную точку
    if start == 18 or start == 30:
        flag = True

    # 2. Базовый случай: дошли до цели
    if start == end:
        return 1 if flag else 0

    # 3. Условие выхода за границы или запрещенные числа
    if start > end or start in [28, 36]:
        return 0

    # 4. Рекурсивные шаги
    return f(start + 1, end, flag) + \
        f(start + 5, end, flag) + \
        f(start * 3, end, flag)


# Вызываем правильно: от 2 до 49, флаг изначально False
print(f(2, 49, False))
```