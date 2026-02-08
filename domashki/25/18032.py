for i in range(1000, 10000):
    summ = i + 1
    for m in range(2, i):
        if i % m == 0:
            summ += m
    if summ % 100 == 23:
        print(i, summ)

