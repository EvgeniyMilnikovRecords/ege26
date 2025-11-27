num = 0

for n in range(10000, 100000):
    kv = int(min(str(n))) + int(max(str(n))) ** 2
    pr = 1
    for i in range(0, 5):
        if int(str(n)[i]) % 2 == 0:
            pr *= int(str(n)[i])
    if kv > pr:
        num = str(pr) + str(kv)
    else:
        num = str(kv) + str(pr)

    if int(num) == 12116:
        print(n)
        break
