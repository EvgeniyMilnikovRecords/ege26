def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num // 2
    for i in range(3, int(num // 2 + 1), 2):
        while num % i == 0:
            d += [i]
            num //= i

    if num > 2:
        d += [num]
    return d