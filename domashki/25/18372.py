cnt = 0
for i in range(770_000 - 1, 1, -1):
    summ = [1]
    for m in range(2, i):
        if i % m == 0:
            summ.append(m)
    ar = sum(summ) // len(summ)
    if ar % 100 == 12:
        cnt += 1
        print(i, ar)
        if cnt == 5:
            break

