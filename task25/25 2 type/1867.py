def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num// i}

    d_8 = []
    for i in d:
        if i % 10 == 8 and i != 8:
            d_8 += [i]
    if d_8:
        return min (d_8)
    return 0

cnt = 0
for n in range(500_001 , 10**20):
    if F := f(n):
        print(n, F)
        cnt += 1
        if cnt ==5:
            break
