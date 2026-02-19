def f(n):
    for a in range(113, 10 ** 6, 113 * 2):
        for b in range(0, 13):
            if a + 3 ** b == n:
                print(n, b)
    return 0


cnt = 0
for n in range(100_000, 1_000_000, 2):
    if '0' not in str(n) and (m := f(n)):
        print(n, m)
        cnt += 1
        if cnt == 5:
            break
