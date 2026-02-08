def f (a):
    for m in range(2, int(a ** .5) + 1):
        if a % m ==0:
            return m + a//m
    return 0
cnt = 0
for i in range(800_001, 8_000_000):
    summ = f(i)
    if summ:
        if summ % 10 == 4:
            print(i, summ)
            cnt += 1
            if cnt == 5:
                break

