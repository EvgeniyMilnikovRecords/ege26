def f(num):
    for i in range(19, num + 1, 10):
        if num % i == 0:
            return i
    return False


cnt = 0
for n in range(800_001, 10 **30):
    m = f(n)
    if m:
        print(n, m)
        cnt += 1
        if cnt == 5:
            break
