def f(num):
    d = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            d.append(i)
        d.append(num)

def f2(num):
    d = []
    for i in range(1, num + 1):
        if num % i == 0:
            d.append(i)

def f3(num):
    d = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            d.append(i)
            d.append(num // i)
        d.append(num)

#########################################################################


