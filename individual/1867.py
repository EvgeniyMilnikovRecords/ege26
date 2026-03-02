def f(num):
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return i + num // i
    return 0




cnt = 0
for n in range(800_001, 10 **37):
    m = f(n)
    if m % 10 == 4:
        print(n, m)
        cnt += 1
        if cnt == 5:
            break
